# Documentación de la Base de Datos

## Tabla: Provincias

- **Propósito**: Almacena información sobre las provincias.
- **Atributos**:
  - `Id`: Identificador único de la provincia.
  - `Provincia`: Nombre de la provincia.
- **Relaciones**:
  - No hay relaciones directas.

## Tabla: Ciudades

- **Propósito**: Almacena información sobre las ciudades y su relación con las provincias.
- **Atributos**:
  - `Id`: Identificador único de la ciudad.
  - `Ciudad`: Nombre de la ciudad.
  - `IdProvincia`: Clave externa que referencia la tabla de Provincias.
- **Relaciones**:
  - Relación con la tabla de Provincias a través de `IdProvincia`.

## Tabla: Direcciones

- **Propósito**: Almacena información detallada sobre las direcciones y su relacion con la tabla de ciudades.
- **Atributos**:
  - `Id`: Identificador único de la dirección.
  - `Calle`: Nombre de la calle.
  - `Numero`: Número de la dirección.
  - `IdCiudad`: Clave externa que referencia la tabla de Ciudades.
- **Relaciones**:
  - Relación con la tabla de Ciudades a través de `IdCiudad`.

## Tabla: DireccionesOrigenDestino

- **Propósito**: Almacena información sobre los pares de ciudades que representan direcciones de destinos y orígenes de viajes.
- **Atributos**:
  - `Id`: Identificador único de la relación origen-destino.
  - `IdOrigen`: Clave externa que referencia la tabla de Ciudades para el origen.
  - `IdDestino`: Clave externa que referencia la tabla de Ciudades para el destino.
- **Relaciones**:
  - Relación con la tabla de Ciudades para el origen y destino.

## Tabla: Clientes

- **Propósito**: Almacena información sobre los clientes, ya sean personas o empresas.
- **Atributos**:
  - `Id`: Identificador único del cliente.
  - `Nombre`: Nombre del cliente.
  - `Apellido`: Apellido del cliente.
  - `Dni`: Número de documento.
  - `RazonSocial`: Nombre de la empresa (si aplica).
  - `Cuit`: Número de CUIT (si aplica).
  - `IdDireccion`: Clave externa que referencia la tabla de Direcciones.
- **Relaciones**:
  - Relación con la tabla de Direcciones a través de `IdDireccion`.

## Tabla: TipoRemolque

- **Propósito**: Almacena información sobre los tipos de remolques.
- **Atributos**:
  - `Id`: Identificador único del tipo de remolque.
  - `Remolque`: Descripción del tipo de remolque.
- **Relaciones**:
  - No hay relaciones directas.

## Tabla: Camiones

- **Propósito**: Almacena información detallada sobre los camiones.
- **Atributos**:
  - `Id`: Identificador único del camión.
  - `Patente`: Número de patente del camión.
  - `Marca`: Marca del camión.
  - `Modelo`: Modelo del camión.
  - `Año`: Año de fabricación del camión.
  - `IdRemolque`: Clave externa que referencia la tabla de TipoRemolque.
- **Relaciones**:
  - Relación con la tabla de TipoRemolque a través de `IdRemolque`.

## Tabla: Conductores

- **Propósito**: Almacena información detallada sobre los conductores.
- **Atributos**:
  - `Id`: Identificador único del conductor.
  - `Nombre`: Nombre del conductor.
  - `Apellido`: Apellido del conductor.
  - `Dni`: Número de documento del conductor.
  - `IdDireccion`: Clave externa que referencia la tabla de Direcciones.
  - `TelFijo`: Número de teléfono fijo del conductor.
  - `TelCelular`: Número de teléfono celular del conductor.
  - `Edad`: Edad del conductor.
  - `Email`: Dirección de correo electrónico del conductor.
  - `IdRegistro`: Número de registro del conductor.
- **Relaciones**:
  - Relación con la tabla de Direcciones a través de `IdDireccion`.

## Tabla: Viajes

- **Propósito**: Almacena información detallada sobre los viajes.
- **Atributos**:
  - `Id`: Identificador único del viaje.
  - `IdDireccionesOrigenDestino`: Clave externa que referencia la tabla de DireccionesOrigenDestino.
  - `KmsRecorridos`: Kilómetros recorridos en el viaje.
  - `IdCliente`: Clave externa que referencia la tabla de Clientes.
  - `IdCamion`: Clave externa que referencia la tabla de Camiones.
  - `IdConductor`: Clave externa que referencia la tabla de Conductores.
  - `FechaSalidaEst`: Fecha estimada de salida.
  - `FechaSalidaReal`: Fecha real de salida.
  - `FechaLlegadaEst`: Fecha estimada de llegada.
  - `FechaLlegadaReal`: Fecha real de llegada.
- **Relaciones**:
  - Relación con las tablas de DireccionesOrigenDestino, Clientes, Camiones y Conductores.
En viajes recorte bastantes datos y los meti adentro de IdDireccionesOrigenDestino ya que eran 8 campos mas, ya que tengo:
- calle, numero, ciudad, provincia de origen y de destino.

## Tabla: AsignacionesViaje

- **Propósito**: Almacena información sobre las asignaciones de camiones y conductores a viajes.
- **Atributos**:
  - `IdCamion`: Clave externa que referencia la tabla de Camiones.
  - `IdChofer`: Clave externa que referencia la tabla de Conductores.
  - `IdViajes`: Clave externa que referencia la tabla de Viajes.
  - `FechaAsignacion`: Fecha en que se asigna el camión y el conductor al viaje.
- **Clave Primaria Compuesta**:
  - La clave primaria consta de `IdCamion`, `IdChofer` e `IdViajes`.
- **Relaciones**:
  - Relación con las tablas de Camiones, Conductores y Viajes mediante claves foráneas.
Aca Agregue IdViajes porque eso lo hace unico ya que puede pasar que un camion lo maneje el mismo chofer varias veces y por lo tanto tendria asignado varias veces el mismo camion pero no sabria para que viaje particular seria que se le asigno.

```
Disclaimer/Aclaraciones:
La data ingresada puede que no tenga sentido, ya que puede ser que alguna direccion de un conductor 
sea una direccion de destino u de origen, al igual que otro dato ingresado se pueda pisar.

En la relacion de camiones asignados a viajes es uno a uno ya que para cada camion asignado 
va a tener 1 viaje y para cada viaje va a tener 1 camion asignado.

Despues tema de Provincias-Ciudades-Direcciones-DireccionesOrigenDestino
Podria haber tenido en cuenta que el IdDireccion de Clientes iba a ser siempre la direccion
de destino de los envios, pero para evitar problemas cree una identidad aparte que seria
una combinacion unica de direccion origen y direccion destino.
Como a veces pasa que una calle esta en muchas ciudades yo no lo tuve en cuenta, y lo plantee 
como que las direcciones no se repiten entre ciudades, por mas de que en la realidad se repitan. 
Otra cosa que no puse fue el codigo postal que podria haberlo tomado como un id de la direccion o la ciudad. 
Al igual que en otras entidades tenia id uncios como por ejemplo las patentes en los camiones, los dni en los 
choferes, los dni o cuit en los clientes. Pero decidi que cada entidad tenga su propio Id.
Las entidades de DireccionesOrigenDestino en relacion a las direcciones son las 2 de muchos a 1 ya que 
un destino puede tener solo 1 direccion mientras que nuestras direcciones tienen siempre mas de 1 siempre 
ya que tenemos 2 como minimo, origen y destino.
```

# Third Normal Form
Ya esta normalizada, ya que esta en segunda forma normal y todos los atributos no clave dependen de manera no transitiva de la clave primaria.

