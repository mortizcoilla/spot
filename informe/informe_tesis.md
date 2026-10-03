# Pricing dinámico del mercado spot eléctrico chileno: un modelo estructural de dos zonas del Sistema Eléctrico Nacional (2020–2025)

**Informe de investigación · versión 1.0 · octubre 2026**
Miguel Ortiz Coilla

---

## Resumen

El mercado spot chileno no es una subasta: es un despacho centralizado valorizado
ex-post al costo marginal. Esta investigación construye un **modelo estructural
horario de dos zonas** (norte exportador / centro importador) del Sistema
Eléctrico Nacional (SEN) para el período 2020–2025, sobre datos sintéticos
reproducibles calibrados a las magnitudes documentadas por el Coordinador
Eléctrico Nacional (CEN), la Comisión Nacional de Energía (CNE), Ember y Broker
& Trader (B&T). El modelo reproduce, sin asumirlos, tres fenómenos centrales
del pricing dinámico chileno: (i) la **formación escalonada del costo marginal**
por orden de mérito y su choque durante la crisis 2022–23 (precio medio simulado
2022: 104,9 vs 104 USD/MWh documentado, error +0,8%); (ii) el **desacople de
precios norte-centro** que emerge endógenamente cuando el excedente solar
supera el límite de interconexión (spread medio 5–15 USD/MWh en condiciones
normales, consistente con lo documentado); y (iii) la **migración del
vertimiento** desde un mecanismo de congestión zonal hacia un excedente
sistémico de mediodía, parcialmente mitigado por baterías (BESS). La cadena
tarifaria simulada (precio de nudo semestral → precio estabilizado con tope de
ajuste ±5%) amortigua la volatilidad del spot ×5 y acumula un saldo de
estabilización pico del orden del documentado (~1.700 vs >2.000 M USD).
El escenario HVDC Kimal–Lo Aguirre (+3.000 MW) reduce el spread medio 7,9
USD/MWh y el vertimiento 541 GWh, pero no elimina el excediente estructural de
mediodía. Se auditan y corrigen las cifras del estudio académico de origen.

**Palabras clave:** mercado spot eléctrico, costo marginal, orden de mérito,
congestión nodal, vertimiento (curtailment), BESS, precio de nudo, precio
estabilizado, SEN, Chile.

---

## Abstract

The Chilean spot market is not an auction but a centralized dispatch valued
ex-post at marginal cost. This research builds an **hourly two-zone structural
model** (exporting north / importing center) of Chile's National Electric System
for 2020–2025, on reproducible synthetic data calibrated to documented
magnitudes (CEN, CNE, Ember, B&T). Without assuming them, the model reproduces
the stepped formation of marginal cost — including the 2022–23 fuel-hydrology
shock (simulated 2022 mean price: 104.9 vs 104 USD/MWh documented, +0.8% error)
—, the endogenous north-center price decoupling when solar surplus exceeds the
interconnection limit, and the migration of curtailment from zonal congestion
to a system-wide midday surplus partially absorbed by batteries. The simulated
regulated chain (semi-annual nodal price → 5%-capped stabilized price) dampens
spot volatility ×5 and accumulates a stabilization balance of the documented
order of magnitude. The Kimal–Lo Aguirre HVDC scenario (+3,000 MW) cuts the
average spread by 7.9 USD/MWh but does not eliminate the structural midday
surplus.

---

## 1. Introducción

### 1.1 Motivación

El pricing dinámico del mercado spot eléctrico chileno concentra tres
fricciones que la literatura regulatoria nacional discute de forma separada:
la congestión de la troncal norte-centro, el vertimiento de energía renovable
variable (ERV) y la transición de la volatilidad del mercado mayorista hacia
la tarifa regulada. El estudio académico de origen (10 partes, 2026) documenta
estos fenómenos con fuentes primarias, pero no los integra en un modelo
cuantitativo que permita **contrafactuales limpios**: ¿qué habría pasado sin
baterías?, ¿qué pasará con la línea HVDC Kimal–Lo Aguirre?

### 1.2 Preguntas de investigación

- **RQ1.** ¿La formación del precio spot puede reproducirse con un modelo
  estructural de orden de mérito simple, calibrado solo con magnitudes
  documentadas?
