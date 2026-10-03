# Auditoría técnica — SEN ▸ SPOT (dashboard `index.html`)

Auditoría de código y de dominio (mercado eléctrico chileno) sobre la guía de
campo interactiva, previa a su publicación. Cada hallazgo indica severidad,
diagnóstico y corrección aplicada.

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
