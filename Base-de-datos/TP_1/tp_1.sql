create database TpBDD1

use TpBDD1
/*Tables*/
create table Provincias(
Id int primary key identity (1,1) not null,
Provincia VARCHAR(50),
)

CREATE INDEX idx_Provincias_Provincia ON Provincias (Provincia);

create table Ciudades(
Id int primary key identity (1,1) not null,
Ciudad VARCHAR(50),
IdProvincia int,
FOREIGN KEY (IdProvincia) REFERENCES Provincias(Id)
)

CREATE INDEX idx_Ciudades_IdProvincia ON Ciudades (IdProvincia);

create table Direcciones(
Id int primary key identity (1,1) not null,
Calle VARCHAR(100),
Numero VARCHAR(10),
IdCiudad int,
FOREIGN KEY (IdCiudad) REFERENCES Ciudades(Id)
)

CREATE INDEX idx_Direcciones_IdCiudad ON Direcciones (IdCiudad);


create table DireccionesOrigenDestino(
Id int primary key identity (1,1) not null,
IdOrigen int,
IdDestino int,
FOREIGN KEY (IdOrigen) REFERENCES Direcciones(Id),
FOREIGN KEY (IdDestino) REFERENCES Direcciones(Id)
)

CREATE INDEX idx_DireccionesOrigenDestino_IdOrigen ON DireccionesOrigenDestino (IdOrigen);
CREATE INDEX idx_DireccionesOrigenDestino_IdDestino ON DireccionesOrigenDestino (IdDestino);

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

CREATE INDEX idx_Clientes_IdDireccion ON Clientes (IdDireccion);

ALTER TABLE Clientes
ADD CONSTRAINT CK_ClienteTipo CHECK ( /*ESTO LO METIMOS PARA VERIFICAR LO DE SI ES EMPRESA O NO*/
    (Nombre IS NOT NULL AND Apellido IS NOT NULL AND Dni IS NOT NULL AND RazonSocial IS NULL AND Cuit IS NULL) OR
    (Nombre IS NULL AND Apellido IS NULL AND Dni IS NULL AND RazonSocial IS NOT NULL AND Cuit IS NOT NULL)
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
año int,
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
FOREIGN KEY (IdDireccion) REFERENCES Direcciones(Id),
)

create table Viajes (
Id int primary key identity (1,1) not null,
IdDireccionesOrigenDestino int,
KmsRecorridos int,
IdCliente int,
IdCamion int,
IdConductor int,
FechaSalidaEst date,
FechaSalidaReal date,
FechaLlegadaEst date,
FechaLlegadaReal date,
FOREIGN KEY (IdCliente) REFERENCES Clientes(Id),
FOREIGN KEY (IdCamion) REFERENCES Camiones(Id),
FOREIGN KEY (IdConductor) REFERENCES Conductores(Id),
FOREIGN KEY (IdDireccionesOrigenDestino) REFERENCES DireccionesOrigenDestino(Id)
);

CREATE TABLE AsignacionesViaje (
    IdCamion int,
    IdChofer int,
    IdViaje int,
    FechaAsignacion date,
    PRIMARY KEY (IdCamion, IdChofer, IdViaje),
    FOREIGN KEY (IdCamion) REFERENCES Camiones(Id),
    FOREIGN KEY (IdChofer) REFERENCES Conductores(Id),
    FOREIGN KEY (IdViaje) REFERENCES Viajes(Id)
);

GO /*Esto se usa para separar bloques de codigo Es para el CP*/

/*Aca vamos a agregar el store procedure*/
CREATE PROCEDURE ActualizarViajeEnvio
    @IdViaje INT,
    @NuevaFechaLlegadaEst DATE
AS
BEGIN
    IF EXISTS (
        SELECT 1
        FROM Viajes
        WHERE Id = @IdViaje
          AND FechaLlegadaReal IS NULL
    )
    BEGIN
        UPDATE Viajes
        SET FechaLlegadaEst = @NuevaFechaLlegadaEst
        WHERE Id = @IdViaje;

        PRINT 'Fecha estimada de llegada actualizada exitosamente.';
    END
    ELSE
    BEGIN
        PRINT 'No se puede actualizar la fecha estimada de llegada para un viaje que ya ha llegado.';
    END
END;

/*Inserts*/
INSERT INTO Provincias (Provincia) VALUES
('Buenos Aires'), ('Córdoba'), ('Santa Fe'), ('Mendoza'), ('Tucumán'), ('Salta'),
('Jujuy'), ('Misiones'), ('Entre Ríos'), ('La Pampa'), ('Neuquén'), ('Río Negro');

