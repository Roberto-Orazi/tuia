CREATE TABLE[dbo].[Pacientes](
[Id][int] IDENTITY(1,1) NOT NULL,
[Nombre][nchar](10) NULL,
[Apellido][nchar](10) NULL,
[DNI][int] NULL,
[Altura][float] NULL,
[Peso][float] NULL
) ON [PRIMARY]
GO
