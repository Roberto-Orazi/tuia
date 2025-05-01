# Resumen de definiciones clave de Data Warehouse

## Unidad 1: Data Warehouse

- **Datos**: Partículas de conocimiento que llegan al observador desde la realidad que está sucediendo, reflejo de una
  realidad que ya sucedió.

- **Información**: Conjunto de datos que interesan a un observador por un motivo específico, para un fin determinado, en
  una circunstancia dada.

- **Conocimiento**: Mezcla de experiencia, valores, información y "know-how" que sirve como marco para incorporar nuevas
  experiencias e información, útil para la acción.

- **Sistema de Información**: Conjunto de elementos orientados al tratamiento y administración de datos e información
  para colaborar con los objetivos de una organización.

- **Data Warehouse (DW)**: Repositorio de datos específicamente construido y mantenido para responder a necesidades de
  información estratégica, táctica y operativa. Representa la única fuente de datos necesaria para construir sistemas
  que brinden soporte a la toma de decisiones.

- **Data Warehousing (DWH)**: Procesos necesarios para la extracción, limpieza, transformación, control y carga de datos
  para mantenerlos en un Data Warehouse.

- **ETL**: Extract, Transform, Load. Procesos para extraer, transformar y cargar datos.

- **Enterprise Data Warehouse (EDW)**: DW centralizado diseñado para responder a las necesidades de BI de toda la
  organización con un modelo de negocio global.

- **Data Mart (DM)**: Una "partición" del DW empresarial orientada a un departamento o tema específico.

- **Operational Data Store (ODS)**: Base de datos integrada de datos operacionales recientes para decisiones tácticas u
  operativas.

- **DW Virtual (DWV)**: Permite ejecutar consultas directamente sobre bases operacionales sin afectar su rendimiento.

## Unidad 2: OLAP

- **OLAP**: Procesamiento Analítico En Línea. Enfoque para responder consultas analíticas multidimensionales
  rápidamente, permitiendo extraer y ver datos desde diferentes perspectivas.

- **Medidas/Métricas**: Valores que permiten evaluar, medir o comparar aspectos del negocio (ventas, márgenes, costos).

- **Tipos de medidas**:
  - **Aditivas**: Se pueden agregar (sumar) uniformemente en todas las dimensiones.
  - **Semiaditivas**: Se suman pero no uniformemente en todas las dimensiones.
  - **No aditivas**: No se suman (índices, ratios, porcentajes).

- **Dimensión**: Atributos que proporcionan contexto a las mediciones, organizan y categorizan los datos para análisis.

- **Jerarquía**: Estructura dentro de dimensiones que organiza datos en niveles de detalle (Año > Trimestre > Mes >
  Día).

- **Multidimensionalidad**: Proceso de diseño y construcción de un modelo dimensional a partir de una base de datos
  transaccional.

- **Tabla de Hechos/Fact Table**: Colección de medidas relacionadas con dimensiones, representadas por claves o IDs que
  conectan con tablas de dimensión.

- **Modelo Estrella**: Estructura con una tabla central de hechos rodeada por tablas de dimensiones.

- **Modelo Copo de Nieve**: Extensión del modelo estrella donde las dimensiones están normalizadas en múltiples tablas
  relacionadas.

- **Dimensiones conformadas**: Dimensiones estandarizadas que pueden utilizarse en varias tablas de hechos, manteniendo
  consistencia.

- **ROLAP, MOLAP, HOLAP**: Implementaciones de OLAP (Relacional, Multidimensional e Híbrida respectivamente).

## Unidad 3: Explotación de Datos

- **Data Lake**: Almacén que guarda datos en formato nativo y a escala, sin procesar, estructurados o no estructurados.

- **Data Mining**: Herramientas que predicen tendencias y comportamientos mediante técnicas para descubrir patrones
  ocultos.

- **Business Intelligence (BI)**: Transformación de datos empresariales en conocimiento para obtener ventaja
  competitiva. Incluye aplicaciones, infraestructura y prácticas para mejorar decisiones.

- **Data Quality**: Características de datos de alta calidad y procesos para medir/mejorar su calidad.

## Unidad 4: NoSQL

