# Estudio académico del pricing dinámico del mercado spot eléctrico chileno

**Material de estudio exhaustivo sobre el Sistema Eléctrico Nacional (SEN) de Chile**
Período cubierto: 2020–2026 · Fuentes: Coordinador Eléctrico Nacional (CEN), Comisión Nacional de Energía (CNE), Ministerio de Energía, Ember, ACERA, Broker & Trader Energy, sector académico chileno y comparado.

---

## Prefacio y nota de uso

Este documento es la versión académica expandida del estudio que originó la página web interactiva sobre el SEN. Su propósito es servir como material de estudio profundo: cada sección está pensada para que un profesional o estudiante avanzado comprenda no solo el qué, sino el por qué y el cómo de los mecanismos del mercado spot eléctrico chileno, con las referencias normativas, físicas y económicas que los sustentan.

El documento se organiza en diez partes progresivas. Las primeras tres sientan las bases conceptuales e institucionales (qué es un mercado spot, por qué la electricidad es especial, cómo está organizado el SEN). Las partes IV a VII desglosan los mecanismos operativos, los episodios críticos de los últimos cinco años y los fenómenos estructurales (desacople, vertimiento, blackout). La parte VIII compara el caso chileno con sistemas de referencia internacionales. La parte IX proyecta hacia adelante y la parte X cierra con glosario, bibliografía y preguntas de autoevaluación.

Las cifras utilizadas provienen de fuentes oficiales y de consultoras con credibilidad documentada; cuando hay discrepancias entre fuentes, se señala en el cuerpo. El lector debe tratar los precios spot como magnitudes operativas que cambian hora a hora, y los promedios mensuales como simplificaciones útiles pero no exentas de sesgo por la composición horaria.

---

## Parte I. Fundamentos teóricos del mercado eléctrico y el pricing dinámico

### 1.1. Por qué la electricidad no es un commodity como los demás

El primer paso para entender el mercado spot eléctrico es comprender por qué la electricidad tiene una estructura de mercado radicalmente distinta a la del petróleo, el gas o los metales. La razón no es regulatoria sino física, y se resume en cinco propiedades.

La primera propiedad es la **no-almacenabilidad** a escala de red. Aunque existen baterías, pumped-hydro y, en el futuro, hidrógeno, su capacidad agregada representa una fracción mínima de la demanda instantánea. En un sistema del tamaño del SEN, con una demanda que oscila entre 6.000 y 12.000 MW según la hora, la energía total almacenada disponible para arbitraje en tiempo real es del orden de 200–400 MWh (lo que algunos llaman "la batería del sistema"). Esto es suficiente para gestionar fluctuaciones de minutos, no para arbitrar precios diarios. La consecuencia económica directa es que el precio spot de la electricidad no puede ser arbitrado a gran escala: si el precio es alto, no puedes comprar barato para almacenar y vender después, salvo en proporciones diminutas. Por eso el spot eléctrico es genuinamente spot.

La segunda propiedad es la **necesidad de balance instantáneo**. La frecuencia de la red (50 Hz en Chile, 60 Hz en USA) debe mantenerse en una banda muy estrecha (típicamente 49,8 a 50,2 Hz). Si la generación supera a la demanda, la frecuencia sube; si la demanda supera a la generación, la frecuencia baja. Desviaciones sostenidas dañan equipamiento y, en el extremo, producen apagones como el del 25 de febrero de 2025. Por lo tanto, la operación del sistema requiere un **despacho coordinado en tiempo real** que asegure que la suma de la generación más la importación menos la demanda menos la exportación es exactamente cero en cada instante. Esta es la función del Coordinador Eléctrico Nacional.

La tercera propiedad es la **indivisibilidad de la red**. La electricidad fluye por las líneas según las leyes de Kirchhoff, no según los contratos. Esto significa que la energía generada en Antofagasta y consumida en Santiago fluye por una red de transmisión compartida, y los flujos resultantes dependen del estado físico de todas las líneas, no de los contratos bilaterales. Cuando una línea se congestiona, el operador debe **redespachar** unidades para mantener el balance, y ese redespacho tiene un coste que se refleja en los precios marginales diferenciados por barra.

La cuarta propiedad es la **inelasticidad de la demanda de corto plazo**. En el momento en que el operador necesita reducir 1.000 MW de consumo, los hogares no pueden dejar de usar electricidad a esa velocidad. Existen programas de respuesta de demanda (en Chile aún incipientes), pero la mayoría del ajuste en tiempo real se hace por el lado de la generación. Esto significa que el precio spot está determinado casi enteramente por la curva de oferta, no por la curva de demanda.

La quinta propiedad es la **escasez de inversión en capacidad de respaldo**. Un mercado puramente spot, sin pagos por capacidad, no genera señales para invertir en centrales que solo operan unas pocas horas al año pero son necesarias para la seguridad de suministro. Por eso casi todos los sistemas eléctricos del mundo combinan un mercado spot con mecanismos de capacidad: en Chile, el pago por potencia; en USA, los capacity markets (PJM, ISO-NE); en Europa, los mecanismos de capacidad (CRM francés, mercado de capacidad español).

Estas cinco propiedades explican por qué los mercados eléctricos son **mercados diseñados**: ni spot puro ni regulación pura, sino una construcción institucional que internaliza las restricciones físicas. El pricing dinámico del mercado spot es el resultado natural de esa construcción, y Chile no es la excepción.

### 1.2. La noción de mercado spot en electricidad

Un mercado spot es aquel en el que la transacción y la liquidación ocurren en un horizonte muy corto. En electricidad se distinguen tres niveles:

El **mercado de contratos** (forward, futuros, PPA bilaterales, licitaciones reguladas) es el grueso del volumen en sistemas maduros: en Chile, más del 70% de la energía se transa mediante contratos de largo plazo entre generadores y distribuidoras, o entre generadores y clientes libres. Estos contratos no afectan el despacho en tiempo real; solo afectan la valorización posterior (los generadores venden su energía contratada al precio spot, y reciben la diferencia como pago).

El **mercado day-ahead** es donde se casan las ofertas de generación y demanda para las 24 horas del día siguiente. En Europa, EPEX SPOT ejecuta una subasta diaria a las 12:00 CET que produce 24 precios horarios. En Chile, **no existe un day-ahead organizado**: el despacho del día siguiente se programa internamente por el Coordinador a partir de la mejor información disponible (pronóstico de demanda, pronóstico de aportes hídricos, mantenimientos programados, disponibilidad declarada), pero ese programa no es vinculante para los contratos; es un plan operativo que puede modificarse a tiempo real.

El **mercado intradiario** (intraday continuo en Europa, despacho en tiempo real en Chile) permite ajustes de último minuto. En Europa, los agentes pueden re-casar órdenes hasta minutos antes de la entrega. En Chile, el Coordinador emite instrucciones de despacho en tiempo real, y los generadores se obligan a operar según el costo marginal de corto plazo (el CV más los servicios complementarios).

Lo que coloquialmente se llama **"mercado spot" en Chile** se refiere, en realidad, a las **transferencias de energía valorizadas al costo marginal**: la diferencia entre lo que cada generador inyectó físicamente y lo que tenía contratado se liquida a precio spot. Este mecanismo, llamado **balances de transferencias de energía**, es la pieza clave que muchos análisis confunden con un mercado propiamente dicho. Un mercado spot exige ofertas y demandantes que concurren; el sistema chileno tiene un despacho centralizado y una valorización ex-post. La diferencia importa porque cambia los incentivos: en un mercado spot, el generador puja para maximizar su ingreso marginal; en el esquema chileno, el generador declara sus costos y el Coordinador lo despacha según mérito.

### 1.3. Pricing dinámico: concepto, dimensiones y variantes

Pricing dinámico es toda estrategia de ajuste de precios en tiempo real en función de variables observables. En electricidad, se manifiesta en cinco dimensiones que conviene distinguir.

La primera dimensión es la **granularidad temporal**: cada cuánto cambia el precio. Va desde el año (tarifa plana) hasta los 15 minutos (FTRs en algunos mercados USA) o el segundo (regulación secundaria en sistemas modernos). En Chile, el costo marginal cambia cada hora, con ajustes en tiempo real.

La segunda dimensión es la **granularidad espacial**: si hay un único precio nacional o un precio por nodo/barra. En Chile, hay un precio por barra (cada subestación del SEN), y la diferencia entre barras refleja el coste de las congestiones. En sistemas como el PJM (USA), la granularidad llega a los 12.000 nodos individuales.

La tercera dimensión es el **alcance de la señal**: si refleja soloel equilibrio agregado de oferta y demanda, o incorpora datos individuales del usuario. Aquí la distinción regulatoria clave: pricing dinámico agregado (que responde al balance de oferta y demanda zonal o nodal) es distinto del surveillance pricing (que personaliza según datos del consumidor). En Chile, la primera modalidad es el corazón del mercado mayorista; la segunda está empezando a discutirse con la irrupción de los medidores inteligentes y los agregadores.

La cuarta dimensión es el **mecanismo de transmisión al cliente final**: si el precio spot llega directamente al consumidor (dynamic retail tariff, como en UK o Finlandia), se promedia y estabiliza (precio estabilizado chileno, average price en España), o permanece en el mercado mayorista sin afectar al cliente regulado. En Chile, el cliente regulado paga una tarifa construida sobre un **precio de nudo promedio** que se determina semestralmente por la CNE, y un **precio estabilizado** regulado por el DS 88/2020 que amortigua la volatilidad.

La quinta dimensión es el **mecanismo de respaldo**: si existe un mercado de capacidad, contratos de largo plazo, pagos por potencia, o solo spot. Chile combina un mercado spot valorizado al costo marginal, un sistema de licitaciones reguladas para el segmento de clientes regulados, y un pago por potencia regulado por la CNE. La combinación determina la intensidad del pricing dinámico en el cliente final.

### 1.4. Por qué el mercado spot es dinámico, no aleatorio

Una confusión frecuente es tratar la volatilidad del spot eléctrico como ruido o como evento. No lo es. La volatilidad es la **señal** que el sistema necesita para coordinarla oferta y la demanda instantáneas, y es dinámica en un sentido preciso: refleja cambios reales enoferta y demanda, no en expectativas. Si la demanda sube un 5% porque hace calor, el precio spot sube; si entra 1.000 MW de generación solar no prevista, el precio spot baja. Esta es la diferencia entre **dinámico** y **estocástico**: dinámico significa determinista en función de las variables observables; estocástico significaría aleatorio e impredecible. El mercado spot es lo primero.

La consecuencia operativa es que el precio spot es **información densa**: contiene señales sobre la disponibilidad de generación, el estado de la red de transmisión, la hidrología, el precio de los combustibles, y el nivel de demanda. Aprender a leer el spot es aprender a leer la operación del sistema en tiempo real. La curva de costos marginales del SEN, vista en una pantalla del CEN, dice más sobre la salud del sistema eléctrico chileno que cualquier estadística agregada mensual.

