create database recuperatorio

use recuperatorio

create table centrodesalud(
idcentro int primary key,
direccion varchar(20)
)

create table medico(
nombre varchar(20),
dni int primary key,
especialidad varchar(20),
matricula int,
)
create table centrosaludmedico(
idcentro int,
dnimedico int,
primary key(idcentro,dnimedico),
foreign key(idcentro) references centrodesalud(idcentro),
foreign key(dnimedico) references medico(dni),
)
create table paciente(
nombre varchar(20),
dni int primary key,
direccion varchar(20),
obrasocial int,
idmedico int,
foreign key(idmedico) references medico(dni)
);

create table consulta(
idconsulta int primary key,
fecha date,
dni int,
idcentrosalud int,
diagnostico varchar(20),
foreign key(dni) references paciente(dni),
foreign key(idcentrosalud) references centrodesalud(idcentro),
)

create table medicacion(
id int primary key,
idconsulta int,
descripcion varchar(20),
foreign key(idconsulta) references consulta(idconsulta),
)

create table programavacunacion(
id int primary key,
fechain date,
fechafin date,
descripcion varchar(20)
)

create table vacunacion(
id int primary key,
dni int,
fecha date,
idprograma int,
descripcion varchar(20),
foreign key(dni) references paciente(dni),
foreign key(idprograma) references programavacunacion(id)
);

-- Inserting data into centrodesalud table
INSERT INTO centrodesalud (idcentro, direccion) VALUES
(1, 'Direccion1'),
(2, 'Direccion2');

-- Inserting data into medico table
INSERT INTO medico (nombre, dni, especialidad, matricula) VALUES
('Dr. Smith', 123456789, 'Cardiologist', 78901234),
('Dr. Johnson', 987654321, 'Pediatrician', 56789012);

-- Inserting data into centrosaludmedico table
INSERT INTO centrosaludmedico (idcentro, dnimedico) VALUES
(1, 123456789),
(2, 987654321);

-- Inserting data into paciente table
INSERT INTO paciente (nombre, dni, direccion, obrasocial, idmedico) VALUES
('John Doe', 111222333, 'PatientAddress1', 123456, 123456789),
('Jane Doe', 444555666, 'PatientAddress2', 789012, 987654321),
('Pepe sanchez', 444555667, 'PatientAddress2', 789012, 987654321);


-- Inserting data into consulta table
INSERT INTO consulta (idconsulta, fecha, dni, idcentrosalud, diagnostico) VALUES
(1, '2023-01-01', 111222333, 1, 'Fever'),
(2, '2023-02-01', 444555666, 2, 'Cough');

-- Inserting data into medicacion table
INSERT INTO medicacion (id, idconsulta, descripcion) VALUES
(1, 1, 'Ibuprofen'),
(2, 2, 'Cough Syrup');

-- Inserting data into programavacunacion table
INSERT INTO programavacunacion (id, fechain, fechafin, descripcion) VALUES
(1, '2023-03-01', '2023-04-01', 'Flu Vaccination'),
(2, '2023-05-01', '2023-06-01', 'COVID-19 Vaccination');

-- Inserting data into vacunacion table
INSERT INTO vacunacion (id, dni, fecha, idprograma, descripcion) VALUES
(1, 111222333, '2023-03-15', 1, 'Flu Shot'),
(2, 444555666, '2023-05-15', 2, 'COVID-19 Vaccine');


-- queryesss

SELECT idcentro,paciente.nombre from centrodesalud
join consulta on consulta.idcentrosalud = centrodesalud.idcentro
join paciente on paciente.dni = consulta.dni
where paciente.nombre = 'Pepe sanchez'

SELECT descripcion from medicacion
join consulta on consulta.idconsulta = medicacion.idconsulta
join paciente on paciente.dni = consulta.dni
WHERE
paciente.nombre='Facundo conte'
AND
consulta.fecha>'2018-01-01'

SELECT count()