INSERT INTO Ciudades (Ciudad, IdProvincia) VALUES
('La Plata', 1), ('Córdoba Capital', 2), ('Rosario', 3), ('Mendoza Capital', 4), ('San Miguel de Tucumán', 5), ('Salta Capital', 6),
('San Salvador de Jujuy', 7), ('Posadas', 8), ('Paraná', 9), ('Santa Rosa', 10), ('Neuquén Capital', 11), ('Viedma', 12);

INSERT INTO Direcciones (Calle, Numero, IdCiudad) VALUES
('San Martín', '567', 1), ('Belgrano', '432', 2), ('Rivadavia', '876', 3),
('Sarmiento', '321', 4), ('Avenida Mayo', '654', 5), ('Laprida', '987', 6),
('San Juan', '111', 1), ('San Luis', '222', 2), ('Entre Ríos', '333', 3),
('Jujuy', '444', 4), ('Santa Cruz', '555', 5), ('Tierra del Fuego', '666', 6),
('Rawson', '777', 1), ('Trelew', '888', 2), ('Comodoro Rivadavia', '999', 3),
('Bolívar', '123', 7), ('San Martín', '456', 8), ('Urquiza', '789', 9),
('Moreno', '234', 10), ('Sáenz Peña', '567', 11), ('Roca', '890', 12),
('Belgrano', '111', 7), ('Alem', '222', 8), ('San Martín', '333', 9),
('Mitre', '444', 10), ('Brown', '555', 11), ('Alberdi', '666', 12),
('San Juan', '777', 7), ('Lavalle', '888', 8), ('Castelli', '999', 9);

INSERT INTO DireccionesOrigenDestino (IdOrigen, IdDestino) VALUES
(1, 16), (4, 20), (5, 4), (7, 8), (9, 12), (11, 2), (13, 3), (12, 10), (2, 14), (4, 18),
(6, 22), (8, 2), (10, 30), (16, 1), (20, 5), (24, 3), (28, 13), (2, 17), (6, 21), (10, 25);

INSERT INTO Clientes (Nombre, Apellido, Dni, RazonSocial, Cuit, IdDireccion, Telefono, Email) VALUES
('Juan', 'García', '12345679', NULL, NULL, 1, '1234567891', 'juan2@gmail.com'),
(NULL,NULL,NULL, 'Empresa D', '12345678902', 12, '2345678902', 'marcela@empresaD.com'),
('Carolina', 'Martínez', '34567891', NULL, NULL, 13, '3456789013', 'carolina@gmail.com'),
(NULL,NULL,NULL, 'Empresa E', '23456789023', 14, '4567890124', 'pedro@empresaE.com'),
('Marta', 'López', '56789013', NULL, NULL, 15, '5678901235', 'marta@gmail.com'),
(NULL,NULL,NULL, 'Empresa F', '34567890124', 16, '6789012346', 'ricardo@empresaF.com'),
('Camila', 'Gómez', '78901235', NULL, NULL, 17, '7890123456', 'camila@empresaG.com'),
(NULL,NULL,NULL, 'Empresa H', '56789012346', 18, '8901234567', 'francisco@empresaH.com'),
(NULL,NULL,NULL, 'Empresa I', '67890123457', 19, '9012345678', 'victoria@empresaI.com'),
('Jorge', 'Díaz', '01234568', NULL, NULL, 20, '0123456789', 'jorge@empresaJ.com'),
('Liliana', 'Fernández', '12345679',  NULL, NULL, 21, '1234567890', 'liliana@empresaK.com'),
('Eduardo', 'Gómez', '23456780',  NULL, NULL,  22, '2345678901', 'eduardo@empresaL.com'),
('Lucas', 'Pérez', '34567891',  NULL, NULL,  23, '3456789012', 'lucas@empresaM.com'),
(NULL,NULL,NULL, 'Empresa N', '12345678902', 24, '4567890123', 'ana@empresaN.com'),
('Sofía', 'Martínez', '56789013',  NULL, NULL,  25, '5678901234', 'sofia@empresaO.com'),
(NULL,NULL,NULL, 'Empresa P', '34567890124', 26, '6789012345', 'diego@empresaP.com'),
('Mariano', 'López', '78901235',  NULL, NULL,  27, '7890123456', 'mariano@empresaQ.com'),
(NULL,NULL,NULL, 'Empresa R', '56789012346', 28, '8901234567', 'florencia@empresaR.com'),
(NULL,NULL,NULL, 'Empresa S', '67890123457', 29, '9012345678', 'carlos@empresaS.com'),
('Romina', 'Suárez', '01234568',  NULL, NULL, 30, '0123456789', 'romina@empresaT.com');

