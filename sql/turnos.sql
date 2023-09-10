CREATE TABLE "usuarios" (
    "id_usuario" INTEGER,
    "nombre" TEXT DEFAULT 'Nombre',
    "apellido" TEXT,
    "edad" INTEGER
);

INSERT INTO usuarios (nombre,apellido,edad)
VALUES ('Roberto','Orazi',26),('Juan','Pepito',16);

CREATE TABLE "turnos_medicos" (
    "id_turno" INTEGER,
    "profesional" TEXT,
    "id_usuario" INTEGER,
    "motivo" TEXT,
    "horario" TEXT
)

INSERT INTO turnos_medicos (profesional,id_usuario,motivo,horario)
VALUES("Dr. Ramirez",6,"Dolor de panza", "12:30";)

SELECT * FROM turnos_medicos,usuarios;

