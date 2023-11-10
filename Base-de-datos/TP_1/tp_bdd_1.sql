create database TpBDD2

use TpBDD2

create table Provincias(
Id int primary key identity (1,1) not null,
Provincia VARCHAR(50),
)


create table Ciudades(
Id int primary key identity (1,1) not null,
Ciudad VARCHAR(50),
IdProvincia int,
FOREIGN KEY (IdProvincia) REFERENCES Provincias(Id)
)

create table Direcciones(
Id int primary key identity (1,1) not null,
Calle VARCHAR(100),
Numero VARCHAR(10),
IdCiudad int,
FOREIGN KEY (IdCiudad) REFERENCES Ciudades(Id)
)

create table Clientes(
Id int primary key identity (1,1) not null,
Nombre VARCHAR(50),
Apellido VARCHAR(50),
Dni VARCHAR(50),
RazonSocial VARCHAR(100),
Cuit VARCHAR(20),
IdDireccion int,
Telefono VARCHAR(20),
Email VARCHAR(100),
FOREIGN KEY (IdDireccion) REFERENCES Direcciones(Id)
)

create table TipoRemolque (
Id int primary key identity (1,1) not null,
Remolque varchar(50),
)

create table Camiones (
Id int primary key identity (1,1) not null,
Patente varchar(20),
Marca VARCHAR(50),
Modelo VARCHAR(50),
anio int,
IdRemolque int,
FOREIGN KEY (IdRemolque) REFERENCES TipoRemolque(Id)
)

create table Conductores (
Id int primary key identity (1,1) not null,
Nombre VARCHAR(50),
Apellido VARCHAR(50),
Dni VARCHAR(20),
IdDireccion int,
TelFijo VARCHAR(20),
TelCelular VARCHAR(20),
Edad int,
email VARCHAR(100),
IdRegistro varchar(20),
FOREIGN KEY (IdDireccion) REFERENCES Direcciones(Id)
)

create table Viajes (
Id int primary key identity (1,1) not null,
IdDireccionOrigen int,
IdDireccionDestino int,
KmsRecorridos int,
IdCliente int,
IdCamion int,
IdConductor int,
FechaSalidaEst date,
FechaSalidaReal date,
FechaLlegadaEst date,
FechaLlegadaReal date,
FOREIGN KEY (IdCliente) REFERENCES Clientes(Id),
FOREIGN KEY (IdConductor) REFERENCES Conductores(Dni),
FOREIGN KEY (IdCamion) REFERENCES Camiones(Patente),
FOREIGN KEY (IdDireccionOrigen) REFERENCES Direcciones(Id),
FOREIGN KEY (IdDireccionDestino) REFERENCES Direcciones(Id)
);