### 1.5. La distinción entre precio spot y precio regulado

Para evitar errores conceptuales, la pieza clave es distinguir:

- **Costo marginal** (cMg): el coste variable de producir una unidad adicional de energía en una barra y hora dadas. Es un concepto físico-operativo, calculado por el Coordinador.

- **Precio spot**: el cMg, una vez publicado y usado para valorizar las transferencias. En Chile, es esencialmente el cMg mismo.

- **Precio de nudo (PN)**: precio regulado, fijado semestralmente por la CNE, que las distribuidoras cobran a clientes regulados. Se construye a partir del cMg proyectado, los precios de combustibles esperados y el costo de la potencia.

- **Precio estabilizado (PE)**: precio regulado, fijado por el Ministerio de Energía según el DS 88/2020, que suaviza la volatilidad del PN en el tiempo para evitar alzas abruptas en las tarifas finales. Es lo que realmente paga la mayoría de los hogares.

- **Precio libre**: precio pactado bilateralmente entre generador (o comercializador) y cliente libre (>0,3 MW según RE N°58/2024, modificado por RE N°13/2025).

La cadena es: cMg (operativo) → precio spot (valorización ex-post) → PN (regulación ex-ante) → PE (regulación ex-post con suavizamiento) → tarifa al cliente regulado. Cada eslabón introduce mecanismos de estabilización. Por eso un hogar chileno promedio no ve la volatilidad del spot en su factura mensual: la ve el sistema, y se la devuelve amortiguada al cabo de meses.

---

## Parte II. Arquitectura institucional del Sistema Eléctrico Nacional

### 2.1. La cadena institucional chilena: Ministerio, CNE, SEC, CEN

El sector eléctrico chileno es una construcción de cuatro décadas de reformas liberalizadoras. La Ley General de Servicios Eléctricos (DFL N°4/2006, refundido) es la columna vertebral, modificada por leyes posteriores: Ley 19.940 (2004, ley corta 1), Ley 20.018 (2005, licitaciones), Ley 20.220 (2007, perfeccionamiento), Ley 20.257 (2008, ERNC), Ley 20.402 (2009, expansión), Ley 20.726 (2013, licitaciones y contratos), Ley 20.805 (2015, ERNC), Ley 20.936 (2016, transmisión), Ley 21.118 (2018, Net Billing), Ley 21.185 (2019, estabilización), Ley 21.194 (2019, licitaciones), Ley 21.220 (2020, DS 88 sobre precio estabilizado), Ley 21.305 (2021, eficiencia energética), Ley 21.505 (2022, almacenamiento), y varias más. Cada una de estas leyes ha movido algún ladrillo del edificio.

El **Ministerio de Energía** define la política sectorial y emite los reglamentos. La **Comisión Nacional de Energía (CNE)**, organismo técnico descentralizado, es el regulador económico: fija precios regulados, aprueba planes de expansión de transmisión, conduce las licitaciones de suministro, y emite normas técnicas. La **Superintendencia de Electricidad y Combustibles (SEC)** es el regulador técnico y fiscalizador: verifica calidad de servicio, sanciona incumplimientos, y procesa las contingencias mayores (como el apagón de febrero de 2025). El **Coordinador Eléctrico Nacional (CEN)**, creado en 2016 (Ley 20.936) y operativo desde 2017, es el operador independiente del sistema: coordina la operación en tiempo real, calcula el costo marginal, liquida las transferencias, y proyecta la expansión de la red.

Esta arquitectura busca una separación clara de funciones: el Ministerio propone política, la CNE regula, la SEC fiscaliza, el CEN opera. El CEN es **técnico e independiente**: no depende del Ministerio, no responde a las generadoras ni a las distribuidoras, y tiene personalidad jurídica propia. Es la pieza clave del modelo, y su consolidación es lo que permite hablar de un mercado spot en sentido técnico.

### 2.2. El Coordinador Eléctrico Nacional: función y estructura

El CEN coordina el **Sistema Eléctrico Nacional (SEN)**, que desde 2017 agrupa las dos antiguas zonas del país: el Sistema Interconectado Central (SIC) y el Sistema Interconectado del Norte Grande (SING). Antes de 2017, había dos CDEC (Centros de Despacho Económico de Carga) independientes; la unificación fue una decisión técnica-política mayor, porque implicó acoplar dos sistemas con estructuras de generación, hidrología y topología muy distintas.

El SEN se extiende **desde Arica y Parinacota (extremo norte) hasta la región de Los Lagos (sur)**, cubriendo más de 3.000 km de longitud. Abarca 16 regiones administrativas (14 continentales más Arica y Parinacota, y la región de Magallanes, que sigue siendo un sistema aislado). Atiende a más del 99% de la población. La capacidad instalada en 2024–2025 ronda los 35.000 MW, con una generación anual en torno a 85.000 GWh.

La operación se organiza en tres niveles: el **Centro de Despacho y Control (CDC)**, que coordina en tiempo real las instrucciones de despacho; los **Centros de Control de Empresas** (uno por generador relevante o transmisora), que ejecutan las instrucciones a sus unidades; y los **procedimientos de programación** (programa diario, semanal, mensual) que anticipan el despacho. El CEN emite cientos de instrucciones por hora, cada una con su correspondiente costo variable, y con ellas construye el **costo marginal ex-post** que valora las transferencias.

El CEN publica en su web el **Costo Marginal en Línea** (cada 5–15 minutos, preliminar) y el **Costo Marginal Real** (ex-post, usado para liquidaciones). Desde julio de 2024, se aplica una metodología actualizada que introdujo cambios relevantes en la valorización, sobre todo en la separación de la energía y los servicios complementarios. Estos reportes son la materia prima de cualquier análisis de mercado.

### 2.3. La Comisión Nacional de Energía: el regulador económico

La CNE tiene cuatro funciones principales en el sector eléctrico. Primero, **fija los precios regulados** que las distribuidoras cobran a los clientes regulados. Esto incluye el **precio de nudo de la energía** (fijado semestralmente), el **precio de nudo de la potencia**, y el **precio estabilizado** (PE) bajo el DS 88/2020. Segundo, **administra el proceso de licitaciones de suministro** para clientes regulados, definiendo las bases técnicas, los bloques de suministro, los períodos, y los precios de reserva. Tercero, **planifica la expansión de la transmisión** mediante el Plan de Expansión Anual, que define las obras troncales y de subtransmisión que se licitarán. Cuarto, **monitorea el funcionamiento del mercado** y emite informes públicos como el Reporte Energético Financiero, el Reporte de Precios de Combustibles, y la Proyección de Precios de Combustibles.

El modelo chileno de regulación económica es de tipo **price-cap con ajustes por canastas**: la CNE determina una tarifa objetivo basada en costos eficientes, y la empresa distribuidora se queda con la diferencia (positiva o negativa) entre su costo real y la tarifa regulada. Esto crea incentivos a la eficiencia pero también ha generado controversias por la acumulación de saldos pendientes (la "deuda con las distribuidoras") que en algunos momentos superó los USD 2.000 millones.

### 2.4. El sector privado: generadores, transmisoras, distribuidoras

El sector eléctrico chileno es propiedad y operación de empresas privadas, con fuerte presencia de actores internacionales. Los principales generadores son **Enel Generación** (italiana, dueña de la mayor parte del parque hidroeléctrico y de centrales a gas en Quintero), **Engie Chile** (francesa,dueña de centrales a carbón y renovables), **AES Andes** (norteamericana, carbón y renovables), **Colbún** (chilena, gas e hidro), **Enel Green Power** (renovables), y **Acciona Energía** (renovables). El sector de transmisión está dominado por **Transelec** (hoy controlada por el grupo canadiense Brookfield), **ISA InterChile** (colombiana, dueña de la línea que falló en 2025), y **CGE Transmission**. La distribución se reparte entre **Enel Distribución** (Santiago), **CGE** (gran parte del país), y algunas distribuidoras regionales menores.

Esta concentración empresarial tiene implicaciones regulatorias: el **Informe de Monitoreo de la Competencia** del CEN, publicado anualmente, analiza la estructura de mercado y la existencia de poder de mercado. La existencia de clientes libres (con potencia conectada >0,3 MW) es un contrapeso a esta concentración, porque permite a los grandes consumidores negociar directamente y disciplinar a las generadoras.

### 2.5. La distinción entre cliente regulado y cliente libre

La frontera regulatoria entre cliente libre y regulado es, en sí misma, una decisión de política industrial. Originalmente (DFL N°4/2006), el límite era 2.000 kW (2 MW): un cliente con potencia conectada superior podía negociar libremente. La Ley 20.936 (2016) lo rebajó a 0,5 MW, y la **Resolución Exenta N°58 del 5 de diciembre de 2024** (modificada por RE N°13 del 6 de febrero de 2025) lo bajó a **0,3 MW**, previa consulta favorable del TDLC (Tribunal de Defensa de la Libre Competencia) mediante su Informe N°33/2024.

La lógica es que clientes con potencia superior a 0,3 MW (300 kW, equivalente a un edificio de oficinas mediano, un supermercado grande, o una industria pequeña) tienen poder de negociación suficiente para pactar precios libres y, al hacerlo, presionan a la baja los precios regulados al reducir la demanda cautiva. La rebaja del límite en 2024-2025 amplía la base de clientes libres, lo que afecta tanto a las distribuidoras (pierden volumen) como a las generadoras (pueden expandir ventas sin pasar por la CNE).

Históricamente, la proporción de clientes libres ha oscilado entre 5% y 8% del total de clientes del SEN, pero representan alrededor del 30-40% de la energía consumida (por su mayor consumo unitario). Tras la rebaja a 0,3 MW, se proyecta que la proporción de energía libre crezca al 45-50%, una transformación significativa.

---

## Parte III. Mecánica operativa: costo marginal, merit order y balance oferta-demanda

### 3.1. La curva de oferta agregada del SEN

La curva de oferta del SEN es la combinación ordenada, de menor a mayor costo variable, de toda la capacidad de generación disponible en una hora dada. Su forma es la siguiente:

- **Renovables de costo marginal cero** (solar, eólica pasada, hidro de pasada): entran primero, hasta el límite de su producción horaria. Su CV declarado suele ser 0, aunque en la práctica tienen un costo de oportunidad cuando hay vertimiento (la energía que se pierde o se paga para que salga del sistema).
- **Hidroeléctrica de embalse**: CV bajo (5-15 USD/MWh), pero con decisión económica de cuándo turbinar basada en el valor del agua embalsada. En sistemas con hidrología predominante (como el sur de Chile), la operación del embalse se optimiza con modelos estocásticos que proyectan aportes futuros.
- **Biomasa y geotermia**: CV medio-bajo (15-25 USD/MWh), inflexibles por diseño (la biomasa necesita un régimen térmico constante).
- **Carbón**: CV 25-35 USD/MWh, pero con tendencia a la baja por el cierre programado de centrales (Chile ha comprometido el cierre de todas las centrales a carbón antes de 2040, con hitos parciales en 2025 y 2030).
- **Gas natural licuado (GNL)**: CV 35-55 USD/MWh en condiciones normales, pero puede subir a 100+ USD/MWh en picos de precio internacional.
- **Diésel**: CV 80-150 USD/MWh, usado como **último recurso**. En el estudio ACENOR de 2022 se estimaba que el diésel de seguridad mensual podría llegar a 264.000 m³ con máximos diarios de 6.673 m³.

