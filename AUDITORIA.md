# Auditoría técnica — SEN ▸ SPOT

Auditoría de código y de dominio (mercado eléctrico chileno). Parte 1: la guía
de campo interactiva (`index.html`). Parte 2: la investigación reproducible
(modelo estructural, notebook, dashboard de resultados, informe).

## Parte 2 · Investigación (v2, oct-2026)

### Errores del estudio académico de origen (corregidos en los artefactos)

- **E1 · Aritmética del vertimiento.** "2025: 6.205 GWh (−0,3% vs 2024)" es
  incorrecto: 6.205/5.909 = **+5,0%** (y vs 2023 es +161%, no +133%).
- **E2 · Duplicado tipográfico.** "embalses… Pangue, Ralco, Pangue" (§3.4).
- **E3 · Doble estándar del saldo de estabilización.** "USD 2.000 M" (§2.3)
  vs "USD 2.500 M" (§4.3). Se adopta ">2.000 M (2023)" como ancla.
- **E4 · "Más de 6.000 PMGD"** (§4.5): probablemente agrega instalaciones
  netbilling; la PMGD estricta es menor. Solo la capacidad (2–3 GW) entra al
  modelo.
- **E5 · Contradicción conceptual en la guía derivada.** "70% se transa en el
  spot" contradice el propio estudio (">70% se contrata a plazo"); corregida.

### Errores del modelo estructural, detectados y corregidos durante el desarrollo

- **E6 · Doble conteo de ERV (crítico, v1).** El stack de precios incluía
  solar/eólica en la base mientras la demanda neta ya las descontaba → el
  precio colapsaba a ~0. Corregido: el stack de fijación de precios es solo
  térmico-hidro; la ERV entra por la demanda neta (mecanismo documentado en el
  estudio §4.5).
- **E7 · Flujo de interconexión unidireccional (crítico, v1).** Solo se
  modelaba la exportación norte→centro: en horas de déficit norte, el norte
  quedaba preciado POR ENCIMA del centro (invertido vs la realidad
  Crucero ≤ Quillota). Corregido: flujo bidireccional (importación capada por L).
- **E8 · Piso SSCC asimétrico.** En horas de excedente sistémico donde todo el
  derrame se asignaba al norte, el norte recibía el piso (8) y el centro 0 →
  26 meses con media invertida. Corregido: el piso aplica a ambas zonas en
  horas de excedente.
- **E9 · RNG no determinista por escenario (v1).** Cada corrida consumía ruido
  nuevo → HVDC/BESS/GNL se comparaban contra ruido distinto. Corregido: RNG
  por año (seed 2026·100+año); los contrafactuales comparten ruido base.
- **E10 · Artefacto aceptado.** 49 h/año (0,09%) de "congestión inversa"
  (déficit norte > L) dejan al norte ≤4,3 USD/MWh sobre el centro en media
  mensual. Físicamente interpretable; documentado en el informe §6.

### Honestidad de calibración

- Crisis 2022: **+0,8%** de error en precio medio (104,9 vs 104 doc).
- Sesgo negativo post-2024 (−35% a −47%) declarado y explicado: sin primas
  SSCC en estrés, sin unit commitment, sin restricciones de red locales.
- Vertimiento: patrón y orden de magnitud correctos; nivel 2024-25 subestimado
  (~−10% en potencial 2025: 7.352 vs 8.200 GWh).
- Spread medio en congestión dentro del rango documentado (5–15 USD/MWh).

## Parte 1 · Guía de campo interactiva (v1)

## Errores corregidos

### A1 · Crosshair de § 01 inoperante — CRÍTICO (JS)

**Síntoma.** La serie de costo marginal prometía lectura por punto al mover el
mouse ("muévete con el mouse para leer cada punto"), pero el crosshair y el
tooltip nunca aparecían.

**Diagnóstico.** `d3.bisector(d => d.date).center(arr, x)` devuelve un **índice**
(entero), no el elemento. El handler lo trataba como punto: `p.date` era
`undefined`, la comparación `p.date >= d0` fallaba siempre, `rows` quedaba
vacío y el handler hacía `return` temprano. Además, los círculos de datos
tienen listeners propios de tooltip, pero quedan **debajo del overlay
transparente** de zoom/paneo, así que nunca recibían el evento: la feature
estaba doblemente muerta.