- **RQ2.** ¿El desacople norte-centro emerge de la geografía de la generación
  y del límite de interconexión, sin supuesto ad hoc?
- **RQ3.** ¿Cuándo el vertimiento deja de ser congestión zonal y pasa a ser
  excedente sistémico, y cuál es el rol marginal de las BESS?
- **RQ4.** ¿Cuánta volatilidad absorbe la cadena tarifaria regulada
  (PN → PE) y de qué orden es el saldo fiscal que acumula?
- **RQ5.** ¿Cuán elástico es el precio spot al costo del GNL importado y qué
  efecto estructural tiene la HVDC proyectada?

### 1.3 Contribuciones

1. Un modelo estructural horario de dos zonas, open source y reproducible
   (semilla fija), que aisla mecanismos (crisis de combustible, congestión,
   BESS, HVDC) sobre el mismo ruido base.
2. Una **auditoría crítica** del estudio de origen: corrección de
   inconsistencias numéricas y de una contradicción conceptual
   (§contratación vs spot; Anexo A).
3. Tres artefactos integrados: notebook ejecutado, dashboard D3 interactivo
   e informe.

### 1.4 Alcance y limitaciones de partida

Los datos son **sintéticos calibrados**: reproducen magnitudes y patrones
documentados, no series reales. El objetivo es explicación estructural y
análisis contrafactual, no forecasting (para pronóstico del CMG ver el
proyecto *CMG Forecast Study*). El modelo no incluye: red eléctrica detallada
(solo 2 zonas), pérdidas, arranques/paradas unitarios, reserva rotante,
restricciones de tensión, ni comportamiento estratégico de oferentes.

---

## 2. Marco institucional y regulatorio (auditoría del estudio de origen)

El SEN se despacha centralizadamente por el CEN (Ley 20.936 de 2016) y las
transferencias entre generadores se liquidan ex-post al **costo marginal**
(cMg) por barra y hora. La cadena de precios relevante es:

> cMg (operativo) → spot (transferencias ex-post) → precio de nudo, PN
> (proyección semestral CNE) → precio estabilizado, PE (DS 88/2020, Ley
> 21.185, tope de ajuste 5% trimestral, vigente a diciembre 2027) → tarifa.

Puntos clave verificados y auditados del estudio de origen:

| Afirmación del estudio | Veredicto de auditoría |
|---|---|
| ">70% de la energía se transa mediante contratos de largo plazo" (Parte I) | **Correcto** y consistente con Parte VIII; la *guía de campo* derivada contenía la contradicción "70% se transa en el spot" — corregida en la versión actual del dashboard |
| Vertimiento 2022–2025: 1.810 / 2.376 / 5.909 / 6.205 GWh (Ember, B&T, CEN) | Consistente entre secciones; **el delta "2025: −0,3% vs 2024" es incorrecto**: 6.205/5.909 = **+5,0%** (el +133% vs 2023 también es +161%); corregido en los artefactos de este proyecto |
| Spread Crucero–Quillota "5–15 USD/MWh normal, >50 en congestión severa" | Consistente con las series de la guía (máximo reportado +48 en abr-2025); adoptado como ancla |
| "Saldo de estabilización superó USD 2.000 M" (§2.3) vs "más de USD 2.500 M en 2023" (§4.3) | Doble estándar interno; se adopta ">2.000 M USD (2023)" como ancla conservadora y se documenta la discrepancia |
| "Más de 6.000 PMGD" (§4.5) | **Plausible pero impreciso**: la cifra agrega probablemente instalaciones netbilling; la PMGD estricta (<9 MW) es del orden de 1–3 mil unidades. El efecto relevante (capacidad solar PMGD ~2–3 GW al 2025) sí está capturado en el modelo |
| CV por tecnología (Parte III.1) | Razonables; adoptados como base del stack con disponibilidad efectiva |
| Embalses "Pangue, Ralco, Pangue" (§3.4) | Duplicado tipográfico; corregido en referencias internas |

La auditoría completa, incluidos los bugs de la guía interactiva (crosshair
inoperante, excepción en el gráfico de desacople), está en `AUDITORIA.md`.

---