La forma escalonada de la curva es lo que produce el **salto del costo marginal**: cuando la demanda cruza un umbral de capacidad, el precio salta al CV de la siguiente unidad. Este es el fenómeno que la página web simula con el slider interactivo.

### 3.2. La operación hora a hora: el ciclo del CEN

Cada hora, el CEN ejecuta un ciclo de decisiones que se puede esquematizar así:

En la **fase de programación**, el CEN recibe de las generadoras sus **declaraciones de costo variable** y **disponibilidad** para las próximas 24-168 horas. También recibe pronósticos de **aporte hidráulico** (de la Dirección General de Aguas y de las propias empresas), **pronóstico de demanda** (de la demanda histórica corregida por clima, calendario y actividad económica), y **pronóstico de generación renovable variable** (a partir de modelos numéricos de predicción meteorológica). Con esta información, corre un modelo de optimización (mixed-integer programming) que minimiza el costo total de operación sujeto a restricciones técnicas: balance instantáneo, reservas operativas, mínimos técnicos de las unidades, rampas de subida/bajada, y límites de transmisión.

En la **fase de despacho en tiempo real** (RTD, real-time dispatch), que ocurre cada 15 minutos o cada 5 minutos, el CEN re-optimiza considerando la información actualizada: demanda real, generación real de renovables, disponibilidad efectiva de las unidades, e imprevistos (falla de una central, desconexión de una línea). El resultado es un conjunto de instrucciones de despacho que se envían a las unidades a través de sus Centros de Control.

En la **fase de liquidación** (días o semanas después), el CEN calcula el **costo marginal real** ex-post de cada hora y cada barra, y con ello liquida las **transferencias de energía** entre generadores. Una central que inyectó 100 MWh pero tenía contratado vender 80 MWh debe comprar los 20 MWh de diferencia al costo marginal; si inyectó solo 70 MWh, debe comprar 30 MWh al costo marginal. Este balance se llama **"balance de transferencias"** y es la esencia del mercado spot chileno.

### 3.3. Servicios complementarios y su tratamiento en el costo marginal

El sistema eléctrico no solo requiere energía: requiere **frecuencia estable, voltaje estable, y capacidad de respuesta ante contingencias**. Estos servicios se llaman genéricamente **servicios complementarios** (SSCC en la jerga chilena), e incluyen:

- **Regulación de frecuencia** (primaria, secundaria, terciaria): ajuste automático o manual de generación para corregir desviaciones de la frecuencia nominal.
- **Reserva en giro**: capacidad de generación sincronizada al sistema que puede responder en minutos.
- **Reserva fría**: capacidad de generación que puede arrancar y sincronizarse en horas.
- **Control de voltaje**: aporte de potencia reactiva para mantener tensiones en rangos aceptables.
- **Desconexión automática de carga (EDAC)**: esquemas que cortan consumo predefinido para evitar colapsos sistémicos.

Históricamente, los SSCC se valoraban y remuneraban por mecanismos separados del costo marginal de energía. Desde la reforma de 2024, el CEN ha avanzado en internalizarlos: parte de la remuneración por SSCC se incluye como **componentes adicionales** del costo marginal, especialmente en barras con restricciones de seguridad. Esto significa que el "costo marginal" que se publica tiene dos o más componentes: el **cMg de energía** (lo que hemos descrito) y los **componentes de SSCC** (que pueden ser positivos o negativos).

El impacto práctico es que el costo marginal observado en una barra incluye, en horas de estrés, una prima por seguridad de suministro. Esta prima es lo que explica que en ciertas horas (típicamente las de máxima demanda y mínima reserva), el cMg salte a valores anormalmente altos que no se corresponden con el CV de las unidades despachadas.

### 3.4. La hidrología como variable sistémica

El SEN tiene una **matriz de generación con componente hidroeléctrica significativa pero decreciente**: alrededor del 25% de la generación anual histórica provenía de hidroeléctricas de embalse y pasada, aunque esta proporción ha caído con el aumento de la generación solar. La capacidad hidroeléctrica instalada se concentra en la zona centro-sur (Maule, Biobío, Los Ríos), con embalses grandes como Pangue, Ralco, Pangue, Colbún-Machicura, y Lago Laja.

La hidrología es la variable que más afecta el costo marginal en el corto plazo. Un año seco (como 2021 y, en parte, 2022) obliga a despachar más generación térmica cara; un año húmedo (como 2024) permite ahorrar agua en los embalses y mantener el costo marginal bajo. La **operación óptima de embalses** es un problema de optimización estocástica que el CEN resuelve con modelos que proyectan aportes futuros y asignan el agua disponible entre el presente y el futuro, maximizando el valor esperado de la energía generada.

La **crisis 2022-2023** fue esencialmente una crisis hidrológica exacerbada por la indisponibilidad de GNL y la necesidad de recurrir al diésel. Volveremos sobre esto en la Parte V.

### 3.5. La formación del precio por barra: teoría de la congestión

En un sistema sin congestión de transmisión, habría un único precio marginal en todo el SEN. Pero el SEN tiene **miles de líneas de transmisión** con capacidad finita, y en muchas horas del año algunas de esas líneas operan cerca de su límite. Cuando una línea se congestiona, el sistema se divide en dos zonas: la zona exportadora (donde sobra generación) y la zona importadora (donde falta). El precio marginal en la zona importadora sube; en la zona exportadora, baja. La diferencia se llama **desacople de precios** o **congestión nodal**.

El **caso chileno prototípico** es el desacople Crucero (norte) vs Quillota (centro). La línea troncal de 500 kV que conecta la zona norte con la zona centro tiene capacidad limitada (alrededor de 1.500-2.500 MW en condiciones nominales, reducidos en horas de alta temperatura o alta generación solar). En horas de máxima generación solar, la zona norte puede tener un costo marginal cercano a cero (porque hay mucha energía que no se puede evacuar y termina vertida), mientras que en el centro puede haber un costo marginal de 50-100 USD/MWh. La diferencia refleja el coste de oportunidad de no poder traer más energía limpia al centro.

La **expansión de la transmisión** es la respuesta estructural. El Plan de Expansión de Transmisión que publica anualmente la CNE define las obras prioritarias. La **línea HVDC Kimal-Lo Aguirre** (en construcción, ~2.000 km, 3.000 MW de capacidad, ±600 kV) es la obra más ambiciosa del sistema y está diseñada precisamente para mitigar el desacople norte-centro; su entrada en operación, prevista para 2029-2030, cambiará radicalmente la geografía de precios del SEN.

---

## Parte IV. El mercado spot chileno en detalle

### 4.1. El balance de transferencias de energía

El balance de transferencias es el mecanismo central del mercado spot chileno. Cada generador, al final del período de liquidación (mensual), debe declarar su **energía inyectada físicamente** (medida en los puntos de inyección al sistema) y su **energía comprometida en contratos** (con distribuidoras, con clientes libres, o con otros generadores). La diferencia se líquida al costo marginal.

Por ejemplo, una central hidroeléctrica puede haber inyectado 200 GWh en un mes, tener contratos por 150 GWh, y por tanto tener un excedente de 50 GWh. Esos 50 GWh se venden al pool al costo marginal ponderado por hora del mes. Si el costo marginal promedio del mes fue 45 USD/MWh, el generador recibe 2,25 M USD por ese excedente.

Si en cambio la central inyectó 100 GWh pero tenía contratos por 150 GWh, debe comprar 50 GWh al pool a 45 USD/MWh, es decir, paga 2,25 M USD. Este generador tiene una **posición compradora** en el mercado spot, y la diferencia entre el precio contratado y el spot es lo que determina si el contrato fue favorable o desfavorable.

Para los **clientes libres**, la dinámica es similar pero al revés: el cliente compra a un generador a precio contratado (digamos 60 USD/MWh) y consume 100 GWh en el mes; su consumo físico real se valora al spot para los balances de transferencias, y la diferencia entre el precio contratado y el spot se cobra o se paga como ajuste.

### 4.2. El precio de nudo: definición, cálculo y rol

El **precio de nudo (PN)** es el precio regulado que las distribuidoras pagan a las generadoras (o a sus comercializadoras) por la energía suministrada a clientes regulados. Se calcula semestralmente por la CNE y se publica en abril (para el primer semestre) y octubre (para el segundo semestre).

El cálculo del PN se basa en una **proyección de costos medios de generación a 6 meses**, considerando: costos de combustibles (carbón, GNL, diésel) proyectados; costo variable de operación y mantenimiento; precio esperado del agua; costo de la potencia de punta; y peajes de transmisión. El resultado es un **precio de nudo de la energía** (USD/MWh) y un **precio de nudo de la potencia** (USD/kW-mes), definidos por barra.

Cuando el costo marginal real del mes difiere del PN proyectado, se activa un mecanismo de **compensación**: si el spot fue mayor al PN, las generadoras reciben un sobrecosto (pagado por la demanda); si fue menor, las generadoras devuelven la diferencia. Este mecanismo se llama **"Account Difference"** y es fuente de cuantiosos saldos pendientes en períodos de alta volatilidad (como 2022-2023).

### 4.3. El precio estabilizado (DS 88/2020) y la Ley 21.185

Tras la crisis de 2019 (alza de tarifas tras la guerra comercial y la caída del GNL), el legislador chileno aprobó la **Ley 21.185 (2019)** que creó un **mecismo transitorio de estabilización de precios** para los clientes regulados, vigente hasta diciembre de 2027. Este mecanismo congela las tarifas a niveles de 2019 y financia la diferencia con un fondo público (suscripción de bonos y aportes fiscales). El **Decreto Supremo 88/2020** reguló la implementación.

El **precio estabilizado (PE)** es, en la práctica, lo que paga el cliente regulado. Se calcula como un promedio de los PN de los últimos 12 meses, con un factor de ajuste trimestral limitado al 5% para evitar saltos. Esto produce una tarifa mucho más estable que el spot subyacente.

La diferencia entre el PE que paga el cliente y el costo marginal real que paga el sistema se acumula en un **"saldo de estabilización"** que se financia con deuda pública. Este saldo alcanzó más de USD 2.500 millones en 2023, y es una de las principales fuentes de tensión fiscal del sector eléctrico chileno.

### 4.4. El pago por potencia y el mercado de capacidad

El **pago por potencia** es el complemento de capacidad al mercado spot chileno. Cada mes, las centrales reciben un pago regulado por la potencia firme que aportan al sistema, calculado con base en la **potencia de suficiencia** (la capacidad que puede garantizarse en condiciones hidrológicas adversas). El precio de la potencia se fija anualmente por la CNE y se cobra a la demanda a través de los PN.

