1. Definición y Creación de la Base de Datos:
- Se crea una base de datos llamada "TpBDD1".
- Se definen varias tablas como "Provincias", "Ciudades", "Direcciones", "DireccionesOrigenDestino", "Clientes", "TipoRemolque", "Camiones", "Conductores", "Viajes", "AsignacionesViaje".
2. Definición de Índices en las Tablas:
- Se crean índices para mejorar el rendimiento en las consultas en varias tablas.
3. Agregando un Check Constraint a la Tabla Clientes:
- Se agrega un CHECK CONSTRAINT en la tabla "Clientes" para verificar si es un cliente individual o una empresa, basándose en los campos de nombre, apellido, DNI, razón social y CUIT.
4. Definición de un Stored Procedure "ActualizarViajeEnvio":
- Este procedimiento actualiza la fecha estimada de llegada de un viaje si la fecha de llegada real aún no está registrada.
5. Inserción de Datos de Ejemplo:
- Se insertan datos de ejemplo en las tablas "Provincias", "Ciudades", "Direcciones", "DireccionesOrigenDestino", "Clientes", "TipoRemolque", "Camiones", "Conductores", "Viajes", y "AsignacionesViaje".
6. Ejecución del Stored Procedure "ActualizarViajeEnvio" y Obtención de Datos:
- Se ejecuta el procedimiento almacenado ActualizarViajeEnvio para actualizar la fecha estimada de llegada de un viaje específico.
- Se declara un par de variables para almacenar mensajes de resultado y patente de camión.
- Se ejecuta el procedimiento ObtenerPatenteCamionAsignado con algunos parámetros y se muestra el resultado.
7. Consultas SQL:
- Se realizan diversas consultas SQL, como contar cuántos viajes se realizaron hacia la provincia de Santa Fe, mostrar datos relevantes sobre los viajes realizados desde la provincia de Córdoba durante el primer semestre de 2023, listar los 3 choferes con la mayor cantidad de kilómetros en 2023, y obtener una lista de clientes que solicitaron viajes/envíos en 2023 con nombre de choferes y kilómetros recorridos.