## 3. Datos y calibración

### 3.1 Filosofía

Cada parámetro del modelo se ancla a una magnitud documentada; donde hay
incertidumbre se declara. La calibración se valida **por año** contra anclas
independientes de las usadas para ajustar (precio medio documentado de la barra
Quillota; vertimiento anual; spread medio).

### 3.2 Anclas y parámetros principales

| Parámetro | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | Fuente/justificación |
|---|---|---|---|---|---|---|---|
| Demanda media (MW) | 7.300 | 7.550 | 7.750 | 7.850 | 8.150 | 8.350 | CEN, balances anuales |
| Solar utility+PMGD (GW) | 3,2 | 4,2 | 6,0 | 8,6 | 12,2 | 15,0 | CEN/ACERA; incluye PMGD (mayoritariamente norte) |
| Eólica (GW) | 1,7 | 1,9 | 2,3 | 2,7 | 3,2 | 3,7 | CEN/ACERA |
| Factor hidrológico | 1,00 | 0,78 | 0,68 | 0,72 | 1,08 | 0,96 | Megasequía 2021-23; año húmedo 2024 (estudio, Parte V) |
| Multiplicador CV GNL | 1,30 | 1,85 | 2,95 | 2,60 | 1,30 | 1,25 | Henry Hub 8,79 USD/MMBtu ago-2022 (crisis Ucrania) |
| Carbón (GW, disp. 52%) | 4,6 | 4,3 | 3,8 | 3,3 | 2,7 | 2,2 | Retiros programados |
| Límite intercambio N-C (MW) | 1.350 | 1.400 | 1.400 | 1.600 | 1.750 | 1.750 | Estudio §3.5/§6.1 (1.500–2.500 nominal) |
| BESS (GW) | — | — | — | — | 1,1 | 1,6 | B&T; arbitraje 4 h, η 0,86 |

El **piso de vertimiento** (8 USD/MWh) representa los componentes SSCC y
costos de arranque que mantienen el cMg positivo aun con excedente (estudio,
Parte III.3). Las series horarias usan ruido $t(3)$ (demanda, colas pesadas),
campana solar estacional (Atacama) y AR(1) eólico. Cada año tiene semilla
propia: los escenarios (BESS, HVDC, GNL) se comparan contra el **mismo ruido
base**.

### 3.3 Resultado de la calibración (RQ1)

| Año | Precio modelo | Precio doc. (Quillota) | Error | Vert. modelo | Vert. doc. | VaR95 mod. |
|---|---|---|---|---|---|---|
| 2020 | 40,7 | 52 | −22% | 36 | — | 57 |
| 2021 | 64,8 | 72 | −10% | 271 | — | 81 |
| 2022 | **104,9** | **104** | **+0,8%** | 1.063 | 1.810 | 130 |
| 2023 | 88,1 | 107 | −18% | 2.040 | 2.376 | 114 |
| 2024 | 39,7 | 61 | −35% | 2.587 | 5.909 | 57 |
| 2025 | 39,9 | 75 | −47% | 5.018 | 6.205 | 55 |

**Lectura honesta.** El modelo reproduce el patrón (auge 2021-23, normalización
2024, repunte 2025) y calza casi exacto en el año de crisis (2022, +0,8%).
El sesgo negativo creciente post-2024 se explica por tres omisiones
declaradas: primas SSCC en horas de estrés, restricciones locales de red
menores, y la omisión de contratos de GNL caro heredados en 2024-25. En
vertimiento captura el orden de magnitud y el patrón ×5 de crecimiento, con
subestimación del nivel (la PMGD real y la congestión fina exceden lo
modelable con una zona por región de despacho).

---

## 4. Metodología: modelo estructural de dos zonas

### 4.1 M1 · Series horarias

Demanda horaria $D_t$ = media anual × ciclo diario (valle 04:00, punta 20:00)
× estacionalidad (invierno +6,5%) × factor semanal × ruido $t(3)$ acotado.
Solar $S_t$ = capacidad × campana gaussiana centrada 13:20 h con ancho y
amplitud estacionales × ruido de nubes. Eólica $W_t$ = AR(1) horario
($\phi=0,93$) + componente diurno. Hidrología anual (pasada y embalse) por
factor documentado.