La potencia de suficiencia se calcula mediante un modelo probabilístico que estima, para cada central, cuánta capacidad puede aportar al sistema en las horas críticas. Las centrales renovables variables (solar, eólica) tienen una potencia de suficiencia menor que su capacidad instalada, porque su producción es intermitente. El cálculo exacto ha sido objeto de debate regulatorio y ha cambiado varias veces en los últimos años.

No existe en Chile un **mercado de capacidad** explícito como el de PJM o ISO-NE, donde los generadores ofertan capacidad y reciben pagos por comprometerse a estar disponibles. El mecanismo chileno es regulado y centralizado, lo que simplifica la operación pero reduce la eficiencia en la señal de inversión.

### 4.5. Cómo se determina la curva de demanda para el despacho

Una pieza clave que a menudo se pasa por alto: la **curva de demanda que usa el CEN** no es la misma que la demanda agregada de los hogares. Es una **demanda neta** que ya descuenta la generación renovable variable (que entra automáticamente por mérito). Esto significa que, en una hora de máxima generación solar, la demanda neta que enfrenta el CEN es la demanda agregada de los hogares **menos la generación solar**; por eso el costo marginal puede caer dramáticamente a mediodía.

El CEN también descuenta la **generación distribuida** (PMGD, Pequeños y Medios de Generación Distribuida): centrales renovables de menos de 9 MW conectadas a redes de distribución. Chile tiene una explosión de PMGD solares (más de 6.000 unidades), especialmente en el norte, que se inyectan a la red de distribución sin pasar por el mercado spot mayorista. Esto ha creado controversias porque los PMGD no internalizan el coste de las congestiones que generan.

### 4.6. La interacción con los Pequeños Medios de Generación Distribuida (PMGD)

El tratamiento de los PMGD es uno de los temas regulatorios más espinosos del SEN. Los PMGD venden su energía a precio estabilizado (60-70 USD/MWh en condiciones normales), independientemente del costo marginal horario. Esto significa que cuando el costo marginal es bajo (horas de sol abundante, vertimiento), los PMGD cobran mucho más que el mercado, generando **ingresos excesivos** a costa del sistema. Cuando el costo marginal es alto (noches de invierno), los PMGD no se mueven, dejando a la demanda expuesta al spot térmico.

La CNE y el CEN han intentado introducir señales de precio para los PMGD, pero el cambio es lento por la cantidad de actores involucrados y por la defensa política del esquema. En el mediano plazo, la reforma más probable es migrar a los PMGD hacia un esquema de **precio spot horario** con contratos a plazo que les den cobertura, similar al modelo que ya rige para las grandes centrales.

---

## Parte V. La crisis 2022-2023: sequía, GNL caro y diésel de seguridad

### 5.1. La tormenta perfecta

La crisis 2022-2023 en el mercado eléctrico chileno no fue un evento aislado: fue la convergencia de cuatro factores que se reforzaron mutuamente.

El primer factor fue la **sequía extrema**. La megasequía que afecta al centro-sur de Chile desde 2010 llegó a su peak en 2021-2022, con aportes hídricos a los embalses un 30-40% por debajo del promedio histórico. Los embalses de Colbún y Lago Laja, los más grandes del sistema, llegaron a niveles mínimos. Sin agua embalsada, la generación hidroeléctrica cayó y fue reemplazada por generación térmica.

El segundo factor fue el **precio internacional del GNL**. La invasión rusa de Ucrania (febrero 2022) disparó los precios del gas natural en Europa, y por arbitraje en todo el mundo. El **Henry Hub** (referencia para el GNL chileno) llegó a 8,79 USD/MMBtu en agosto de 2022, multiplicando por 3-4 los precios previos. Chile, que importa la mayor parte de su GNL, vio su costo de generación a gas multiplicarse.

El tercer factor fue la **indisponibilidad de GNL argentino**. Argentina aplica retenciones a las exportaciones de gas, lo que encarece el gas que llega a Chile desde Mendoza. En momentos de alta demanda interna argentina, los envíos a Chile se cortan, dejando al sistema sin esa fuente.

El cuarto factor fue la **disponibilidad limitada de diésel**. Chile no tiene producción significativa de diésel, y debe importarlo. El mantenimiento de stocks de seguridad es costoso (se estima USD 82-161 millones anuales solo en logística). El Decreto Supremo N°1 de 2022 y el decreto anterior declararon la "vulnerabilidad del sistema" e instruyeron mantener disponibilidad de diésel de seguridad entre marzo y septiembre de 2022.

### 5.2. El Decreto de Racionamiento Preventivo y el diésel de seguridad

El gobierno, a través del Ministerio de Energía y la CNE, declaró el **Estado de Vulnerabilidad del SEN** y emitió el **Decreto de Racionamiento Preventivo**, que instruyó a las empresas generadoras a mantener una disponibilidad mínima de diésel. El CEN asignó mensualmente el diésel de seguridad a unidades específicas en función de las necesidades zonales, y los costos se trasladaron a la demanda a través de los cargos respectivos.

El estudio **ACENOR (2022)** "Petróleo en el Sistema Interconectado de Chile" cuantificó el coste: en el escenario más favorable, el diésel de seguridad mensual sería de 136.000 m³, con un coste logístico de 1,8-3,34 USD/MWh. En el escenario más desfavorable, hasta 264.000 m³ mensuales, con un coste de 2,6-5,2 USD/MWh. Estas cifras parecen bajas, pero se sumaban a un costo marginal ya elevado por el GNL caro.

El decreto permitió que el SEN sorteara los momentos más críticos de 2022, pero tuvo un costo fiscal significativo y expuso la **dependencia chilena de los combustibles importados** como vulnerabilidad estructural.

### 5.3. El comportamiento del costo marginal durante la crisis

El **costo marginal de Crucero 220 kV** (barra del norte) alcanzó **93,5 USD/MWh en marzo de 2022**, el nivel más alto en muchos años. El **costo marginal de Quillota 220 kV** (barra del centro) llegó a **130,4 USD/MWh en marzo de 2023**, con un alza del 31,4% respecto al año anterior. La diferencia de 30-40 USD/MWh entre Crucero y Quillota refleja el coste de la congestión troncal, que en esas condiciones era severa.

El **componente nocturno vs diurno** también se amplificó: la variación promedio noche-día fue de 98,06 USD/MWh en Crucero, 105,07 USD/MWh en Quillota y 75,49 USD/MWh en P. Montt durante 2022. Esto significa que en una sola jornada, el costo marginal podía variar en más de 100 USD/MWh, un rango enorme que ningún mecanismo de estabilización podía absorber completamente.

### 5.4. La respuesta de política y sus efectos

La crisis 2022-2023 fue la gota que colmó el vaso del diseño de mercado anterior. Varias reformas se aceleraron:

- **Aceleración de la transición renovable**: el gobierno del Presidente Boric (2022-) se fijó metas más ambiciosas de cierre de carbón, con hitos en 2025 y 2030 (cierre total).

- **Inversión en almacenamiento**: la Ley 21.505 (2022) creó un marco regulatorio para sistemas de almacenamiento (BESS), y se abrieron licitaciones de proyectos a gran escala.

- **Expansión de la transmisión**: la CNE aceleró los procesos de aprobación de obras troncales, incluyendo la línea HVDC Kimal-Lo Aguirre.

- **Diversificación de combustibles**: Chile exploró activamente la importación de GNL desde otros orígenes (USA principalmente), y la firma de contratos de largo plazo para estabilizar precios.

- **Fortalecimiento de la respuesta de demanda**: la CNMC y el CEN trabajaron en programas para que grandes consumidores (mineras, industria) reduzcan consumo en horas punta, pero estos siguen siendo incipientes.

A pesar de las reformas, la estructura fundamental del mercado spot no cambió: sigue siendo un esquema de despacho centralizado con valorización al costo marginal. Lo que cambió fue la **magnitud y frecuencia de los choques** que el sistema debe absorber, lo que ha elevado la prioridad política del tema.

---

## Parte VI. Desacople norte-centro y el fenómeno del vertimiento

### 6.1. Por qué el norte es barato y el centro es caro

La geografía de generación de Chile está sesgada hacia el norte: las mejores condiciones solares del mundo (el desierto de Atacama, con irradiancia superior a 2.500 kWh/m²/año) y excelentes condiciones eólicas en la costa del norte y del sur. Pero la demanda está concentrada en la zona centro (Santiago, Valparaíso, Rancagua), con centros mineros puntuales en el norte (Antofagasta, Calama) y un centro industrial en el sur (Talcahuano, Coronel, Biobío).

La consecuencia es que la **energía generada en el norte debe recorrer grandes distancias hasta llegar a los centros de consumo**, atravesando un sistema de transmisión que fue diseñado para topologías previas a la revolución renovable. La **línea troncal 2x500 kV** (Cardones-Polpaico, Maitencillo-Pan de Azúcar) tiene capacidad de 1.500-2.500 MW, pero en horas de máxima generación solar el flujo deseado es muy superior. El CEN recurre entonces a **redespachos** que bajan la generación solar del norte, y como esa generación tiene CV cercano a cero, el costo marginal en la zona norte cae dramáticamente (incluso a cero o negativo en el caso de vertimiento explícito).

La métrica del **desacople** se calcula como la diferencia horaria (o mensual promedio) entre el costo marginal de la zona exportadora (norte) y la zona importadora (centro). En condiciones normales de demanda, el desacople Crucero-Quillota es de 5-15 USD/MWh. En horas de congestión severa, puede superar 50 USD/MWh.

### 6.2. El vertimiento como síntoma estructural

El **vertimiento** (curtailment en inglés) es la reducción o apagado de generación renovable que el sistema no puede absorber, sea por congestión de la transmisión o por excedente sobre la demanda. En Chile, el vertimiento se disparó a partir de 2022 con el ingreso masivo de nuevas centrales solares en el norte:

- 2022: ~1.810 GWh vertidos
- 2023: ~2.376 GWh (+31%)
- 2024: ~5.909 GWh (+149%) — 18% de la generación renovable variable
- 2025: ~6.205 GWh (–0,3% vs 2024, +133% vs 2023) — estabilización por BESS

En términos económicos, el estudio de **Ember (octubre 2025)** estima que entre 2022 y mayo de 2025 se dejaron de inyectar 11.900 GWh de generación renovable, equivalente al consumo anual de 2,77 millones de hogares, con pérdidas de ingreso estimadas en **USD 562 millones**. Esta es la dimensión del desperdicio sistémico.

### 6.3. La concentración geográfica del vertimiento

El 76% del vertimiento se concentra en **Antofagasta** (48,3%) y **Atacama** (28,4%). Coquimbo aporta otro 8% y Biobío un 5,1%. Esta concentración no es casualidad: refleja la ubicación de la capacidad solar (Atacama) y la combinación solar-eólica del norte (Antofagasta con BESS, además de solar), junto con la limitada capacidad de evacuación de la red troncal.

