"""
Pipeline de investigacion: Pricing dinamico del mercado spot electrico chileno (SEN).

Modelo estructural sintetico calibrado (2020-2025, horario, semilla fija):
  M1  Series horarias de demanda y ERV (no gaussianas, estacionales)
  M2  Despacho por orden de merito -> costo marginal horario
  M3  Dos zonas (norte exportador / centro importador) con limite de
      interconexion -> desacople de precios y vertimiento zonal
  M4  BESS: arbitraje diario (carga mediodia, descarga punta) 2024-2025
  M5  Cadena tarifaria: cMg -> PN (semestral) -> PE (DS 88/2020, tope 5%)
  M6  Riesgo: VaR/CVaR del spot; sensibilidades (HVDC Kimal-Lo Aguirre, GNL)

Los datos son SINTETICOS REPRODUCIBLES calibrados a las magnitudes
documentadas del estudio (CEN/CNE/Ember/B&T). No son observaciones reales.
Cada ano usa su propia semilla, por lo que los escenarios (HVDC, GNL, BESS)
se comparan contra el mismo ruido base.

Uso:
  python src/pipeline.py            # ejecuta todo y exporta dashboard/informe
  from pipeline import *            # uso desde el notebook
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2026
ROOT = Path(__file__).resolve().parent.parent
YEARS = [2020, 2021, 2022, 2023, 2024, 2025]
H = 8760  # horas por ano (se ignora bisiesto)
COSTO_RACIONAMIENTO = 650.6  # USD/MWh (CNE, jun-2025)

# ----------------------------------------------------------------------------
# Calibracion: capacidades y factores por ano (GW / adimensional)
# ----------------------------------------------------------------------------

DEMANDA_MEDIA = {2020: 7300, 2021: 7550, 2022: 7750, 2023: 7850, 2024: 8150, 2025: 8350}  # MW
# solar utility-scale + PMGD (la PMGD, mayoritariamente norte, es clave del vertimiento)
SOLAR_CAP = {2020: 3.2, 2021: 4.2, 2022: 6.0, 2023: 8.6, 2024: 12.2, 2025: 15.0}          # GW
EOLICA_CAP = {2020: 1.7, 2021: 1.9, 2022: 2.3, 2023: 2.7, 2024: 3.2, 2025: 3.7}           # GW
HIDRO_FACTOR = {2020: 1.00, 2021: 0.78, 2022: 0.68, 2023: 0.72, 2024: 1.08, 2025: 0.96}   # sequia 2021-23, humedo 2024
CARBON_CAP = {2020: 4.6, 2021: 4.3, 2022: 3.8, 2023: 3.3, 2024: 2.7, 2025: 2.2}           # GW (retiros)
GNL_CAP = {2020: 4.6, 2021: 4.8, 2022: 5.0, 2023: 5.2, 2024: 5.4, 2025: 5.6}              # GW
GNL_F = {2020: 1.30, 2021: 1.85, 2022: 2.95, 2023: 2.60, 2024: 1.30, 2025: 1.25}          # mult. CV GNL (crisis Ucrania)
BESS_GW = {2024: 1.1, 2025: 1.6}                                                          # potencia instalada
LIMITE_INTERCAMBIO = {2020: 1350, 2021: 1400, 2022: 1400, 2023: 1600, 2024: 1750, 2025: 1750}  # MW

# Disponibilidad efectiva de unidades (outages, mantenimientos, minimos tecnicos)
DISP = {"carbon": 0.52, "gnl": 0.88, "diesel": 0.90}
# Piso del cMg en horas de vertimiento: componentes SSCC y costos de arranque
# mantienen el costo marginal positivo aun con excedente (estudio, Parte III.3)
PISO_VERTIMIENTO = 8.0

CV_BASE = {
    "hidro_pasada": 8, "hidro_embalse": 13, "biomasa": 18,
    "carbon": 29, "gnl": 44, "diesel": 118,
}

# Reparto zonal (norte = Antofagasta-Atacama-Coquimbo; centro = resto)
ZONA = {
    "demanda_n": 0.18, "solar_n": 0.72, "eolica_n": 0.42, "carbon_n": 0.32,
    "gnl_n": 0.30, "hidro_n": 0.08, "diesel_n": 0.18,
}

# Anclas documentadas (estudio + dashboard; CEN, CNE, Ember, B&T)
ANCLAS = {
    "precio_medio_quillota": {2020: 52, 2021: 72, 2022: 104, 2023: 107, 2024: 61, 2025: 75},
    "vertimiento_gwh": {2022: 1810, 2023: 2376, 2024: 5909, 2025: 6205},
    "vertimiento_potencial_2025": 8200,
    "spread_medio": (5, 15),
    "spread_max": 48,
    "noche_dia_2022": 98.1,
    "cmg_mensual": {
        "crucero": {2020: 43, 2021: 61, 2022: 79, 2023: 78, 2024: 51, 2025: 53},
        "quillota": {2020: 52, 2021: 72, 2022: 104, 2023: 107, 2024: 61, 2025: 75},
    },
}


def rng_ano(ano):
    """RNG determinista por ano: escenarios comparables contra el mismo ruido."""
    return np.random.default_rng(SEED * 100 + ano)


def horas_del_ano():
    h = np.arange(H)
    mes = np.minimum(h // 730, 11)
    return h, mes


# ----------------------------------------------------------------------------
# M1 · Series horarias
# ----------------------------------------------------------------------------

def serie_demanda(ano, rng=None):
    rng = rng or rng_ano(ano)
    h, mes = horas_del_ano()
    diario = 1 + 0.17 * np.cos(2 * np.pi * (h % 24 - 20) / 24)     # valle 04, punta 20
    estac = np.where((mes >= 4) & (mes <= 7), 1.065,
            np.where(mes <= 2, 1.015, 0.955))
    dow = (h // 24) % 7
    semanal = np.where(dow >= 5, 0.92, 1.0)
    ruido = np.clip(rng.standard_t(3, H) * 0.022, -0.07, 0.10)      # colas pesadas
    return DEMANDA_MEDIA[ano] * diario * estac * semanal * (1 + ruido)


def serie_solar(ano, rng=None):
    rng = rng or rng_ano(ano)
    h, mes = horas_del_ano()
    hh = h % 24
    ancho = np.where((mes <= 2) | (mes == 11), 2.75, 2.05)          # dia mas largo en verano
    amp = np.where((mes <= 2) | (mes == 11), 1.12, 0.82)
    campana = np.exp(-((hh - 13.2) / ancho) ** 2)
    nubes = np.clip(1 + rng.normal(0, 0.05, H), 0.75, 1.15)         # Atacama: cielo casi limpio
    return SOLAR_CAP[ano] * 1000 * campana * amp * nubes


def serie_eolica(ano, rng=None):
    rng = rng or rng_ano(ano)
    h, _ = horas_del_ano()
    eps = rng.normal(0, 0.16, H)
    ar = np.zeros(H)
    ar[0] = eps[0]
    for i in range(1, H):
        ar[i] = 0.93 * ar[i - 1] + eps[i]
    diurno = 0.10 * np.sin(2 * np.pi * (h % 24 + 3) / 24)
    cf = np.clip(0.30 + ar + diurno, 0.03, 0.82)
    return EOLICA_CAP[ano] * 1000 * cf


def hidro_disponible(ano, rng=None):
    rng = rng or rng_ano(ano)
    _, mes = horas_del_ano()
    f = HIDRO_FACTOR[ano]
    estac = np.where((mes >= 3) & (mes <= 5), 0.92, 1.0)
    pasada = 3400 * 0.52 * f * estac * np.clip(1 + rng.normal(0, 0.06, H), 0.8, 1.2)
    embalse = 3200 * min(1.0, 0.58 * f) * estac
    return pasada, embalse


# ----------------------------------------------------------------------------
# M2 + M3 · Despacho con dos zonas y limite de intercambio
# ----------------------------------------------------------------------------

def construir_stack(ano):
    """Stack TERMICO+HIDRO (sin ERV: la demanda neta ya las descuenta).

    Devuelve (cvs, cum): capacidades acumuladas para searchsorted.
    """
    pasada, embalse = hidro_disponible(ano)
    cv_gnl = CV_BASE["gnl"] * GNL_F[ano]
    segmentos = [
        (CV_BASE["hidro_pasada"], pasada.mean()),
        (CV_BASE["hidro_embalse"], embalse.mean()),
        (CV_BASE["biomasa"], 300),
        (CV_BASE["carbon"], CARBON_CAP[ano] * 1000 * DISP["carbon"]),
        (cv_gnl, GNL_CAP[ano] * 1000 * DISP["gnl"]),
        (CV_BASE["diesel"], 1600 * DISP["diesel"]),
    ]
    caps = np.array([s[1] for s in segmentos])
    cvs = np.array([s[0] for s in segmentos])
    return cvs, np.cumsum(caps), cv_gnl


def precio_stack(cvs, cum, demanda_neta):
    """Costo marginal horario para demanda neta (MW) contra el stack termico."""
    idx = np.searchsorted(cum, demanda_neta)
    dentro = idx < len(cvs)
    precio = np.where(dentro, cvs[np.minimum(idx, len(cvs) - 1)], COSTO_RACIONAMIENTO)
    return np.where(demanda_neta <= 0, 0.0, precio)


def despacho_ano(ano, limite_extra=0.0, con_bess=False):
    """Simula un ano horario; devuelve dict de arrays."""
    rng = rng_ano(ano)
    demanda = serie_demanda(ano, rng)
    solar = serie_solar(ano, rng)
    eolica = serie_eolica(ano, rng)
    pasada, embalse = hidro_disponible(ano, rng)
    cvs, cum, cv_gnl = construir_stack(ano)

    dem_n, dem_c = demanda * ZONA["demanda_n"], demanda * (1 - ZONA["demanda_n"])
    sol_n, sol_c = solar * ZONA["solar_n"], solar * (1 - ZONA["solar_n"])
    wnd_n, wnd_c = eolica * ZONA["eolica_n"], eolica * (1 - ZONA["eolica_n"])
    ren_n, ren_c = sol_n + wnd_n, sol_c + wnd_c
    L = LIMITE_INTERCAMBIO[ano] + limite_extra

    neto_sys = (dem_n + dem_c) - (ren_n + ren_c)
    surplus_n = np.clip(ren_n - dem_n, 0, None)
    deficit_n = np.clip(dem_n - ren_n, 0, None)                        # norte importando del centro

    congesta = (surplus_n > L) & (neto_sys > 0)
    flujo = np.where(congesta, L, surplus_n)                           # exportacion norte->centro
    curtail_n = np.where(congesta, surplus_n - L, 0.0)
    spill_sys = np.clip(-neto_sys, 0, None)                            # excedente sistemico
    curtail_n = np.maximum(curtail_n, np.minimum(surplus_n, spill_sys))
    curtail_c = np.clip(spill_sys - curtail_n, 0, None)

    # demanda neta termica del centro: su deficit - import recibida + export al norte
    centro_neto = (dem_c - ren_c) - flujo + np.minimum(deficit_n, L)
    precio_centro = precio_stack(cvs, cum, centro_neto)
    precio_norte = precio_stack(cvs, cum, neto_sys)
    # piso SSCC: con vertimiento (zonal o sistemico) el cMg no baja del minimo
    precio_centro = np.where((curtail_c > 0) | (neto_sys <= 0), PISO_VERTIMIENTO, precio_centro)
    precio_norte = np.where((curtail_n > 0) | (neto_sys <= 0), PISO_VERTIMIENTO, precio_norte)

    # M4 · BESS: arbitraje diario (carga con vertimiento, descarga 19-22 h)
    if con_bess and ano in BESS_GW:
        p_bess = BESS_GW[ano] * 1000
        eta = 0.86
        total_curt = curtail_n + curtail_c
        for d in range(H // 24):
            sl = slice(d * 24, (d + 1) * 24)
            e_carga = min(p_bess * 4, float(total_curt[sl].sum()))
            if e_carga <= 0:
                continue
            # reduccion proporcional del vertimiento del dia
            k = (total_curt[sl].sum() - e_carga) / total_curt[sl].sum()
            curtail_n[sl] *= k
            curtail_c[sl] *= k
            total_curt[sl] *= k
            # descarga en la punta (19-22): baja la demanda neta esas horas
            extra = e_carga * eta / 4
            centro_neto[d * 24 + 19:(d + 1) * 24][[0, 1, 2, 3]] -= extra
        precio_centro = np.where(curtail_c > 0, PISO_VERTIMIENTO, precio_stack(cvs, cum, centro_neto))

    return {
        "ano": ano, "demanda": demanda, "solar": solar, "eolica": eolica,
        "precio_norte": precio_norte, "precio_centro": precio_centro,
        "curtail_n": curtail_n, "curtail_c": curtail_c,
        "flujo": flujo, "congesta": congesta, "cv_gnl": cv_gnl,
    }


# ----------------------------------------------------------------------------
# M5 · Cadena tarifaria cMg -> PN -> PE (DS 88/2020)
# ----------------------------------------------------------------------------

def cadena_tarifaria(precios_por_ano):
    """PN semestral (persistencia 6m) y PE con tope de ajuste 5% trimestral."""
    filas = []
    for ano in YEARS:
        p = precios_por_ano[ano]
        for m in range(12):
            filas.append({"ano": ano, "mes": m + 1,
                          "spot": float(p[m * 730:(m + 1) * 730].mean())})
    df = pd.DataFrame(filas)
    df["pn"] = df["spot"].rolling(6, min_periods=1).mean().shift(1).fillna(df["spot"])
    pe, saldo = [], []
    pe_prev, acum = None, 0.0
    for i, r in df.iterrows():
        ma12 = df["pn"].iloc[max(0, i - 11):i + 1].mean()
        if pe_prev is None:
            pe_v = ma12
        else:
            paso = np.clip(ma12 - pe_prev, -0.05 * pe_prev, 0.05 * pe_prev)
            pe_v = pe_prev + paso
        pe.append(pe_v)
        # saldo = costo real no cobrado al cliente regulado (55% de la energia)
        e_reg_mwh = DEMANDA_MEDIA[r["ano"]] * 730 * 0.55
        acum += (r["spot"] - pe_v) * e_reg_mwh / 1e6   # MUSD acumulados
        saldo.append(acum)
        pe_prev = pe_v
    df["pe"] = pe
    df["saldo_mmusd"] = saldo
    return df


# ----------------------------------------------------------------------------
# M6 · Metricas y escenarios
# ----------------------------------------------------------------------------

def metricas_ano(res):
    pn, pc = res["precio_norte"], res["precio_centro"]
    spread = pc - pn
    pos = spread[spread > 0]
    return {
        "ano": res["ano"],
        "precio_medio": float(pc.mean()),
        "precio_norte_medio": float(pn.mean()),
        "var95": float(np.quantile(pc, 0.95)),
        "cvar95": float(pc[pc >= np.quantile(pc, 0.95)].mean()),
        "horas_precio_0": int((pc <= 1e-9).sum()),
        "horas_congestion": int((res["curtail_n"] > 1).sum()),  # horas con vertimiento norte
        "spread_medio": float(pos.mean()) if len(pos) else 0.0,
        "spread_max": float(spread.max()),
        "vertimiento_gwh": float((res["curtail_n"].sum() + res["curtail_c"].sum()) / 1e3),
    }


def perfil_medio_diario(res):
    """Curva de pato: perfil 24h promedio verano (ene-feb-dic) e invierno (jun-jul-ago)."""
    _, mes = horas_del_ano()
    out = {}
    for nombre, meses in [("verano", (0, 1, 11)), ("invierno", (5, 6, 7))]:
        mask = np.isin(mes, meses)
        suma = np.zeros(24)
        hh = np.arange(H) % 24
        for h24 in range(24):
            m = mask & (hh == h24)
            suma[h24] = res["precio_centro"][m].mean()
        out[nombre] = [round(float(x), 1) for x in suma]
    return out


def escenario_hvdc(ano=2025, extra=3000):
    """Efecto de la HVDC Kimal-Lo Aguirre (+3.000 MW) sobre el ano indicado."""
    base = despacho_ano(ano)
    con = despacho_ano(ano, limite_extra=extra)
    mb, mc = metricas_ano(base), metricas_ano(con)
    return {
        "base": mb, "con_hvdc": mc,
        "delta_spread": mc["spread_medio"] - mb["spread_medio"],
        "delta_vertimiento": mc["vertimiento_gwh"] - mb["vertimiento_gwh"],
        "delta_horas_cong": mc["horas_congestion"] - mb["horas_congestion"],
    }


def sensibilidad_gnl(ano=2022, mults=(0.8, 1.0, 1.2, 1.4)):
    """Elasticidad del precio medio al CV del GNL (ano de crisis)."""
    global GNL_F
    original = GNL_F[ano]
    out = []
    try:
        for m in mults:
            GNL_F[ano] = original * m
            res = despacho_ano(ano)
            out.append({"mult": m, "cv_gnl": float(res["cv_gnl"]),
                        "precio_medio": metricas_ano(res)["precio_medio"]})
    finally:
        GNL_F[ano] = original
    return out


# ----------------------------------------------------------------------------
# Exportacion
# ----------------------------------------------------------------------------

def ejecutar_todo():
    resultados = {}
    for ano in YEARS:
        sin_bess = despacho_ano(ano)
        con_bess = despacho_ano(ano, con_bess=True) if ano in BESS_GW else sin_bess
        resultados[ano] = {"sin_bess": sin_bess, "con_bess": con_bess,
                           "metricas": metricas_ano(con_bess),
                           "metricas_potencial": metricas_ano(sin_bess)}
    return resultados


def exportar(resultados, destino):
    dest = Path(destino)
    dest.mkdir(parents=True, exist_ok=True)

    mensual = []
    for ano in YEARS:
        r = resultados[ano]["con_bess"]
        for m in range(12):
            sl = slice(m * 730, (m + 1) * 730)
            mensual.append({
                "fecha": f"{ano}-{m + 1:02d}",
                "pnorte": round(float(r["precio_norte"][sl].mean()), 1),
                "pcentro": round(float(r["precio_centro"][sl].mean()), 1),
                "spread": round(float((r["precio_centro"][sl] - r["precio_norte"][sl]).mean()), 1),
            })
    doc = []
    for ano in YEARS:
        cq = ANCLAS["cmg_mensual"]["crucero"][ano]
        cc = ANCLAS["cmg_mensual"]["quillota"][ano]
        for m in range(12):
            doc.append({"fecha": f"{ano}-{m + 1:02d}", "crucero": cq, "quillota": cc})

    hists = []
    for ano in YEARS:
        p = resultados[ano]["con_bess"]["precio_centro"]
        counts, edges = np.histogram(p, bins=np.arange(0, 170, 8))
        hists.append({"ano": ano, "counts": counts.tolist(),
                      "edges": edges[:-1].tolist()})

    anual = []
    for ano in YEARS:
        m = resultados[ano]["metricas"]
        mp = resultados[ano]["metricas_potencial"]
        anual.append({
            **m, "vertimiento_potencial": mp["vertimiento_gwh"],
            "vertimiento_doc": ANCLAS["vertimiento_gwh"].get(ano),
            "precio_doc": ANCLAS["precio_medio_quillota"][ano],
        })

    cadena = cadena_tarifaria({a: resultados[a]["con_bess"]["precio_centro"] for a in YEARS})
    cadena_out = {
        "mes": [f"{int(r.ano)}-{int(r.mes):02d}" for r in cadena.itertuples()],
        "spot": [round(r.spot, 1) for r in cadena.itertuples()],
        "pn": [round(r.pn, 1) for r in cadena.itertuples()],
        "pe": [round(r.pe, 1) for r in cadena.itertuples()],
        "saldo": [round(r.saldo_mmusd, 1) for r in cadena.itertuples()],
    }

    hvdc = escenario_hvdc()
    sens = sensibilidad_gnl()
    pato = {str(a): perfil_medio_diario(resultados[a]["con_bess"]) for a in (2022, 2025)}

    data = {
        "generado": "src/pipeline.py · seed 2026 · datos sinteticos calibrados",
        "mensual": mensual, "documentado": doc, "hist": hists, "anual": anual,
        "cadena": cadena_out, "hvdc": hvdc, "sens_gnl": sens, "pato": pato,
        "anclas": {"precio_medio": {str(k): v for k, v in ANCLAS["precio_medio_quillota"].items()},
                   "vertimiento": {str(k): v for k, v in ANCLAS["vertimiento_gwh"].items()},
                   "spread_medio": ANCLAS["spread_medio"], "spread_max": ANCLAS["spread_max"],
                   "vertimiento_potencial_2025": ANCLAS["vertimiento_potencial_2025"]},
    }

    (dest / "data.js").write_text(
        "window.SENSPOT = " + json.dumps(data, ensure_ascii=False, default=float) + ";",
        encoding="utf-8")

    pd.DataFrame(anual).to_csv(dest / "tabla_metricas.csv", index=False)
    print(f"exportado: {dest/'data.js'} y {dest/'tabla_metricas.csv'}")
    return data


if __name__ == "__main__":
    res = ejecutar_todo()
    data = exportar(res, ROOT / "dashboard" / "js")
    print("\n=== Calibracion (modelo vs documentado) ===")
    print(f"{'ano':>4} {'p.modelo':>9} {'p.doc':>6} {'vert.mod':>9} {'vert.pot':>9} {'vert.doc':>8} {'h.cong':>7} {'spread':>7} {'V95':>6}")
    for a in data["anual"]:
        print(f"{a['ano']:>4} {a['precio_medio']:>9.1f} {a['precio_doc']:>6} "
              f"{a['vertimiento_gwh']:>9.0f} {a['vertimiento_potencial']:>9.0f} {str(a['vertimiento_doc']):>8} "
              f"{a['horas_congestion']:>7} {a['spread_medio']:>7.1f} {a['var95']:>6.0f}")
    print("\nHVDC:", {k: round(v, 1) if isinstance(v, float) else v
                      for k, v in data["hvdc"].items() if k.startswith("delta")})
    print("Sens GNL:", [(s["mult"], round(s["precio_medio"], 1)) for s in data["sens_gnl"]])
