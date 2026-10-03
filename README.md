# SEN ▸ SPOT — Pricing dinámico del mercado spot eléctrico chileno

Investigación reproducible + guía de campo interactiva sobre el mercado spot
del Sistema Eléctrico Nacional de Chile (2020–2026): orden de mérito, costo
marginal, desacople norte-centro, vertimiento renovable, BESS, cadena
tarifaria PN/PE, apagón 25-feb-2025 y comparativa internacional.

Diseño editorial "papel milimetrado": fondo crema con retícula, tarjetas con
esquinas técnicas, tipografías Space Grotesk / Newsreader / JetBrains Mono,
paleta de tinta navy con acentos naranja (solar/demanda), azul (hidro/norte) y
rojo (diésel/crisis).

## Contenido

| Ruta | Descripción |
|---|---|
| `index.html` | **Guía de campo interactiva** (8 secciones, 7+ visualizaciones D3) |
| `dashboard/` | **Dashboard de investigación**: resultados del modelo estructural (9 visualizaciones D3) |
| `informe/informe_tesis.md` | **Informe tipo tesis** con marco regulatorio, metodología, resultados y auditoría |
| `notebook/` | Notebook ejecutable + ejecutado con los modelos M1–M6 y 7 figuras |
| `src/pipeline.py` | Fuente única de los modelos (despacho, 2 zonas, BESS, cadena PN/PE, riesgo) |
| `src/build_notebook.py` | Genera y ejecuta el notebook |
| `estudio-academico-pricing-dinamico-sen-chile.md` | Estudio académico de 10 partes (auditado; ver AUDITORIA.md) |
| `AUDITORIA.md` | Auditoría técnica completa (guía + estudio + modelo) |
| `informe.html` | Versión informe anterior (tema oscuro, archivo) |

## El modelo en una línea

Demanda y ERV sintéticas horarias (no gaussianas, semilla 2026) → orden de
mérito térmico-hidro → **dos zonas con límite de interconexión** (norte
exportador / centro importador) → spread de congestión y vertimiento
endógenos → BESS (arbitraje 4 h) → cadena tarifaria PN→PE (DS 88/2020) →
VaR/CVaR y escenarios (HVDC Kimal–Lo Aguirre, CV del GNL). Calibrado contra
anclas CEN/CNE/Ember/B&T: la crisis 2022 queda a **+0,8%** del precio medio
documentado.

## Reproducir

```bash
python src/pipeline.py        # modelos + dashboard/js/data.js + tabla_metricas.csv
python src/build_notebook.py  # notebook ejecutado con 7 figuras
python -m http.server 8000    # guía en / · investigación en /dashboard/
```

## Despliegue (Vercel)

`vercel.json` raíz ya define clean URLs y cabeceras. `npx vercel --prod`
desde la raíz, o importar el repo con Framework Preset **Other**. La guía
queda en `/` y la investigación en `/dashboard/`.

## Datos y fuentes

Series y cifras: CEN (Costo Marginal Real, Reporte Energético SEN), CNE
(fijaciones de precio de nudo, licitación 2023/01, costo de racionamiento
650,6 USD/MWh), Ministerio de Energía (RME), Ember (vertimiento), ACERA,
Broker & Trader, Systep. Los promedios usan meses reportados (ene/abr/jul/oct)
y los perfiles horarios son sintéticos calibrados; las limitaciones están
documentadas en el dashboard y en `informe/informe_tesis.md` §6.

## Autor

Miguel Ortiz Coilla · 2026