El CEN publica mensualmente un informe de **"reducciones de ERV"** que detalla las reducciones aplicadas a cada central, con causa técnica justificada. Esto ha permitido identificar a los **mayores afectados** desde el punto de vista de los generadores: **Enel Green Power Chile** cerró 2024 con 1.027 GWh de vertimiento solar y 236 GWh eólico, el mayor del sistema, seguido por Acciona Energía Chile y Engie Chile. Estos vertimientos tienen impacto directo en la **viabilidad económica** de proyectos renovables: un generador que esperaba producir 1.000 GWh/año y solo puede inyectar 700-800 GWh ve sus ingresos reducidos en 20-30%, lo que deteriora la TIR del proyecto y puede hacer inviables nuevos desarrollos.

### 6.4. Las baterías (BESS) como mitigador parcial

Los sistemas de almacenamiento con baterías (BESS) son la primera línea de defensa contra el vertimiento. La **Ley 21.505 (2022)** creó un marco regulatorio específico para almacenamiento, y desde entonces se han adjudicado proyectos por varios GW de capacidad, principalmente en el norte.

El reporte de **Broker & Trader Energy Chile (enero 2026)** estima que durante 2025, las BESS aportaron 2 TWh al sistema, evitando que el vertimiento potencial (sin BESS) alcanzara 8.200 GWh. Es decir, las baterías redujeron el vertimiento en un **24%**. Es un impacto significativo, pero insuficiente: todavía queda 6.205 GWh vertidos, y el problema seguirá creciendo si no se expande la transmisión o se suman más BESS.

La dinámica económica de las BESS es interesante: en horas de alto vertimiento (donde el precio marginal es cero o negativo), las baterías se cargan "gratis"; en horas de alta demanda, se descargan al precio spot. La diferencia es el spread de arbitraje, que en Chile ha sido atractivo en 2024-2025 por la combinación de precios diurnos bajos y nocturnos altos. La curva de spread nocturno-diurno, que era de 30-50 USD/MWh en 2022, ha subido a 50-80 USD/MWh en algunas horas, lo que hace viables proyectos BESS de 4 horas de duración con un ciclo diario.

### 6.5. La solución estructural: transmisión y electrificación

El vertimiento no es un problema soluble solo con BESS, porque la BESS solo desplaza la energía en el tiempo, no resuelve la congestión espacial. Las dos soluciones estructurales son:

**Ampliación de la transmisión**: el Plan de Expansión aprobado por la CNE en los últimos años incluye varias obras troncales nuevas, pero la más ambiciosa es la **línea HVDC Kimal-Lo Aguirre**: 2.000 km de longitud, 3.000 MW de capacidad, ±600 kV, con una inversión estimada de USD 2.500-3.000 millones. Esta línea conectará la zona de mayor generación solar (Antofagasta-Atacama) directamente con la zona de mayor demanda (Santiago), evitando la congestión del corredor AC existente. Su entrada en operación está prevista para 2029-2030.

**Electrificación de la demanda**: el segundo vector de solución es aumentar la demanda absorbente en el norte. Esto incluye la electrificación de la minería (camiones, chancado, electrolisis para producir hidrógeno verde), la producción de hidrógeno verde para exportación (proyectos en Magallanes y Antofagasta), y la electrificación del transporte (vehículos eléctricos, que pueden cargar preferentemente en horas de bajo costo). Chile tiene oportunidades únicas: la combinación de energía renovable barata, capacidad de electrólisis y cercanía a puertos para exportar hidrógeno/amoníaco verde es una ventaja comparativa global.

Mientras estas soluciones no se materializan plenamente, el vertimiento seguirá siendo un síntoma estructural de la transición energética chilena: la generación renovable ha crecido más rápido que la transmisión y la demanda absorbente, y el sistema paga el costo.

---

## Parte VII. El apagón del 25 de febrero de 2025

### 7.1. La cronología técnica del evento

El apagón del 25 de febrero de 2025 es, hasta la fecha, el mayor blackout del SEN desde su unificación en 2017. La cronología, reconstruida a partir del Estudio de Análisis de Falla del CEN (entregado a la SEC el 19 de marzo de 2025), es la siguiente.

A las 13:35 del 25 de febrero, la empresa **ISA InterChile** (propietaria de la línea) comunicó al CEN que tenía un problema en el módulo de comunicaciones de una de las funciones de protección de la **Línea 2x500 kV Nueva Maitencillo - Nueva Pan de Azúcar** (que conecta Vallenar con Coquimbo, en la región de Atacama). El módulo estaba deshabilitado, pero según la información preliminar, esto no representaba un riesgo operativo porque el sistema de respaldo estaba funcionando.

A las 15:13, sin embargo, el personal de ISA Interchile decidió **reiniciar el módulo de comunicaciones** que tenía problemas, y a continuación intentó **resincronizar la función de protección desactivada**. Este procedimiento se hizo, según el informe del CEN, sin aviso al Coordinador y sin tomar las precauciones establecidas en los manuales del fabricante.

A las 15:15, **la línea de transmisión 2x500 kV se desconectó completamente** del sistema. Esto generó un desbalance instantáneo de potencia que el CEN intentó mitigar con sus recursos de reserva, pero la perturbación fue demasiado severa.

Inmediatamente después, el sistema se dividió en **dos islas eléctricas**:
- **Isla Norte**: desde Arica hasta Coquimbo, aproximadamente el 30% de la demanda.
- **Isla Centro-Sur**: desde Valparaíso hasta Los Lagos, aproximadamente el 70% de la demanda.

Ninguna de las dos islas pudo mantener el balance generación-demanda por sí sola. Las centrales de cada isla comenzaron a desconectarse por sus protecciones de frecuencia, y el resultado fue un **apagón total del SEN** alrededor de las 15:17.

### 7.2. La respuesta del sistema y la recuperación

La recuperación del SEN tomó **más de 7 horas** y requirió una secuencia cuidadosa. Las centrales hidroeléctricas del sur, que estaban operativas gracias a las lluvias de 2024 (que habían recargado los embalses), fueron las primeras en arrancar la reposición. Una central hidroeléctrica puede arrancar y sincronizarse en minutos, a diferencia de las centrales térmicas que pueden tardar horas.

La reposición se hizo isla por isla: primero se energizó la red troncal de la isla centro-sur, luego se fueron sincronizando centrales termoeléctricas disponibles, y finalmente se reconectaron los consumos de manera escalonada. En la isla norte, el proceso fue más lento por la mayor dependencia de generación solar (que a las 22:00 de la noche, en febrero, ya no produce) y térmica.

A la **madrugada del 26 de febrero**, alrededor del 97% de los hogares tenía servicio normalizado. El gobierno levantó el estado de excepción por catástrofe y el toque de queda nocturno que había decretado.

### 7.3. Las causas y las responsabilidades

El **informe del CEN identifica como causa raíz** la actuación incorrecta de las protecciones de la línea 2x500 kV, y como causa inmediata la **falta de coordinación** entre ISA InterChile y el CEN. El Coordinador tiene procedimientos estrictos para coordinar cualquier intervención sobre la red troncal: el agente debe solicitar autorización, y el CEN evalúa el impacto sobre la seguridad sistémica antes de autorizar. En este caso, ISA Interchile no siguió el procedimiento.

Adicionalmente, el informe identifica **deficiencias en la respuesta de los recursos de mitigación**, incluyendo los Esquemas de Desconexión Automática de Carga (EDAC) y la respuesta de algunas centrales generadoras. Esto sugiere que, además de la causa humana, había problemas sistémicos en los esquemas de protección que no respondieron como se esperaba.

En el plano institucional, el evento abrió varios debates:

- **La responsabilidad de ISA InterChile**: la empresa reconoció el error operativo y se enfrenta a sanciones de la SEC y eventuales demandas civiles. La matriz ISA (Interconexión Eléctrica S.A., Colombia) emitió un comunicado reconociendo el incidente.

- **La resiliencia del SEN**: la posibilidad de que un error operativo en una sola línea produzca un apagón total del sistema es un indicador de que las defensas sistémicas (EDAC, reservas, esquemas de defensa) son insuficientes para contingencias de este tipo.

- **La coordinación público-privada**: la existencia de una empresa privada con capacidad de afectar la operación de todo el SEN mediante una decisión operativa local ha renovado el debate sobre el grado de autonomía de los agentes y la capacidad real del CEN de coordinar.

### 7.4. El apagón como evento de pricing dinámico

El apagón ilustra un punto que muchos análisis pasan por alto: el **mercado spot opera sobre la base de un sistema físico estable**. Cuando la frecuencia se pierde, el mercado se suspende. El CEN tiene la potestad de suspender el despacho spot y operar en modo de emergencia, donde las instrucciones son mandatorias y la valorización se hace a costo de racionamiento (650,6 USD/MWh, según la CNE para junio de 2025, que es el costo de la energía no suministrada).

El **costo de racionamiento** es una variable clave: representa el valor que la sociedad asigna a la energía no suministrada, y se usa como techo teórico del costo marginal. En la práctica, el costo marginal rara vez alcanza este valor, pero su sola existencia es una **señal de escasez** que las generadoras pueden internalizar en sus decisiones de inversión.

El evento de febrero de 2025 es, en este sentido, una **lección de teoría de mercados** aplicada a la infraestructura crítica: los precios solo importan cuando el sistema físico funciona. Cuando la red colapsa, todos los precios son cero (no hay transacción) o son el costo de racionamiento (en emergencia).

### 7.5. Implicancias regulatorias del blackout

El apagón ha tenido varias consecuencias regulatorias y operativas:

- **Refuerzo de los EDAC**: la SEC y el CEN han revisado los Esquemas de Desconexión Automática de Carga y han ordenado ajustes para reducir la probabilidad de apagón total.

- **Mayor rigor en las intervenciones sobre la red troncal**: la CNE ha emitido instrucciones para que cualquier intervención sobre líneas de 500 kV o superiores requiera coordinación previa con el CEN, con protocolos reforzados.

- **Discusión sobre la separación vertical de la transmisión**: aunque no se ha avanzado legislativamente, el evento reabrió el debate sobre si el propietario de la línea debería ser distinto del operador (modelo ISO independiente), o si la integración vertical ISA-Transelec es compatible con una coordinación efectiva.

- **Inversión en redundancia**: el apagón aceleró la valoración de proyectos de **refuerzo de redundancia de la red troncal** (segundas líneas, sistemas de almacenamiento para respaldo de emergencia).

- **Coordinación internacional**: la línea atacama-Calingasta (que conecta con Argentina) y otras interconexiones internacionales han cobrado nuevo interés como mecanismo de respaldo mutuo, aunque su capacidad efectiva es limitada.

---

## Parte VIII. Comparativa internacional: el SEN en contexto global

### 8.1. El spectrum de diseños de mercado eléctrico

