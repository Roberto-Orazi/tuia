/*Tablas*/
create database TpBDD

use TpBDD

create table Provincias(
Id int primary key identity (1,1) not null,
provincia varchar,
)


create table Ciudades(
Id int primary key identity (1,1) not null,
Ciudad varchar,
IdProvincia int,
FOREIGN KEY (IdProvincia) REFERENCES Provincias(Id)
)

create table Direcciones(
Id int primary key identity (1,1) not null,
Calle varchar,
Numero varchar,
IdCiudad int,
FOREIGN KEY (IdCiudad) REFERENCES Ciudades(Id)
)

create table Clientes(
Id int primary key identity (1,1) not null,
Nombre varchar,
Apellido varchar,
Dni varchar,
RazonSocial varchar,
Cuit varchar,
IdDireccion int,
Telefono varchar,
Email varchar,
FOREIGN KEY (IdDireccion) REFERENCES Direcciones(Id)
)

create table TipoRemolque (
Id int primary key identity (1,1) not null,
Remolque varchar,
)

create table Camiones (
Patente varchar primary key not null,
Marca varchar,
Modelo varchar,
año int,
IdRemolque int,
FOREIGN KEY (IdRemolque) REFERENCES TipoRemolque(Id)
)

create table Conductores (
Nombre varchar,
Apellido varchar,
Dni int primary key identity (1,1) not null,
IdDireccion int,
TelFijo varchar,
TelCelular varchar,
Edad int,
email varchar,
IdRegistro varchar,
IdCamion varchar,
FOREIGN KEY (IdCamion) REFERENCES Camiones(Patente),
FOREIGN KEY (IdDireccion) REFERENCES Direcciones(Id)
)

create table Viajes (
Id int primary key identity (1,1) not null,
IdDireccionOrigen int,
KmsRecorridos int,
IdCliente int,
IdCamion varchar,
IdConductor int,
FechaSalidaEst date,
FechaSalidaReal date,
FechaLlegadaEst date,
FechaLlegadaReal date,
FOREIGN KEY (IdCliente) REFERENCES Clientes(Id),
FOREIGN KEY (IdConductor) REFERENCES Conductores(Dni),
FOREIGN KEY (IdDireccionOrigen) REFERENCES Direcciones(Id)
);