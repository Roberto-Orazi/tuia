# Normalización en Bases de Datos

## Primera Forma Normal (1NF)
Una tabla está en 1NF si:
1. Todos los atributos contienen valores atómicos, es decir, indivisibles.
2. Cada campo debe contener solo un valor por registro.

**Ejemplo:**
Supongamos que tenemos una tabla con información de estudiantes y sus cursos:

| EstudianteID | Nombre      | Cursos                |
|--------------|-------------|-----------------------|
| 1            | Juan Pérez  | Matemáticas, Física   |
| 2            | Ana Gómez   | Química, Biología     |

**Problema:** Los cursos están almacenados en un solo campo como una lista de valores, lo cual no es atómico.

**Solución (1NF):** Separar los cursos en registros individuales.

| EstudianteID | Nombre      | Curso         |
|--------------|-------------|---------------|
| 1            | Juan Pérez  | Matemáticas   |
| 1            | Juan Pérez  | Física        |
| 2            | Ana Gómez   | Química       |
| 2            | Ana Gómez   | Biología      |

## Segunda Forma Normal (2NF)
Una tabla está en 2NF si:
1. Está en 1NF.
2. Todos los atributos no clave dependen de toda la clave primaria.

**Ejemplo:**
Continuamos con la tabla anterior pero añadimos la información del profesor del curso:

| EstudianteID | Nombre      | Curso         | Profesor       |
|--------------|-------------|---------------|----------------|
| 1            | Juan Pérez  | Matemáticas   | Prof. García   |
| 1            | Juan Pérez  | Física        | Prof. López    |
| 2            | Ana Gómez   | Química       | Prof. Martínez |
| 2            | Ana Gómez   | Biología      | Prof. Rodríguez|

**Problema:** La columna "Nombre" depende solo de "EstudianteID", no de la combinación de "EstudianteID" y "Curso", lo que viola la 2NF.

**Solución (2NF):** Dividir la tabla en dos para que cada campo dependa de toda la clave primaria.

**Tabla Estudiantes:**

| EstudianteID | Nombre      |
|--------------|-------------|
| 1            | Juan Pérez  |
| 2            | Ana Gómez   |

**Tabla Cursos:**

| EstudianteID | Curso       | Profesor       |
|--------------|-------------|----------------|
| 1            | Matemáticas | Prof. García   |
| 1            | Física      | Prof. López    |
| 2            | Química     | Prof. Martínez |
| 2            | Biología    | Prof. Rodríguez|

## Tercera Forma Normal (3NF)
Una tabla está en 3NF si:
1. Está en 2NF.
2. No hay dependencias transitivas, es decir, los atributos no clave no deben depender de otros atributos no clave.

**Ejemplo:**
Supongamos que en la tabla de cursos añadimos la información del departamento del profesor:

| EstudianteID | Curso       | Profesor       | Departamento      |
|--------------|-------------|----------------|-------------------|
| 1            | Matemáticas | Prof. García   | Ciencias Exactas  |
| 1            | Física      | Prof. López    | Ciencias Exactas  |
| 2            | Química     | Prof. Martínez | Ciencias Naturales|
| 2            | Biología    | Prof. Rodríguez| Ciencias Naturales|

**Problema:** "Departamento" depende de "Profesor", no de la clave primaria compuesta (EstudianteID, Curso).

**Solución (3NF):** Crear una tabla separada para los profesores y sus departamentos.

**Tabla Estudiantes:**

| EstudianteID | Nombre      |
|--------------|-------------|
| 1            | Juan Pérez  |
| 2            | Ana Gómez   |

**Tabla Cursos:**

| EstudianteID | Curso       | Profesor       |
|--------------|-------------|----------------|
| 1            | Matemáticas | Prof. García   |
| 1            | Física      | Prof. López    |
| 2            | Química     | Prof. Martínez |
| 2            | Biología    | Prof. Rodríguez|

**Tabla Profesores:**