El SEN chileno no existe en el vacío. Es un caso particular dentro de un espectro global de diseños de mercado que se pueden caracterizar por cuatro dimensiones:

La primera dimensión es la **desintegración vertical**: si generación, transmisión y distribución son empresas separadas o integradas. Chile optó por separación (1982-2007) con segmentos no competitivos (transmisión, distribución regulados) y un segmento competitivo (generación). EE.UU. (PJM) tiene separación similar. Francia tiene integración vertical predominante (EDF).

La segunda dimensión es la **existencia de mercado spot organizado**: si hay un day-ahead subastado públicamente, o si el despacho es centralizado. Europa (EPEX SPOT) tiene day-ahead subastado. USA (PJM, CAISO) tiene day-ahead subastado. Chile tiene despacho centralizado con valorización ex-post. Esta diferencia es crucial: en Chile, el "precio spot" es un concepto ex-post, no un precio descubierto por oferta y demanda en una subasta.

La tercera dimensión es la **profundidad de la contratación a plazo**: si los contratos son predominantes o si el spot gobierna la mayor parte de las transacciones. En Chile, la contratación a plazo es mayoritaria (>70%), pero el spot sigue siendo el precio de referencia. En PJM, la contratación bilateral y los forwards son aún más dominantes (>90%).

La cuarta dimensión es el **grado de integración regional**: si hay acoplamiento entre mercados de países vecinos. Europa tiene PCR/MRC que acopla los day-ahead de 22 países. Sudamérica tiene iniciativas incipientes de integración (SADI en Argentina, conexión a Bolivia, Paraguay, Uruguay) pero Chile no está plenamente integrado con sus vecinos.

### 8.2. El modelo europeo: day-ahead acoplado, intraday continuo, AI Act

El modelo europeo es el más sofisticado del mundo en pricing dinámico de electricidad. El **Single Day-Ahead Coupling (SDAC)** ejecutado por EPEX SPOT y otros operadores acopla las subastas day-ahead de 22 países en un solo proceso. Esto permite que la energía fluya de la zona más barata a la más cara a través de las interconexiones, y produce un precio único en cada zona que refleja el equilibrio agregado europeo más las restricciones de transmisión.

El modelo europeo tiene tres capas:

- **Day-ahead** (D+1): subasta a las 12:00 CET que produce 24 precios horarios para cada zona. El clearing es pay-as-cleared, todos reciben el precio de la última oferta casada.

- **Intraday continuo** (mismo día): los participantes pueden re-casar órdenes hasta minutos antes de la entrega, ajustando sus posiciones.

- **Mercados de balance** (tiempo real): los operadores de red compran y venden energía de reserva para mantener el balance instantáneo.

La **Directiva (UE) 2019/944** define los **contratos de precio dinámico de electricidad** para consumidores, requiriendo que los comercializadores ofrezcan tarifas que reflejen el spot al menos con frecuencia horaria. El **AI Act 2024/1689** clasifica como *high-risk* ciertos sistemas de pricing algorítmico, abriendo un frente regulatorio que Chile aún no aborda.

El contraste con Chile es instructivo: Europa ha **internalizado el pricing dinámico en la regulación del consumidor**, mientras que Chile ha **externalizado la estabilización** mediante el DS 88/2020 y el precio estabilizado. La consecuencia es que el consumidor europeo recibe señales de precio en tiempo real (a través de su tarifa dinámica) y puede responder, mientras que el consumidor chileno paga una tarifa suavizada y no tiene incentivo para modificar su consumo en función del spot.

### 8.3. El modelo USA: LMP nodal, mercados de capacidad, ISO independientes

El modelo estadounidense, nacido con la desregulación de los 90 (FERC Orders 888/889), se organiza en torno a **Independent System Operators (ISO)** y **Regional Transmission Organizations (RTO)** que operan los mercados spot y de capacidad en regiones específicas. Los principales son:

- **PJM** (13 estados del este + DC): el mercado más grande del mundo por volumen. Day-ahead subastado, intraday continuo, y un capacity market (Reliability Pricing Model) que paga a las generadoras por comprometerse a estar disponibles.

- **CAISO** (California): day-ahead e intraday con FTRs (Financial Transmission Rights) para gestionar la congestión. Esquema único de GHG pricing (cap-and-trade).

- **ERCOT** (Texas): un energy-only market, sin mercado de capacidad, con un precio máximo alto (~9.000 USD/MWh) para asegurar inversión. La crisis de Uri 2021 (blackout de Texas) mostró las debilidades de este modelo.

- **NYISO**, **MISO**, **SPP**: variaciones del modelo PJM con особенidades regionales.

El **Locational Marginal Price (LMP)** es la pieza clave: cada nodo del sistema tiene un precio que refleja la energía, la congestión y las pérdidas. Esto es **mucho más granular** que el chileno (que tiene un cMg por barra, no por nodo), pero la lógica es la misma: refleja el coste marginal de suministrar una unidad adicional en un punto específico de la red.

La **diferencia con Chile** es que USA tiene mercados day-ahead **explícitamente subastados** (no un despacho centralizado), lo que da a los generadores incentivos para ofertar estratégicamente. En Chile, los generadores declaran sus costos y el CEN los despacha por mérito, sin puja estratégica. Esta diferencia es **técnica-política** y tiene implicaciones para la eficiencia: el sistema chileno es más robusto ante manipulación de ofertas, pero menos sensible a las preferencias reveladas de los generadores.

### 8.4. El modelo PJM en detalle: capacidad y energía

PJM es el referente mundial. Su diseño combina:

- **Day-ahead market**: subasta hourly a las 10:30 EST para las 24 horas del día siguiente. Productos: energía, reservas de regulación, reservas sincronizadas, reservas no sincronizadas.

- **Real-time market**: recalculación cada 5 minutos del LMP, con base en el despacho real.

- **Capacity market (RPM)**: subasta anual donde las generadoras ofertan capacidad (MW) y reciben pagos por comprometerse a estar disponibles en condiciones de escasez. El precio de capacidad lo determina la intersección de oferta y demanda, y ha llegado a superar USD 250/MW-día en algunos períodos.

- **Financial Transmission Rights (FTRs)**: instrumentos financieros que permiten a los participantes cubrirse contra la congestión de la red, comprando derechos de transmisión entre nodos.

Este diseño crea incentivos económicos para: invertir en capacidad firme (porque el capacity market paga por estar disponible, no por producir), gestionar el riesgo de congestión (a través de FTRs), y ofertar estratégicamente en el day-ahead. Es más complejo que el chileno, pero también más eficiente en términos de señales de inversión.

### 8.5. El caso ERCOT (Texas) y la crisis de Uri 2021

ERCOT es un caso único por su condición de **energy-only market** en un sistema aislado (sin interconexiones significativas con otros estados). El precio de la energía puede alcanzar 9.000 USD/MWh, lo que en teoría debería atraer inversión en capacidad. Sin embargo, durante la tormenta **Uri** (febrero 2021), el sistema falló catastróficamente: las centrales térmicas se congelaron, la red colapsó, y millones de personas quedaron sin electricidad durante días. Los precios spot llegaron a 9.000 USD/MWh durante horas, lo que generó facturas astronómicas para clientes con tarifas variables.

El caso ERCOT es un **counter-argument al energy-only market puro**: en sistemas con dependencia de combustibles fósiles y climas extremos, los precios de escasez no son suficientes para garantizar la resiliencia. Chile ha aprendido de Uri y ha mantenido el pago por potencia como complemento al mercado spot, lo que es una diferencia importante con el modelo Texas.

### 8.6. El modelo nórdico: hidrología dominante y acoplamiento europeo

El mercado nórdico (Noruega, Suecia, Finlandia, Dinamarca) es particularmente relevante para Chile por su **componente hidroeléctrica dominante**. El Nord Pool Spot opera el day-ahead acoplado de la región, y los precios reflejan fuertemente la hidrología esperada: en años húmedos, los precios son bajos; en años secos, suben significativamente.

La **hidrología variable** es un factor que la operación hidroeléctrica de cualquier sistema (incluido el chileno) debe gestionar. Los nórdicos usan **modelos estocásticos de aportes hídricos** similares a los del CEN, y sus embalses funcionan como baterías naturales a escala estacional. Chile tiene embalses más pequeños en términos relativos, y la proporción hidroeléctrica está decreciendo con el ingreso masivo de solares, lo que cambia el perfil de riesgos.

### 8.7. Lo que Chile puede aprender de los demás

Cuatro lecciones emergen de la comparativa internacional.

Primera: el **mercado day-ahead subastado** tiene ventajas de eficiencia sobre el despacho centralizado, pero requiere un diseño de ofertas robusto y supervisión anticolusión. Chile podría evolucionar hacia un day-ahead subastado, pero esto requeriría un cambio institucional significativo.

Segunda: el **mercado de capacidad** es esencial para garantizar la seguridad de suministro en sistemas con alta dependencia de combustibles fósiles. Chile lo ha entendido y mantiene el pago por potencia, aunque podría robustecerlo con señales de escasez más explícitas.

Tercera: la **integración regional** (acoplamiento de mercados day-ahead, interconexiones físicas) reduce la volatilidad y mejora la resiliencia. Chile está aislado del sistema argentino en la práctica, y los proyectos de interconexión con Perú, Bolivia y Argentina han avanzado poco.

Cuarta: la **estabilización tarifaria** para clientes finales (DS 88/2020) es un instrumento útil para la política pública, pero **enmascara las señales de precio** que el mercado necesita para la inversión y la respuesta de demanda. La duración de este mecanismo (hasta 2027) y su eventual reemplazo son las preguntas regulatorias más importantes de la próxima década.

---

## Parte IX. Regulación, contratos y el futuro del SEN

### 9.1. La arquitectura legal del sector eléctrico chileno

El sector eléctrico chileno se rige por más de 30 cuerpos legales entre leyes, reglamentos y normas técnicas. La columna vertebral es el **DFL N°4 de 2006** (Ley General de Servicios Eléctricos, refundido), que ha sido modificado más de 15 veces desde su dictación. Las modificaciones más relevantes para entender el mercado spot son:

- **Ley 19.940 (2004)**: introdujo la separación del segmento de transmisión y el peaje único.
- **Ley 20.018 (2005)**: estableció las licitaciones de suministro a clientes regulados.
- **Ley 20.257 (2008) y Ley 20.805 (2015)**: introdujeron y perfeccionaron los **objetivos de ERNC** (20% al 2025, 60% al 2035, 100% al 2050 con la meta actualizada de carbono-neutralidad al 2050).
- **Ley 20.936 (2016)**: creó el Coordinador Eléctrico Nacional, reemplazó los CDEC, y modernizó el sistema de transmisión (introdujo el sistema de planificación de transmisión troncal).
- **Ley 21.185 (2019)**: mecanismo transitorio de estabilización tarifaria.
- **DS 88 (2020)**: regulación del precio estabilizado.
- **Ley 21.220 (2020)**: modificaciones al mercado de clientes libres y a la figura del gestor comercial.
- **Ley 21.305 (2021)**: eficiencia energética.
- **Ley 21.505 (2022)**: marco regulatorio para sistemas de almacenamiento.
- **Ley 21.622 (2024)**: licitaciones de almacenamiento, ajustes al sistema de transmisión.