### 4.2 M2 · Despacho por orden de mérito

La ERV se descuenta de la demanda (demanda neta $ND_t = D_t - S_t - W_t$,
estudio §4.5) y el stack **térmico-hidro** despacha por costo variable:

$$cMg_t = cv^{(k)} \quad \text{tal que} \quad \mathrm{CumCap}^{(k-1)} < ND_t \le \mathrm{CumCap}^{(k)}$$

con costo de racionamiento 650,6 USD/MWh (CNE jun-2025) como techo si
$ND_t$ excede la capacidad, y piso 8 USD/MWh con excedente. La disponibilidad
efectiva por tecnología (52–90%) captura outages y mínimos técnicos. **Error
evitado explícitamente:** incluir la ERV en el stack *y* descontarla de la
demanda duplica la renovable y hunde el precio a cero (bug detectado y
corregido en la primera iteración; ver `AUDITORIA.md`).

### 4.3 M3 · Dos zonas y congestión

El norte concentra 72% de la solar y 18% de la demanda. Con déficits zonales
$\delta^N_t, \delta^C_t$ y límite de interconseción $L_t$ (flujo
bidireccional):

- Si el excedente norte $-\delta^N_t > L_t$: **congestión** — vertimiento
  zonal $V^N_t = -\delta^N_t - L_t$, precio norte = piso, y el centro despacha
  su stack con $L_t$ importado: $cMg^C_t = f(\delta^C_t - L_t)$.
- Si el déficit norte $\delta^N_t > L_t$ (raro): congestión inversa, precio
  norte > centro (49 h/año en el modelo; ≤4,3 USD/MWh de efecto mensual).
- Si el excedente es sistémico ($ND_t < 0$): vertimiento en ambas zonas,
  precio = piso.

El spread $cMg^C_t - cMg^N_t$ **no es un supuesto**: emerge del desbalance
geográfico y de $L_t$.

### 4.4 M4 · BESS

Arbitraje diario: carga hasta `min(4h × potencia, vertimiento del día)` con
η = 0,86 y descarga uniforme en la punta 19–22 h. El contrafactual sin BESS
reproduce el marco B&T (potencial 8.200 GWh en 2025).

### 4.5 M5 · Cadena tarifaria

PN mensual (proxy semestral) = promedio móvil de 6 meses del cMg con rezago.
PE: ajuste trimestral hacia la media móvil de 12 meses del PN, con tope ±5%
(DS 88/2020). Saldo de estabilización =
$\sum_t (cMg_t - PE_t) \times E^{reg}_t$, con 55% de la energía regulada.

### 4.6 M6 · Riesgo y escenarios

VaR95/CVaR95 del cMg horario por año; escenario HVDC (+3.000 MW sobre
$L_{2025}$); sensibilidad al CV del GNL (×0,8–1,4 sobre 2022).

---

## 5. Resultados

### 5.1 RQ1 · Formación del precio

La distribución horaria del cMg es **bimodal**: una masa en el piso
(mediodía solar) y otra en la térmica marginal (noche), con la cola derecha
creciendo en la crisis (CVaR95 2022 = 143 USD/MWh). El precio medio anual
reproduce el patrón documentado (§3.3): la crisis 2022–23 es, en el modelo,
un choque de CV del GNL (×2,95) sobre hidrología seca (0,68) — la elasticidad
resultante es ≈ 0,9: **+18 USD/MWh de precio medio por cada +20% del costo
del gas**. La sequía amplificó; el gas causó.

### 5.2 RQ2 · Desacople norte-centro

El spread medio en horas de congestión cae dentro del rango documentado
(5–15 USD/MWh normal; 15,2 en la crisis). Las horas de vertimiento norte
crecen de 163 (2020) a 1.943 (2025). Con la HVDC (+3.000 MW): spread medio
−7,9 USD/MWh, vertimiento −541 GWh (−11%), horas de congestión −563. **La
línea mitiga pero no resuelve**: el excedente de mediodía es sistémico.

### 5.3 RQ3 · Vertimiento y BESS

