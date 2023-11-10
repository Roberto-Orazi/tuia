INSERT INTO Provincias (Provincia) VALUES ('Buenos Aires'), ('Córdoba'), ('Santa Fe'), ('Mendoza'), ('Tucumán'), ('Salta');


INSERT INTO Ciudades (Ciudad, IdProvincia) VALUES
('La Plata', 1), ('Córdoba Capital', 2), ('Rosario', 3), ('Mendoza Capital', 4), ('San Miguel de Tucumán', 5), ('Salta Capital', 6);


INSERT INTO Direcciones (Calle, Numero, IdCiudad) VALUES
('Av. 9 de Julio', '123', 1), ('Av. Colón', '456', 2), ('Av. Pellegrini', '789', 3),
('Av. San Martín', '234', 4), ('Av. Aconquija', '567', 5), ('Av. Belgrano', '890', 6);


INSERT INTO Clientes (Nombre, Apellido, Dni, RazonSocial, Cuit, IdDireccion, Telefono, Email) VALUES
('Juan', 'García', '12345679', NULL, NULL, 11, '1234567891', 'juan2@gmail.com'),
('Marcela', 'Suárez', '23456780', 'Empresa D', '12345678902', 12, '2345678902', 'marcela@empresaD.com'),
('Carolina', 'Martínez', '34567891', NULL, NULL, 13, '3456789013', 'carolina@gmail.com'),
('Pedro', 'Fernández', '45678902', 'Empresa E', '23456789023', 14, '4567890124', 'pedro@empresaE.com'),
('Marta', 'López', '56789013', NULL, NULL, 15, '5678901235', 'marta@gmail.com'),
('Ricardo', 'Rodríguez', '67890124', 'Empresa F', '34567890124', 16, '6789012346', 'ricardo@empresaF.com'),
('Camila', 'Gómez', '78901235', 'Empresa G', '45678901235', 17, '7890123456', 'camila@empresaG.com'),
('Francisco', 'Pérez', '89012346', 'Empresa H', '56789012346', 18, '8901234567', 'francisco@empresaH.com'),
('Victoria', 'Suárez', '90123457', 'Empresa I', '67890123457', 19, '9012345678', 'victoria@empresaI.com'),
('Jorge', 'Díaz', '01234568', 'Empresa J', '78901234568', 20, '0123456789', 'jorge@empresaJ.com'),
('Liliana', 'Fernández', '12345679', 'Empresa K', '89012345679', 21, '1234567890', 'liliana@empresaK.com'),
('Eduardo', 'Gómez', '23456780', 'Empresa L', '90123456780', 22, '2345678901', 'eduardo@empresaL.com'),
('Lucas', 'Pérez', '34567891', 'Empresa M', '01234567891', 23, '3456789012', 'lucas@empresaM.com'),
('Ana', 'Rodríguez', '45678902', 'Empresa N', '12345678902', 24, '4567890123', 'ana@empresaN.com'),
('Sofía', 'Martínez', '56789013', 'Empresa O', '23456789013', 25, '5678901234', 'sofia@empresaO.com'),
('Diego', 'Fernández', '67890124', 'Empresa P', '34567890124', 26, '6789012345', 'diego@empresaP.com'),
('Mariano', 'López', '78901235', 'Empresa Q', '45678901235', 27, '7890123456', 'mariano@empresaQ.com'),
('Florencia', 'Rodríguez', '89012346', 'Empresa R', '56789012346', 28, '8901234567', 'florencia@empresaR.com'),
('Carlos', 'Gómez', '90123457', 'Empresa S', '67890123457', 29, '9012345678', 'carlos@empresaS.com'),
('Romina', 'Suárez', '01234568', 'Empresa T', '78901234568', 30, '0123456789', 'romina@empresaT.com');


INSERT INTO TipoRemolque (Remolque) VALUES ('Remolque A'), ('Remolque B'), ('Remolque C'), ('Remolque D'), ('Remolque E'), ('Remolque F');


INSERT INTO Camiones (Patente, Marca, Modelo, año, IdRemolque) VALUES
('XYZ123', 'Scania', 'R500', 2020, 1),
('ABC456', 'Volvo', 'FH480', 2019, 2),
('DEF789', 'Mercedes-Benz', 'Actros', 2021, 3),
('GHI012', 'Iveco', 'Stralis', 2018, 4),
('JKL345', 'MAN', 'TGX', 2022, 5),
('MNO678', 'Renault', 'T460', 2017, 6);

INSERT INTO Conductores (Nombre, Apellido, Dni, TelFijo, TelCelular, Edad, email, IdRegistro, IdDireccion) VALUES
('Sofía', 'López', '39.234.634', '011-1111111', '011-2222222', 31, 'sofia@gmail.com', 'ABCDE124', 1),
('Javier', 'González', '37.234.634', '011-3333333', '011-4444444', 29, 'javier@gmail.com', 'FGHIJ457', 2),
('Lucas', 'Martínez', '32.234.114', '011-5555555', '011-6666666', 38, 'lucas@gmail.com', 'KLMNO790', 3),
('Marina', 'Fernández', '33.231.634', '011-7777777', '011-8888888', 35, 'marina@gmail.com', 'PQRST013', 4),
('Miguel', 'Rodríguez', '28.144.324', '011-9999999', '011-0000000', 42, 'miguel@gmail.com', 'UVWXY346', 5),
('Luis', 'Gómez', '35.235.224', '011-1212121', '011-3434343', 27, 'luis@gmail.com', 'ZABCDE679', 6),
('Ana', 'García', '40.235.224', '011-5656565', '011-7878787', 25, 'ana@gmail.com', 'ZABCDE680', 7),
('Roberto', 'Pérez', '41.235.224', '011-9898989', '011-2121212', 33, 'roberto@gmail.com', 'ZABCDE681', 8),
('Julia', 'Suárez', '42.235.224', '011-1212122', '011-3434344', 26, 'julia@gmail.com', 'ZABCDE682', 9),
('Alberto', 'Díaz', '43.235.224', '011-5656566', '011-7878788', 28, 'alberto@gmail.com', 'ZABCDE683', 10);


INSERT INTO Viajes (IdDireccionesOrigenDestino, KmsRecorridos, IdCliente, IdCamion, IdConductor,
                    FechaSalidaEst, FechaSalidaReal, FechaLlegadaEst, FechaLlegadaReal)
VALUES
(1, 500, 1, 1, 1, '2023-11-10', '2023-11-10', '2023-11-12', '2023-11-12'),
(2, 700, 2, 2, 2, '2023-11-15', '2023-11-15', '2023-11-18', '2023-11-18'),
(3, 300, 3, 3, 3, '2023-11-20', '2023-11-20', '2023-11-22', '2023-11-22'),
(4, 600, 4, 4, 4, '2023-11-25', '2023-11-25', '2023-11-28', '2023-11-28'),
(5, 800, 5, 5, 5, '2023-11-30', '2023-11-30', '2023-12-03', '2023-12-03'),
(6, 400, 6, 6, 6, '2023-12-05', '2023-12-05', '2023-12-07', '2023-12-07'),
(1, 550, 1, 1, 1, '2023-12-10', '2023-12-10', '2023-12-12', '2023-12-12'),
(2, 720, 2, 2, 2, '2023-12-15', '2023-12-15', '2023-12-18', '2023-12-18'),
(3, 320, 3, 3, 3, '2023-12-20', '2023-12-20', '2023-12-22', '2023-12-22'),
(4, 610, 4, 4, 4, '2023-12-25', '2023-12-25', '2023-12-28', '2023-12-28');