Esta cascada normativa refleja la **dinámica de un sector en transición**: cada ley corrige una deficiencia del diseño anterior, pero el diseño subyacente (mercado spot con valorización al costo marginal + licitaciones reguladas + pago por potencia + estabilización) se ha mantenido esencialmente intacto desde 2005.

### 9.2. Las licitaciones reguladas y la formación del precio de largo plazo

Las **licitaciones reguladas** son el mecanismo mediante el cual las distribuidoras contratan suministro a largo plazo para abastecer a los clientes regulados. La CNE define las bases (volumen por bloque, período de suministro, precio de reserva, condiciones técnicas), y las generadoras ofertan. El precio adjudicado es el precio de mercado para ese período.

La **licitación 2023/01**, adjudicada en mayo de 2024, es la más reciente y significativa: 3.600 GWh/año adjudicados a Enel Generación Chile a un precio promedio de **56,68 USD/MWh**, con suministro a partir de 2027 y 2028. Este precio es **inferior al costo marginal spot actual** (que ronda 50-90 USD/MWh en condiciones normales), lo que refleja la expectativa del mercado de que los precios spot se mantendrán bajos o caerán con la mayor entrada renovable.

La **interpretación económica** de este resultado es importante: las generadoras están dispuestas a vender a 56,68 USD/MWh porque (a) las nuevas centrales renovables tienen CV cercano a cero, (b) el contrato les da cobertura de precio, y (c) la demanda cautiva de los clientes regulados es valiosa. Para los clientes regulados, la ventaja es clara: un precio predecible y razonable a 10 años vista. Para el sistema en su conjunto, la lección es que **los contratos a largo plazo pueden ser más baratos que el spot promedio** si la generación contratada es renovable y tiene CV bajo.

### 9.3. El mercado de clientes libres y la competencia

El **mercado de clientes libres** (>0,3 MW) opera por contratos bilaterales, sin intervención del CEN en la formación del precio. Los clientes negocian directamente con generadores o comercializadores, y los precios reflejan las condiciones particulares de cada contrato (volumen, perfil de consumo, duración, garantías, ubicación física).

Históricamente, los precios libres han sido **inferiores a los regulados** en 10-20%, lo que refleja la capacidad de negociación de los grandes clientes. La rebaja del límite a 0,3 MW ha abierto este mercado a clientes medianos, y la expectativa es que la diferencia se mantenga o amplíe.

El **riesgo** de este mercado es la **asimetría de información**: las grandes empresas tienen equipos técnicos y legales para negociar, mientras que los clientes medianos pueden quedar en desventaja. La **Resolución N°58/2024** incluye medidas de transparencia, pero la supervisión efectiva es un desafío regulatorio.

### 9.4. El futuro de la descarbonización y la carbono-neutralidad

Chile se ha comprometido a alcanzar la **carbono-neutralidad al 2050**, con metas intermedias de **60% de generación ERNC al 2030** y **100% al 2050** (excluyendo la descarbonización del último 10% del carbón que se ha proyectado cerrar antes de 2040). Estas metas son ambiciosamente más estrictas que las de la mayoría de los países de la OCDE.

El **plan de cierre de centrales a carbón** se ha acelerado: el gobierno del Presidente Boric (2022-) ha establecido el cierre total antes de 2030 para las centrales que no tienen sistemas de captura, con hitos parciales en 2025. Esto significa que, en los próximos 5 años, Chile retirará alrededor de 5.000 MW de capacidad a carbón, que actualmente representa aproximadamente el 15% de la generación.

La **transición tiene costos y riesgos**. Por un lado, la entrada masiva de renovables (solar, eólica, BESS) y la electrificación de la demanda pueden hacer que el costo marginal promedio del SEN **caiga** a niveles de 30-40 USD/MWh en 2030-2035, según proyecciones de la CNE. Por otro lado, los **momentos de transición** (horas con poca renovable y poca hidro) serán los más difíciles, y la disponibilidad de **respaldo firme** (GNL, hidrógeno verde, geotermia) será crítica.

La **reforma de la planificación de la transmisión** es tan importante como la generación. El Plan de Expansión 2024-2030 incluye obras por más de USD 5.000 millones, pero el cuello de botella regulatorio (consultas, oposiciones, licitaciones) ha retrasado muchas obras. La CNE está implementando reformas para acelerar los procesos, pero los resultados se verán gradualmente.

### 9.5. El rol del hidrógeno verde

Chile ha apostado fuerte por el **hidrógeno verde** como vector de descarbonización y oportunidad exportadora. El país tiene condiciones únicas: recursos renovables abundantes y baratos en el norte (solar en Atacama, eólico en Magallanes), puertos de exportación en ambas costas, y acuerdos de demanda internacional (especialmente de Europa y Asia).

El **hidrógeno verde** se produce por electrólisis del agua usando electricidad renovable. En Chile, los **proyectos de hidrógeno verde** están en distintas etapas de desarrollo, con una meta declarada de **25 GW de electrólisis al 2030** (la Estrategia Nacional de Hidrógeno Verde). Si esta meta se cumple, la demanda adicional de electricidad para electrólisis podría absorber el vertimiento estructural y, eventualmente, **transformar al SEN en un sistema dominado por la demanda industrial** más que por la residencial.

El **desafío** es que los proyectos de hidrógeno verde aún no son económicamente competitivos sin subsidios, y la curva de aprendizaje de la electrólisis es incierta. Chile está usando **licitaciones de terreno fiscal** con compromisos de inversión para catalizar el sector, pero el despegue real dependerá de la demanda internacional y de la reducción de costos de electrólisis.

### 9.6. La integración con vehículos eléctricos

La **electrificación del transporte** es otro vector de demanda futura. Chile tiene alrededor de 100.000 vehículos eléctricos a 2025 (3% del parque), y la meta declarada es llegar a 100% de ventas de vehículos ligeros eléctricos al 2035.

Los **vehículos eléctricos (VEs)** son consumidores flexibles por naturaleza: pueden cargar en horas de bajo costo marginal (mediodía, madrugada) sin afectar al usuario. Bien gestionados, los VEs son **demanda absorbente** que reduce el vertimiento y mejora la utilización de las redes. Chile está empezando a desarrollar **tarifas de carga inteligente** para VEs, y las empresas distribuidoras están instalando infraestructura de medición y control.

La integración con VEs es, sin embargo, técnicamente compleja: requiere comunicación bidireccional con los vehículos, gestión de carga en el lado del consumidor, y modelos tarifarios que incentiven la carga en horas de bajo costo. Es un área en pleno desarrollo, y los estándares internacionales (ISO 15118) están convergiendo.

### 9.7. El futuro del pricing dinámico en Chile

El **precio estabilizado del DS 88/2020** vence en diciembre de 2027. Lo que ocurra después es la pregunta regulatoria más importante del sector. Las opciones son:

- **Renovación del PE** con ajustes: extender el mecanismo de estabilización con ajustes en la fórmula, posiblemente con bandas más estrechas y ajustes más frecuentes.

- **Migración a tarifas dinámicas regulatorias**: introducir tarifas de cliente regulado que reflejen el spot con frecuencia horaria, similar a la Directiva 2019/944 de la UE. Esto requeriría un despliegue masivo de medidores inteligentes y un cambio cultural significativo.

- **Híbrido**: una tarifa base con componentes variables por hora o por bloque, donde una fracción refleja el spot y el resto es fija.

Cualquiera sea la opción, el **principio subyacente** es el mismo: las señales de precio son necesarias para que la demanda responda, y el sistema necesita que responda para integrar renovables masivamente. La pregunta no es si Chile tendrá pricing dinámico en el cliente final, sino cuándo y cómo.

---

## Parte X. Glosario, bibliografía y autoevaluación

### 10.1. Glosario técnico

**Account Difference**: mecanismo de compensación entre el precio de nudo proyectado y el costo marginal real. Puede generar saldos pendientes a favor o en contra de generadoras y distribuidoras.

**BESS (Battery Energy Storage System)**: sistema de almacenamiento de energía basado en baterías (generalmente de ion-litio). Permite almacenar energía y liberarla en otro momento, arbitrar precios y prestar servicios complementarios.

**Barra**: punto del sistema de transmisión donde se calcula el costo marginal. Típicamente coincide con una subestación troncal (e.g., Crucero 220, Quillota 220).

**Capacidad instalada**: potencia máxima que una central puede generar en condiciones nominales. No debe confundirse con **generación real** (la energía efectivamente producida en un período).

**Cargo único**: peaje regulado por el uso del sistema de transmisión troncal. Se cobra a la demanda y se paga a los propietarios de líneas troncales.

**CNE**: Comisión Nacional de Energía. Organismo técnico regulador del sector eléctrico chileno.

**CEN (Coordinador Eléctrico Nacional)**: organismo técnico independiente que coordina la operación del SEN. Creado en 2017, reemplazó a los antiguos CDEC.

**Costo marginal (cMg)**: coste variable de producir una unidad adicional de energía en una barra y hora dadas. Concepto físico-operativo, calculado por el CEN.

**CDEC (Centro de Despacho Económico de Carga)**: organismos predecesores del CEN. Operaban el SIC y el SING por separado hasta 2017.

**CV (Costo Variable)**: costo de combustible + costo variable de operación y mantenimiento (no incluye costo de inversión). Es la base del orden de mérito.

**DS 88/2020**: Decreto Supremo que regula el precio estabilizado de la energía para clientes regulados. Vigente hasta diciembre de 2027.

**EDAC (Esquema de Desconexión Automática de Carga)**: sistema de protección que desconecta automáticamente bloques de consumo predefinidos cuando la frecuencia cae por debajo de umbrales críticos, para evitar colapso sistémico.

**ERV (Energía Renovable Variable)**: generación renovable cuya producción depende de condiciones meteorológicas (solar, eólica, mini-hidro de pasada). Se distingue de la generación renovable gestionable (hidro de embalse, biomasa, geotermia).

**Factor de planta**: relación entre la energía efectivamente generada en un período y la energía que se habría generado si la central operara a capacidad instalada todo el tiempo. Para solar en Atacama, 25-30%; para eólica en el sur, 30-40%; para térmica a gas, 50-70%.

**FTR (Financial Transmission Right)**: instrumento financiero para cubrirse del riesgo de congestión en sistemas nodales. Existe en PJM, NYISO, MISO. No existe en Chile.

**Licitación regulada**: proceso competitivo administrado por la CNE mediante el cual las distribuidoras contratan suministro a largo plazo. El precio adjudicado es el precio de mercado para el período.

**LMP (Locational Marginal Price)**: precio nodal en sistemas USA, que refleja energía + congestión + pérdidas (+ GHG en California). En Chile, el concepto equivalente es el cMg por barra, con una granularidad menor.