El mecanismo dominante migra: en 2022–23 el vertimiento del modelo es ~100%
zonal (sol norte atascado tras $L_t$); desde 2024 más de la mitad es
excedente sistémico de mediodía. Sin BESS, 2025 alcanzaría 7.352 GWh
potenciales (B&T: 8.200); con 1,6 GW de baterías el modelo entrega 5.018 GWh
(B&T: 6.205) — las baterías evitan ~2.300 GWh (B&T: ~2.000), un 31% del
potencial. La curva de pato 2025 vs 2022 muestra el aplanamiento del valle y
el recorte de punta que constituye el ingreso de arbitraje BESS.

### 5.4 RQ4 · Cadena tarifaria

Volatilidad mensual del spot 18,4% vs 3,5% del PE → **amortiguación ×5,3**.
El saldo de estabilización simulado pica en ~1.700 M USD durante la crisis
(documentado: >2.000 M USD en 2023), mismo orden de magnitud. El mecanismo,
no la cifra exacta, es el hallazgo: **la estabilidad tarifaria traslada la
volatilidad al balance fiscal**, con vencimiento regulatorio en diciembre de
2027 (fin de la vigencia del esquema DS 88/2020).

### 5.5 RQ5 · Escenarios

| Escenario | Efecto sobre 2022/2025 |
|---|---|
| CV GNL ×1,4 (2022) | Precio medio 143,5 USD/MWh (+37%) |
| CV GNL ×0,8 (2022) | Precio medio 85,6 USD/MWh (−18%) |
| HVDC +3.000 MW (2025) | Spread −7,9; vertimiento −541 GWh; congestión −563 h |

---

## 6. Discusión

**Sobre la crisis 2022–23.** El modelo la reproduce con dos insumos
documentados (Henry Hub, megasequía) y ningún ajuste libre: la dependencia del
GNL importado es la variable dominante del pricing spot chileno, y la
hidrología su amplificador. Esto es consistente con el análisis de ACERA
("implosión del mercado eléctrico 2022") citado por el estudio.

**Sobre el vertimiento.** Que el mecanismo migre de congestión zonal a
excedente sistémico tiene consecuencia regulatoria directa: más transmisión
(HVDC) resuelve lo primero pero no lo segundo; lo segundo exige demanda
absorbente (electrólisis/H2V, electrificación minera y transporte) o
almacenamiento de larga duración. La discusión pública suele confundir ambos
mecanismos; el modelo los separa.

**Sobre la estabilización tarifaria.** La amortiguación ×5 que observa el
cliente regulado es exactamente la deuda que acumula el fisco. El trade-off
señales-de-precio vs estabilidad (estudio, Parte IX.7) no es retórico: el
modelo lo cuantifica.

**Limitaciones.** (1) Dos zonas, no red: el spread es una cota inferior del
mosaico real de barras. (2) Sin unit commitment: mínimos técnicos y arranques
encarecerían las horas de estrés (parte del sesgo post-2024). (3) La PMGD se
modela como capacidad, no como esquema de incentives (el estudio §4.6
documenta la distorsión). (4) El PN real incorpora proyección de combustibles
y potencia, no solo persistencia del cMg. (5) 49 h/año de congestión inversa
(≤4,3 USD/MWh) son un artefacto aceptado del modelado de flujo capado.

---

## 7. Conclusiones

1. **RQ1 ✓** Un modelo estructural simple y calibrado reproduce la formación
   del precio spot chileno con error +0,8% en el año crítico y patrón correcto
   en todo el período; el residuo es explicable y declarado.
2. **RQ2 ✓** El desacople emerge de geografía + límite de interconexión; el
   spread simulado cae dentro del rango documentado.
3. **RQ3 ✓** El vertimiento migra de zonal a sistémico entre 2023 y 2024; las
   BESS evitan ~30% del potencial 2025 (orden del 24% documentado por B&T).
4. **RQ4 ✓** La cadena PN→PE amortigua ×5 y acumula saldo del orden
   documentado; la estabilidad tiene acreedor.
5. **RQ5 ✓** Elasticidad del precio al CV del GNL ≈ 0,9; la HVDC mitiga
   congestion y spread pero no el excedente de mediodía.