- **NoSQL**: Sistemas de gestión de datos que no siguen el modelo relacional y no usan SQL como lenguaje principal (Not
  only SQL).

- **Principios de sistemas distribuidos**:
  - **CAP**: Un sistema distribuido solo puede garantizar dos de tres: Consistencia, Disponibilidad y Tolerancia a
    particiones.
  - **ACID**: Propiedades de transacciones (Atomicidad, Consistencia, Aislamiento, Durabilidad).
  - **BASE**: Principios alternativos (Básicamente Disponible, Estado Suave, Consistencia Eventual).

- **Tipos de NoSQL**:
  - **Key-Value**: Almacenan datos en estructura clave-valor (Redis, Riak).
  - **Document**: Almacenan documentos (MongoDB, CouchDB).
  - **Graph**: Almacenan datos en formato de grafos (Neo4j).
  - **Column Families**: Almacenan datos en columnas (Cassandra).

## Unidad 5: Datos de otras fuentes

- **Datos estructurados**: Tienen longitud, formato y tamaño definidos (tablas, hojas de cálculo, BBDD relacionales).

- **Datos no estructurados**: Sin formato específico (PDF, correos, multimedia).

- **Datos semiestructurados**: Mezcla de los anteriores, con cierta organización en sus metadatos (XML, JSON).

- **BBDD Documentales**: Variante NoSQL que almacena registros como unidades autónomas de información en documentos.

Estas son las definiciones clave del PDF, enfocadas en los conceptos fundamentales sin elementos históricos o
contextuales irrelevantes.


Basándome en las preguntas del examen que me has compartido, te proporcionaré respuestas completas para esas preguntas
específicas:

# RESPUESTAS PARA EL EXAMEN

## 1) Describa qué es una tabla de hecho y qué elementos se pueden encontrar en dicha tabla

Una tabla de hecho (o Fact Table) es la tabla central en un modelo dimensional (como el modelo estrella o copo de nieve)
que contiene las medidas o métricas del negocio y las claves foráneas que conectan con las tablas de dimensiones. Es el
componente principal donde se almacenan los datos cuantitativos para su análisis.

**Elementos que se pueden encontrar en una tabla de hecho:**

- **Medidas o métricas numéricas**: Valores cuantitativos que se pueden agregar (sumar, promediar, etc.) como ventas,
  cantidades, importes, márgenes, etc.
- **Claves foráneas**: Referencias a las tablas de dimensión que proporcionan el contexto para las medidas (ID_Cliente,
  ID_Producto, ID_Fecha, ID_Sucursal, etc.)
- **Clave primaria compuesta**: Generalmente formada por la combinación de todas o algunas de las claves foráneas.
- **Medidas derivadas**: Cálculos precomputados basados en otras medidas (como porcentajes o ratios).
- **Fecha/hora de la transacción**: Registro temporal de cuándo ocurrió el hecho.
- **Flags o indicadores**: Campos booleanos que señalan estados específicos.

Estas tablas representan eventos o transacciones del negocio y son el objeto de análisis en un Data Warehouse. La tabla
de hecho no debe contener datos descriptivos o textuales extensos, esa información pertenece a las dimensiones.

## 2) Indicar las principales diferencias entre medidas y dimensiones (defina cada una y mencione algunas diferencias)

**Medidas (o métricas):**
- Son valores numéricos que representan aspectos cuantitativos del negocio que se pueden medir.
- Se almacenan en las tablas de hechos.
- Son los valores que se analizan, agregan y calculan (suman, promedian, cuentan).
- Ejemplos: importe de venta, cantidad vendida, costo, margen, número de transacciones.

**Dimensiones:**
- Son atributos que proporcionan contexto a las medidas y permiten analizar los datos desde diferentes perspectivas.
- Se almacenan en tablas de dimensiones separadas que se relacionan con la tabla de hechos.
- Contienen atributos descriptivos y jerárquicos que permiten filtrar, agrupar y etiquetar datos.
- Ejemplos: tiempo (fecha), producto, cliente, ubicación, empleado.

**Diferencias clave:**
1. **Naturaleza de los datos**: Las medidas son numéricas y cuantitativas; las dimensiones son descriptivas y
   categóricas.