**Corrección.** Indexar el array con el índice devuelto y acotar al rango
válido:

```js
const arr = cmgData[b];
const i = d3.bisector(d => d.date).center(arr, date);
const p = arr[Math.max(0, Math.min(arr.length - 1, i))];
```

### A2 · Excepción en cada pointermove de § 02 — CRÍTICO (JS)

**Síntoma.** Al pasar el mouse sobre el gráfico de desacople Crucero/Quillota
se lanzaba `TypeError: Cannot read properties of undefined (reading 'v')` en
cada movimiento; tooltip y sello de spread jamás aparecían.

**Diagnóstico.** Mismo patrón A1: `pQ` era un índice, `pQ.m` era `undefined`,
el `find(p => p.m === pQ.m)` devolvía `undefined` (`pC`) y el handler reventaba
al formatear `pC.v`.

**Corrección.** Recuperar el elemento por índice acotado, mantener el cruce por
mes (`find`) como defensa si las series divergen en longitud, y guardar
`if (!pC) return;`.

### A3 · Contradicción de dominio en "Claves" § 06 — ALTO (contenido)

**Síntoma.** La clave "La frontera cliente libre se movió a 0,3 MW" afirmaba:
"Más del 70% de la energía **se transa en el spot**".

**Diagnóstico.** Contradice el propio estudio académico (Parte I.1.2: "más del
70% de la energía se transa mediante contratos de largo plazo") y el readout de
la propia § 01 ("Energía en contratos >70%"). En el esquema chileno el spot
(balances de transferencias) liquida las **diferencias** respecto de lo
contratado; confundirlo es exactamente el error conceptual que la guía
documenta en su prefacio.

**Corrección.** Reformulada a: "Más del 70% de la energía **se contrata a
plazo** — el spot liquida las diferencias entre generadores…".

### A4 · Código muerto — BAJO (JS)

Función `countUp(sel, target, suffix)` definida y nunca invocada. Eliminada.

## Mejoras aplicadas (no errores)

- **M1 · Momento-firma tipo referencia.** Botón "▶ Simular día" en el orden de
  mérito: barre la demanda por un ciclo de 24 h (perfil coseno, punta 20:00 ≈
  8.700 MW, valle 08:00 ≈ 3.900 MW en la escala simulada de 9.000 MW) durante
  18 s y se detiene ante cualquier interacción manual (drag, slider, escenario).
  Es el equivalente del "tangente que barre la curva" del ejemplo de referencia,
  aplicado al escalón del despacho.
- **M2 · Identidad y compartibles.** `favicon.svg` (rayo sobre papel
  milimetrado), metadatos Open Graph y Twitter Card.
- **M3 · Listo para desplegar.** `vercel.json` (clean URLs, cabeceras de
  seguridad), `README.md`, `.gitignore`.

## Hallazgos revisados y aceptados (sin cambio)

- **Escala del orden de mérito (9.000 MW) vs SEN real (~35 GW instalados,
  demanda 6–12 GW).** El gráfico es explícitamente una simulación pedagógica y
  el pie de carta lo declara; la demanda del slider (3.000–9.700 MW) es
  coherente con esa capacidad simulada, no con el sistema físico completo.
- **Curva de pato sintética.** Perfiles ilustrativos calibrados con la
  variación noche-día reportada 2022; declarado en el pie.
- **CMG por "meses reportados" (ene/abr/jul/oct).** Simplificación declarada en
  §01 y en el apéndice; los picos mensuales difieren.
- **Saldo del precio estabilizado "US$ 2.500 M (2023)"** vs "USD 2.000 M" del
  estudio: fuentes públicas de 2023 reportan montos distintos según el corte;
  se mantiene la cifra del dashboard con su año.
- **`informe.html`** es una versión anterior en tema oscuro sin los bugs A1/A2
  (no usa bisector); se conserva como archivo.
- **Dependencia de D3 por CDN** (`d3js.org`) y fuentes de Google Fonts: decisión
  de diseño asumida; para entornos offline se puede vendorizar como en otros
  proyectos del autor.

## Verificación

Servido local por HTTP y probado en navegador: `window.__errs` vacío (sin
excepciones), crosshair y tooltips operativos en §01 y §02, zoom/paneo con
doble clic para reencuadrar, cronología del apagón por botones y teclado,
simulación diaria del héroe, y modo "Comparar" de las 4 barras.
