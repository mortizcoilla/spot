# SEN ▸ SPOT — Pricing dinámico del mercado spot eléctrico chileno

Guía de campo interactiva (dashboard D3.js v7) sobre el mercado spot del Sistema
Eléctrico Nacional de Chile: orden de mérito, costo marginal 2020–2025, desacople
norte-centro, vertimiento renovable, apagón del 25-feb-2025 y comparativa
internacional.

Diseño editorial "papel milimetrado": fondo crema con retícula, tarjetas con
esquinas técnicas, tipografías Space Grotesk / Newsreader / JetBrains Mono,
paleta de tinta navy con acentos naranja (solar/demanda), azul (hidro/norte) y
rojo (diésel/crisis).

## Contenido

| Archivo | Descripción |
|---|---|
| `index.html` | **Dashboard interactivo** (8 secciones, 7+ visualizaciones D3) |
| `informe.html` | Versión informe anterior (tema oscuro, archivo) |
| `estudio-academico-pricing-dinamico-sen-chile.md` | Estudio académico de 10 partes (fuentes, glosario, autoevaluación) |
| `cd540654-…pdf` | Documento fuente original (PDF) |
| `AUDITORIA.md` | Auditoría técnica del dashboard: errores encontrados y corregidos |

## Secciones del dashboard

- **§ 00 · Orden de mérito** — arrastra la demanda (o simula un ciclo diario) y
  observa cómo el costo marginal salta de escalón; incluye vertimiento implícito
  cuando la demanda no alcanza a ocupar la renovable y costo de racionamiento
  (650,6 USD/MWh, CNE jun-2025) sobre el techo simulado de 9.000 MW.
- **§ 01 · Costo marginal 2020–2025** — serie por barra troncal (Crucero,
  Quillota, Alto Jahuel, Charrúa) con zoom (rueda), paneo (arrastre) y
  crosshair; curva de pato verano/invierno; cadena de precios cMg → spot →
  PN → PE → tarifa.
- **§ 02 · Desacople norte-centro** — Crucero vs Quillota con spread de
  congestión por mes; contexto HVDC Kimal–Lo Aguirre.
- **§ 03 · Vertimiento** — dona regional y escalera anual 2022–2025 con
  contrafactual sin BESS (6.205 GWh vertidos en 2025; 8.200 GWh potenciales).
- **§ 04 · Apagón 25-feb-2025** — cronología de 8 pasos (teclado ←/→/N/P) sobre
  esquema topológico animado del SEN.
- **§ 05 · Comparativa internacional** — precio spot medio 2024 y vertimiento
  ERV vs Alemania, España, China, PJM, ERCOT.
- **§ 06 · Claves** — seis síntesis para leer el spot.
- **§ 07 · Apéndice** — tabla de costo marginal, indicadores estructurales y 24
  referencias.

## Uso local

100% estático, sin build. Servir por HTTP (D3 por CDN):

```bash
python -m http.server 8000
# abrir http://localhost:8000
```

## Despliegue (Vercel)

El `vercel.json` raíz ya define clean URLs y cabeceras de seguridad. Desde la
raíz del repo:

```bash
npx vercel --prod
```

o importar el repositorio en vercel.com con Framework Preset **Other** (sin
build command, sin output directory).

## Datos y fuentes

Series y cifras: CEN (Costo Marginal Real, Reporte Energético SEN), CNE
(fijaciones de precio de nudo, licitación 2023/01, costo de racionamiento),
Ministerio de Energía (RME), Ember, ACERA, Broker & Trader Energy, Systep.
Los promedios usan los meses reportados (ene/abr/jul/oct) y el perfil horario
de la curva de pato es sintético calibrado; las limitaciones están documentadas
en el propio dashboard y en el estudio académico.

## Autor

Miguel Ortiz Coilla · 2026