2. **Propósito**: Las medidas responden "cuánto" (valores a analizar); las dimensiones responden "quién, qué, cuándo,
   dónde, cómo" (contexto del análisis).
3. **Operaciones**: Las medidas se agregan (suman, promedian); las dimensiones se usan para filtrar y agrupar.
4. **Almacenamiento**: Las medidas están en la tabla de hechos; las dimensiones tienen sus propias tablas.
5. **Cardinalidad**: Las dimensiones suelen tener menor cardinalidad (número de valores únicos) que las filas en la
   tabla de hechos.

## 3) ¿Cuál es la clave de la dimensión tiempo y de qué tipo de datos es?

La clave de la dimensión tiempo suele ser un número entero compuesto que representa la fecha en formato AAAAMMDD (año,
mes, día). Por ejemplo, el 23 de abril de 2025 se representaría como 20250423.

**Tipo de dato**: Es un valor entero (INTEGER), no un campo de tipo fecha nativo y NO es auto-incremental.

Esta representación ofrece varias ventajas:
- Facilita la ordenación cronológica natural
- Permite operaciones aritméticas directas
- Mejora el rendimiento de las consultas
- Simplifica las comparaciones de fechas
- Mantiene consistencia en el formato de fechas

Este enfoque permite convertir una fecha en formato DATE a un INTEGER en el formato específico, lo que resulta más
eficiente para consultas en un entorno de Data Warehouse.

## 4) ¿Por qué no puede existir una cardinalidad de muchos a muchos entre una tabla Fact y una tabla de Dimensiones?

No puede existir una cardinalidad muchos a muchos entre una tabla Fact y una tabla de Dimensiones porque:

1. **Multiplicación exponencial de datos**: Generaría un producto cartesiano (Cross Join) donde cada registro de la
   tabla de hechos se multiplicaría por cada registro relacionado en la dimensión, creando redundancia excesiva.

2. **Ambigüedad en las medidas**: Las métricas no tendrían un valor claro y único, ya que estarían asociadas a múltiples
   combinaciones de dimensiones, lo que haría imposible determinar el valor real.

3. **Problemas de integridad**: Dificultaría mantener la integridad referencial y consistencia de los datos.

4. **Complejidad en consultas**: Las consultas se volverían extremadamente complejas y el rendimiento se degradaría
   significativamente.

5. **Violación del diseño dimensional**: El modelo dimensional está diseñado específicamente para tener relaciones uno a
   muchos entre dimensiones y hechos, donde cada dimensión proporciona un contexto único para las medidas.

En un modelo dimensional correcto, la relación debe ser de "muchos" desde la tabla de hechos hacia "uno" en la tabla de
dimensión (muchos-a-uno). Cuando se necesita representar una relación muchos-a-muchos en el mundo real, se debe resolver
mediante tablas puente o dimensiones de comportamiento variable.

# INFORMACIÓN ADICIONAL RELEVANTE

- **Cálculos en ETL**: Los cálculos típicamente se realizan entre la etapa intermedia y la tabla de hechos final.

- **IDs en dimensiones**: Los IDs de los sistemas fuente (como empleados) solo se arrastran si el negocio lo requiere,
  usando claves subrogadas (como auto-incrementales) para relacionarlos con la tabla de hechos.

- **Reglas importantes**:
  - Las medidas NO deben estar en las dimensiones, solo en la tabla de hechos
  - La clave primaria de la tabla de hechos generalmente NO es auto-incremental

- **Control Flow vs Data Flow**:
  - **Control Flow (job)**: Organiza y controla qué tareas se ejecutan y en qué orden
  - **Data Flow (task)**: Se encarga de mover y transformar datos de un origen a un destino

- **ETL (Extract, Transform, Load)**: Proceso de extracción, transformación y carga previo al DW. Existen varias
  metodologías como:
  - Full extract: se extraen todos los datos
  - Incremental extract: solo se procesa lo modificado o agregado

- **NoSQL vs SQL**: NoSQL difiere en que no utiliza exclusivamente SQL para consultas, no tiene estructuras fijas como
  tablas, y no suele permitir operaciones JOIN tradicionales.

- **Big Data**: Información de gran volumen, procesada a alta velocidad y con mucha variedad, que facilita la obtención
  de conocimiento y toma de decisiones.