INSERT INTO TipoRemolque (Remolque) VALUES ('Remolque A'), ('Remolque B'), ('Remolque C'), ('Remolque D'), ('Remolque E'), ('Remolque F');

INSERT INTO Camiones (Patente, Marca, Modelo, año, IdRemolque) VALUES
('XYZ123', 'Scania', 'R500', 2020, 1),
('ABC456', 'Volvo', 'FH480', 2019, 2),
('DEF789', 'Mercedes-Benz', 'Actros', 2021, 3),
('GHI012', 'Iveco', 'Stralis', 2018, 4),
('JKL345', 'MAN', 'TGX', 2022, 5),
('MNO678', 'Renault', 'T460', 2017, 6);


INSERT INTO Conductores (Nombre, Apellido, Dni, IdDireccion, TelFijo, TelCelular, Edad, email, IdRegistro)
VALUES
('Carlos', 'Gómez', '12345678', 1, '011-1111111', '011-2222222', 30, 'carlos@gmail.com', 'ABCDE123'),
('Ana', 'Martínez', '23456789', 2, '011-3333333', '011-4444444', 28, 'ana@gmail.com', 'FGHIJ456'),
('Luis', 'Fernández', '34567890', 3, '011-5555555', '011-6666666', 35, 'luis@gmail.com', 'KLMNO789'),
('Laura', 'Rodríguez', '45678901', 4, '011-7777777', '011-8888888', 32, 'laura@gmail.com', 'PQRST012'),
('Javier', 'Suárez', '56789012', 5, '011-9999999', '011-0000000', 29, 'javier@gmail.com', 'UVWXY345'),
('Marta', 'López', '67890123', 6, '011-1212121', '011-3434343', 40, 'marta@gmail.com', 'ZABCDE678'),
('Pedro', 'Díaz', '78901234', 7, '011-5656565', '011-7878787', 27, 'pedro@gmail.com', 'ZABCDE679'),
('Lucía', 'García', '89012345', 8, '011-9898989', '011-2121212', 33, 'lucia@gmail.com', 'ZABCDE680'),
('Diego', 'Pérez', '90123456', 9, '011-1212122', '011-3434344', 26, 'diego@gmail.com', 'ZABCDE681'),
('Sofía', 'Suárez', '01234567', 10, '011-5656566', '011-7878788', 28, 'sofia@gmail.com', 'ZABCDE682');

INSERT INTO Viajes (IdDireccionesOrigenDestino, KmsRecorridos, IdCliente, IdCamion, IdConductor, FechaSalidaEst, FechaSalidaReal, FechaLlegadaEst, FechaLlegadaReal)
VALUES
(1, 300, 1, 1, 1, '2023-12-02', '2023-12-02', '2023-12-03', '2023-12-03'),
(2, 500, 2, 2, 2, '2023-12-03', '2023-12-03', '2023-12-04', '2023-12-04'),
(3, 700, 3, 3, 3, '2023-12-04', '2023-12-04', '2023-12-05', '2023-12-05'),
(4, 900, 4, 4, 4, '2023-12-05', '2023-12-05', '2023-12-06', '2023-12-06'),
(5, 1100, 5, 5, 5, '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-07'),
(6, 1300, 6, 6, 6, '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'),
(7, 1500, 7, 1, 7, '2023-12-08', '2023-12-08', '2023-12-09', '2023-12-09'),
(8, 1700, 8, 2, 8, '2023-12-09', '2023-12-09', '2023-12-10', '2023-12-10'),
(9, 1900, 9, 3, 9, '2023-01-10', '2023-01-11', '2023-01-14', '2023-01-16'),
(10, 2100, 10, 4, 10, '2023-12-11', '2023-12-11', '2023-12-12', '2023-12-12'),
(11, 1000, 11, 5, 1, '2023-12-12', '2023-12-12', '2023-12-13', '2023-12-13'),
(12, 1200, 12, 6, 2, '2023-12-13', '2023-12-13', '2023-12-14', '2023-12-14'),
(13, 1400, 13, 1, 3, '2023-12-14', '2023-12-14', '2023-12-15', '2023-12-15'),
(14, 1600, 14, 2, 4, '2023-12-15', '2023-12-15', '2023-12-16', '2023-12-16'),
(15, 1800, 15, 3, 5, '2023-12-16', '2023-12-16', '2023-12-17', '2023-12-17'),
(16, 2000, 16, 4, 6, '2023-12-17', '2023-12-17', '2023-12-18', '2023-12-18'),
(17, 2200, 17, 5, 7, '2023-12-18', '2023-12-18', '2023-12-19', '2023-12-19'),
(18, 2400, 18, 6, 8, '2023-12-19', '2023-12-19', '2023-12-20', '2023-12-20'),
(19, 2600, 19, 1, 9, '2023-12-20', '2023-12-20', '2023-12-21', '2023-12-21'),
(20, 2800, 20, 2, 10, '2023-12-21', '2023-12-21', '2023-12-22', '2023-12-22');