**Trabajo futuro:** (a) validación con CMG real de Energía Abierta (el
proyecto *CMG Forecast* ya tiene la ingesta); (b) unit commitment simplificado
con mínimos técnicos; (c) mosaico multi-barra con PTDF; (d) endogeneizar
inversión en BESS con el spread simulado como señal; (e) extensión del PE con
el esquema de recupero fiscal post-2027.

---

## Referencias

1. CEN, *Costo Marginal Real* y *Reporte Energético SEN* (mensual, 2022–2025).
2. CNE, *Fijaciones de Precio de Nudo 2025* y *Reporte Energético Financiero* vol. 33 (jul-2025).
3. CNE, *Licitación 2023/01* — 56,679 USD/MWh, Enel Generación, 3.600 GWh/año (2027-28).
4. Ministerio de Energía, *Reporte de Mercados Eléctricos* (oct-2022, nov-2023).
5. CEN, *Estudio de Análisis de Falla — apagón 25-feb-2025* (a SEC, 19-mar-2025).
6. Ember, *Reducing curtailment in Chile* (oct-2025): 11.900 GWh y USD 562 M (2022–may-2025).
7. Broker & Trader Energy Chile, *Reporte de Vertimiento* (ene-2026): 6.205 GWh 2025; potencial 8.200 sin BESS; BESS 2 TWh.
8. ACENOR, *Petróleo en el Sistema Interconectado de Chile* (feb-2022).
9. Stoft, S., *Power System Economics* (IEEE/Wiley, 2002).
10. Kirschen & Strbac, *Fundamentals of Power System Economics* (Wiley, 2004).
11. Ley 21.185 (2019), DS 88/2020, Ley 20.936 (2016), Ley 21.505 (2022), RE N°58/2024 y N°13/2025.

---

## Anexo A · Auditoría del estudio académico de origen

| # | Ubicación | Hallazgo | Acción |
|---|---|---|---|
| A1 | Parte VI.2 | "2025: 6.205 GWh (−0,3% vs 2024)": la cuenta es **+5,0%** (y +161% vs 2023, no +133%) | Corregido en los artefactos de este proyecto |
| A2 | Parte III.4 | "Pangue, Ralco, Pangue" duplicado | Corregido en referencias internas |
| A3 | §2.3 vs §4.3 | Saldo de estabilización "USD 2.000 M" vs "USD 2.500 M" | Ancla conservadora ">2.000 M (2023)"; discrepancia documentada |
| A4 | §4.5 | "más de 6.000 PMGD" probablemente agrega netbilling | Revisado; solo la capacidad (~2–3 GW) entra al modelo |
| A5 | Guía de campo §06 | Contradicción "70% se transa en el spot" vs estudio ">70% contratado" | Corregida en el dashboard de la guía |
| A6 | Guía de campo §01/§02 | Crosshair inoperante y TypeError en pointermove (bisector) | Corregidos (ver `AUDITORIA.md`) |
| A7 | Modelo v1 | Doble conteo de ERV (stack + demanda neta) hundía el precio a ~0 | Corregido: stack térmico-hidro puro |
| A8 | Modelo v1 | Flujo de interconexión unidireccional invertía norte/centro | Corregido: flujo bidireccional con importación capada |

## Anexo B · Artefactos y reproducibilidad

| Artefacto | Ruta | Contenido |
|---|---|---|
| Modelos (fuente única) | `src/pipeline.py` | M1–M6, seed 2026, RNG por año |
| Notebook fuente | `notebook/pricing_dinamico_sen.ipynb` | Generado por `src/build_notebook.py` |
| Notebook ejecutado | `notebook/pricing_dinamico_sen_ejecutado.ipynb` | 7 figuras, ejecución completa sin errores |
| Figuras | `notebook/results/*.png` | series, stack, zonas, BESS, cadena, riesgo, escenarios |
| Dashboard | `dashboard/index.html` + `js/data.js` | 9 visualizaciones D3 interactivas |
| Métricas | `dashboard/js/tabla_metricas.csv` | Calibración anual modelo vs documentado |
| Guía de campo | `index.html` | Dashboard divulgativo del mercado spot |

Reproducir: `python src/pipeline.py && python src/build_notebook.py`.
Servir dashboard: `python -m http.server` y abrir `/dashboard/`.