**MCP (Market Clearing Price)**: precio único de equilibrio en una subasta (day-ahead europea, PJM). En Chile, el equivalente funcional es el cMg calculado por el CEN.

**PMGD (Pequeños y Medios de Generación Distribuida)**: generadores renovables de menos de 9 MW conectados a redes de distribución. Trato especial en la normativa.

**Potencia de suficiencia**: contribución de cada central a la capacidad firme del sistema, calculada con modelos probabilísticos. Menor para renovables variables que para térmicas o hidro de embalse.

**PPAs (Power Purchase Agreements)**: contratos bilaterales de largo plazo entre generadores y clientes. Comunes en el sector libre chileno.

**Precio de nudo (PN)**: precio regulado que las distribuidoras pagan a las generadoras por la energía a clientes regulados. Fijado semestralmente por la CNE.

**Precio estabilizado (PE)**: precio que efectivamente paga el cliente regulado, regulado por el DS 88/2020. Suaviza la volatilidad del PN.

**RE N°58/2024 y N°13/2025**: resoluciones que rebajaron el límite de potencia para ser cliente libre de 0,5 MW a 0,3 MW.

**RTD (Real-Time Dispatch)**: optimización del despacho en tiempo real, ejecutada por el CEN cada 5-15 minutos.

**SIC (Sistema Interconectado Central)**: sistema eléctrico histórico del centro-sur de Chile. Unificado con el SING en el SEN desde 2017.

**SING (Sistema Interconectado del Norte Grande)**: sistema eléctrico histórico del norte de Chile, dominado por la gran minería. Unificado con el SIC en el SEN desde 2017.

**Spot (mercado)**: transacciones de energía valorizadas al costo marginal ex-post. En Chile, no es un mercado de ofertas sino un esquema de transferencias.

**SSCC (Servicios Complementarios)**: servicios de regulación de frecuencia, reserva, control de voltaje, EDAC, necesarios para la operación segura del sistema.

**TDLC (Tribunal de Defensa de la Libre Competencia)**: entidad que vela por la libre competencia en Chile. Emitió el Informe N°33/2024 favorable a la rebaja del límite de cliente libre.

**Vertimiento (curtailment)**: reducción o apagado de generación renovable que el sistema no puede absorber, sea por congestión o por excedente.

### 10.2. Bibliografía y fuentes para profundizar

**Documentos oficiales del CEN**

- Coordinador Eléctrico Nacional, *Costo Marginal Real*. https://www.coordinador.cl/mercados/graficos/costos-marginales/costo-marginal-real/
- Coordinador Eléctrico Nacional, *Reporte Energético SEN mensual*. Disponible en https://www.coordinador.cl/mercados/documentos/transferencias-economicas/costo-marginal-real/
- Coordinador Eléctrico Nacional, *Informe de Monitoreo de la Competencia en el Mercado Eléctrico 2024*. https://www.coordinador.cl/wp-content/uploads/2025/04/Informe-Monitoreo-2024.pdf
- Coordinador Eléctrico Nacional, *Estudio de Análisis de Falla - Apagón 25-feb-2025*. https://www.coordinador.cl/novedades/coordinador-electrico-nacional-entrega-a-la-sec-informe-sobre-el-apagon-del-25-de-febrero/

**Documentos de la CNE**

- Comisión Nacional de Energía, *Fijaciones Precio de Nudo 2025*. https://www.cne.cl/es/tarificacion/electrica/precio-nudo-promedio/fijaciones-2025-2/
- Comisión Nacional de Energía, *Licitación de suministro eléctrico 2023/01*. https://www.cne.cl/prensa/prensa-2024/5-mayo-de-2024/licitacion-de-suministro-electrico-a-clientes-regulados-alcanzo-precio-de-56679us-mwh/
- Comisión Nacional de Energía, *Reporte Energético Financiero*. Vol. 33 (jul-2025). https://www.cne.cl/wp-content/uploads/2025/07/RT_Financiero_v20252T.pdf

**Documentos del Ministerio de Energía**

- Ministerio de Energía, *Reporte de Mercados Eléctricos*. Varios números 2022-2024. https://energia.gob.cl/
- Ministerio de Energía, *Estrategia Nacional de Hidrógeno Verde*. https://energia.gob.cl/h2v

**Documentos académicos y técnicos**

- ACENOR, *Petróleo en el Sistema Interconectado de Chile*, febrero 2022. https://acenor.cl/
- Universidad de Chile, *Mercado Eléctrico Chileno y generadores de ERNC: análisis de las Leyes 20.805 y 20.936*. https://repositorio.uchile.cl/
- Systep, *Reporte Sector Eléctrico*. https://systep.cl/

**Análisis internacional y de mercado**

- Ember, *Reducing curtailment in Chile*, octubre 2025. https://www.pv-magazine-latam.com/2025/10/06/un-informe-de-ember-revela-los-altos-costos-del-vertimiento-de-renovables-en-chile-y-propone-como-reducirlos/
- ACERA, *Columna: Implosión del mercado eléctrico de Chile 2022*. https://www.acera.cl/columna-implosion-del-mercado-electrico-de-chile-2022/
- Broker & Trader Energy Chile, *Reporte Mensual de Vertimiento*. Citado en https://www.reporteminero.cl/noticia/noticias/2026/01/vertimiento-renovables-chile-2025
- EPEX SPOT, *Basics of the Power Market*. https://www.epexspot.com/en/basicspowermarket
- PJM, *Market Information / Data Viewer*. https://dataviewer.pjm.com/

**Prensa especializada**

- *Pulso / La Tercera*: seguimiento del sector eléctrico chileno.
- *Revista Electricidad* (https://www.revistaei.cl/).
- *El Mercurio de Valparaíso* (análisis energético).
- *Diario Financiero*.

**Eventos académicos clave**

- **IEEE PES General Meeting** y **IEEE PES T&D Conference**: papers sobre mercados eléctricos internacionales.
- **IAEE (International Association for Energy Economics)**: conferencias anuales con papers sobre mercados eléctricos.
- **Seminarios CEN-CNE**: presentaciones técnicas sobre el mercado chileno.

### 10.3. Preguntas de autoevaluación

Para verificar la comprensión profunda de los temas cubiertos, las siguientes preguntas pueden servir como punto de partida para autoestudio:

**Conceptuales básicas**

1. ¿Por qué la electricidad no es un commodity almacenable a escala de red, y qué consecuencias económicas tiene esto?
2. ¿Qué diferencia al mercado spot chileno de un day-ahead europeo como EPEX SPOT?
3. ¿Cuál es la diferencia entre costo marginal, precio spot, precio de nudo y precio estabilizado?
4. ¿Por qué el SEN tiene un precio por barra y no un precio único nacional?
5. ¿Qué rol juegan los Pequeños Medios de Generación Distribuida (PMGD) en el vertimiento?

**Operativas intermedias**

6. ¿Cómo se forma el orden de mérito en el SEN? ¿Cuáles son los CV típicos por tecnología?
7. ¿Qué mecanismos usa el CEN para balancear la oferta y la demanda en tiempo real?
8. ¿Cómo se liquidan las transferencias de energía entre generadores?
9. ¿Qué es la potencia de suficiencia y cómo se diferencia de la capacidad instalada?
10. ¿Cómo se determina el precio de nudo y por qué se publica semestralmente?

**Aplicadas avanzadas**

11. ¿Por qué el desacople Crucero-Quillota se amplifica en horas de máxima generación solar?
12. ¿Qué condiciones técnicas y regulatorias habrían evitado el apagón del 25-feb-2025?
13. ¿Cómo explicarías la diferencia de USD 562M en vertimiento perdido entre 2022 y 2025?
14. ¿Por qué el DS 88/2020 enmascara señales de precio a los hogares, y qué implicancias tiene?
15. ¿Qué lecciones del apagón de Uri 2021 (Texas/ERCOT) son aplicables al diseño del SEN?

**Críticas y prospectiva**

16. ¿Qué trade-off enfrenta Chile entre estabilización tarifaria (DS 88/2020) y respuesta de demanda?
17. ¿Cómo puede el hidrógeno verde transformar la geografía de precios del SEN?
18. ¿Por qué la línea HVDC Kimal-Lo Aguirre es la obra más importante del sistema en la próxima década?
19. ¿Qué reformas regulatorias serían necesarias para migrar a tarifas dinámicas de cliente final?
20. ¿Cuáles son los tres riesgos sistémicos más importantes del SEN en 2026-2030?

### 10.4. Itinerario de profundización sugerido

Si después de leer este documento quieres profundizar en algún tema, el orden recomendado es:

**Para entender la teoría económica del mercado eléctrico**: empieza por el libro de **Steven Stoft** *Power System Economics* (IEEE Press / Wiley, 2002), que es la referencia canónica en diseño de mercados eléctricos. Complementa con **Daniel Kirschen y Goran Strbac** *Fundamentals of Power System Economics* (Wiley, 2004).

**Para entender el caso chileno**: la tesis de **Luis Llanos** en la Universidad de Chile (2024), accesible en https://www.dii.uchile.cl/, ofrece una visión comprehensiva del mercado chileno. Los reportes mensuales del CEN son indispensables para entender la operación real.

**Para entender la crisis 2022-2023**: el **Reporte Systep de abril 2022** y el **estudio ACENOR** son fuentes primarias. Complementa con la cobertura de prensa de *La Tercera* y *Diario Financiero*.

**Para entender el apagón de febrero 2025**: el **Estudio de Análisis de Falla del CEN** (entregado a la SEC en marzo 2025) es la fuente autorizada. Complementa con la cobertura de *El País*, *DW Español* y la presentación del CEN ante el Congreso (abril 2025).

**Para entender el vertimiento y la transición**: el **informe Ember de octubre 2025** es la referencia más reciente. Complementa con los reportes mensuales de **Broker & Trader Energy Chile**.

**Para entender la comparativa internacional**: los reportes de **ENTSO-E** (mercado europeo), los **State of the Market reports del PJM**, y los **Annual reports del ERCOT** son fuentes primarias. Los artículos académicos en *Energy Policy*, *The Energy Journal* y *Utilities Policy* ofrecen el marco teórico comparado.

### 10.5. Nota final

Este estudio es un mapa de entrada al mercado spot eléctrico chileno. No sustituye la lectura directa de los documentos primarios del CEN, la CNE y el Ministerio de Energía, que son las fuentes autorizadas. Tampoco sustituye el juicio crítico del lector: las cifras pueden haber cambiado entre la fecha de este documento y su lectura, y las interpretaciones regulatorias evolucionan constantemente. Lo que permanece constante es la **lógica del sistema**: un mercado físicamente restringido, económicamente regulado, políticamente sensible, y técnicamente sofisticado. Dominar esta lógica es el primer paso para operar en él, regularlo, o simplemente entender cómo funciona el interruptor de la luz.

---

**Fin del estudio académico. Versión de referencia: julio 2026.**