INSERT INTO AsignacionesViaje (IdCamion, IdChofer, IdViaje, FechaAsignacion) VALUES
(1, 1, 1, '2023-12-02'),
(2, 2, 2, '2023-12-03'),
(3, 3, 3, '2023-12-04'),
(4, 4, 4, '2023-12-05'),
(5, 5, 5, '2023-12-06'),
(6, 6, 6, '2023-12-07'),
(1, 7, 7, '2023-12-08'),
(2, 8, 8, '2023-12-09'),
(3, 9, 9, '2023-12-10'),
(4, 10, 10, '2023-12-11'),
(5, 1, 11, '2023-12-12'),
(6, 2, 12, '2023-12-13'),
(1, 3, 13, '2023-12-14'),
(2, 4, 14, '2023-12-15'),
(3, 5, 15, '2023-12-16'),
(4, 6, 16, '2023-12-17'),
(5, 7, 17, '2023-12-18'),
(6, 8, 18, '2023-12-19'),
(1, 9, 19, '2023-12-20'),
(2, 10, 20, '2023-12-21');

EXEC ActualizarViajeEnvio @IdViaje = 1, @NuevaFechaLlegadaEst = '2023-12-31';

/*consultas*/
/*Cuantos viajes se realizaron hacia la provincia de santafe*/
SELECT COUNT(DISTINCT v.Id) AS TotalViajes
FROM Viajes v
JOIN DireccionesOrigenDestino dod ON v.IdDireccionesOrigenDestino = dod.Id
JOIN Direcciones d ON dod.IdDestino = d.Id
JOIN Ciudades c ON d.IdCiudad = c.Id
JOIN Provincias p ON c.IdProvincia = p.Id
WHERE p.Provincia = 'Santa Fe';
/*Mostrar datos relevantes sobre los viajes realizados desde la provincia de cordoba durante le primer semestre 2023*/
SELECT
    V.Id AS IdViaje,
    COALESCE(C.Nombre, C.RazonSocial) AS NombreCliente,
    DirOrigen.Calle + ' ' + DirOrigen.Numero AS DireccionOrigen,
    CD.Ciudad AS CiudadOrigen,
    V.KmsRecorridos,
    V.FechaSalidaEst,
    V.FechaLlegadaEst
FROM
    Viajes V
    JOIN Clientes C ON V.IdCliente = C.Id
    JOIN DireccionesOrigenDestino DOD ON V.IdDireccionesOrigenDestino = DOD.Id
    JOIN Direcciones DirOrigen ON DOD.IdOrigen = DirOrigen.Id
    JOIN Ciudades CD ON DirOrigen.IdCiudad = CD.Id
    JOIN Provincias P_CD ON CD.IdProvincia = P_CD.Id
WHERE
    P_CD.Provincia = 'Córdoba'
    AND V.FechaSalidaEst >= '2023-01-01'
    AND V.FechaSalidaEst < '2023-07-01';

/*Listar 3 choferes con mayor cantidad de kilometros en 2023 mostrando: nombres, cantidad de kms recorridos en orden
descentente*/
SELECT TOP 3 cond.Nombre AS NombreConductor, SUM(v.KmsRecorridos) AS TotalKilometros
FROM Viajes v
JOIN Conductores cond ON v.IdConductor = cond.Id
WHERE YEAR(v.FechaSalidaEst) = 2023
GROUP BY cond.Nombre
ORDER BY TotalKilometros DESC;
/*Obtener lista de clientes que solilcitaron viajes/envios en 2023 con nombre de choferes y kms recorridos en cada
viaje. en orden descendete de km recorridos*/
SELECT
    COALESCE(c.Nombre, c.RazonSocial) AS NombreCliente,
    c.Apellido AS ApellidoCliente,
    cond.Nombre AS NombreConductor,
    v.KmsRecorridos,
    v.FechaSalidaEst AS ViajesRecientes
FROM Viajes v
JOIN Clientes c ON v.IdCliente = c.Id
JOIN Conductores cond ON v.IdConductor = cond.Id
WHERE YEAR(v.FechaSalidaEst) = 2023
ORDER BY v.KmsRecorridos DESC;