| Profesor       | Departamento      |
|----------------|-------------------|
| Prof. García   | Ciencias Exactas  |
| Prof. López    | Ciencias Exactas  |
| Prof. Martínez | Ciencias Naturales|
| Prof. Rodríguez| Ciencias Naturales|



# Dependencias Funcionales

## Dependencia Funcional
Una dependencia funcional entre dos conjuntos de atributos en una relación de base de datos ocurre cuando el valor de uno de los atributos determina el valor de otro atributo. Si A y B son atributos de una relación, B es funcionalmente dependiente de A (escrito como A -> B) si, en cualquier instante de tiempo, cada valor de A está asociado con un solo valor de B.

### Ejemplo:
| EstudianteID | Nombre     | Curso       | Profesor       |
|--------------|------------|-------------|----------------|
| 1            | Juan Pérez | Matemáticas | Prof. García   |
| 1            | Juan Pérez | Física      | Prof. López    |
| 2            | Ana Gómez  | Química     | Prof. Martínez |
| 2            | Ana Gómez  | Biología    | Prof. Rodríguez|

En esta tabla, la relación EstudianteID -> Nombre es una dependencia funcional porque cada EstudianteID único tiene asociado un único Nombre.

## Dependencia Funcional Total
Una dependencia funcional es total si un atributo es funcionalmente dependiente de un conjunto de atributos completos. Es decir, un atributo depende de la totalidad de la clave primaria.

### Ejemplo:
| EstudianteID | Curso       | Profesor       |
|--------------|-------------|----------------|
| 1            | Matemáticas | Prof. García   |
| 1            | Física      | Prof. López    |
| 2            | Química     | Prof. Martínez |
| 2            | Biología    | Prof. Rodríguez|

Aquí, (EstudianteID, Curso) -> Profesor es una dependencia funcional total porque el valor de Profesor depende tanto de EstudianteID como de Curso juntos, es decir, de toda la clave primaria compuesta.

## Dependencia Funcional Parcial
Una dependencia funcional es parcial si un atributo depende de una parte de la clave primaria, no de toda la clave primaria.

### Ejemplo:
| EstudianteID | Curso       | Nombre      |
|--------------|-------------|-------------|
| 1            | Matemáticas | Juan Pérez  |
| 1            | Física      | Juan Pérez  |
| 2            | Química     | Ana Gómez   |
| 2            | Biología    | Ana Gómez   |

En esta tabla, EstudianteID -> Nombre es una dependencia funcional parcial porque Nombre depende solo de EstudianteID y no de la clave primaria completa (EstudianteID, Curso).

## Diferencia entre Dependencia Funcional Total y Parcial

- **Dependencia Funcional Total:** Ocurre cuando un atributo depende de toda la clave primaria.
  - **Ejemplo:** (EstudianteID, Curso) -> Profesor en la tabla de cursos. Aquí, Profesor depende de ambas partes de la clave primaria compuesta (EstudianteID y Curso).

- **Dependencia Funcional Parcial:** Ocurre cuando un atributo depende solo de una parte de la clave primaria.
  - **Ejemplo:** EstudianteID -> Nombre en la tabla de cursos. Aquí, Nombre depende solo de EstudianteID, no de toda la clave primaria compuesta.

## Dependencia Funcional Transitiva
Una dependencia funcional es transitiva si un atributo A determina un atributo B, y B determina un atributo C, entonces A determina C.

### Ejemplo:
| EstudianteID | Curso       | Profesor       | Departamento      |
|--------------|-------------|----------------|-------------------|
| 1            | Matemáticas | Prof. García   | Ciencias Exactas  |
| 1            | Física      | Prof. López    | Ciencias Exactas  |
| 2            | Química     | Prof. Martínez | Ciencias Naturales|
| 2            | Biología    | Prof. Rodríguez| Ciencias Naturales|

En esta tabla:
- (EstudianteID, Curso) -> Profesor
- Profesor -> Departamento

Por lo tanto, (EstudianteID, Curso) -> Departamento es una dependencia funcional transitiva, porque el departamento depende de Profesor, que a su vez depende de (EstudianteID, Curso).