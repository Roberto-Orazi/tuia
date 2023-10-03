CREATE TABLE[dbo].[Turista](
[Id][int] IDENTITY(1,1) NOT NULL,
[Nombre completo][nchar](10) NULL,
[Nacionalidad][nchar](10) NULL,
[Edad][int] NULL,
[Ciudad destino][float] NULL,
[Pais destino][float] NULL,
[Fecha inxgreso][date] NULL,
[Fecha egreso][date] NULL,
[Empresa de transporte][float] NULL,
[Telefono][int](11) NULL,
[CUIT][int](10) NULL,
[Direccion][float] NULL
) ON [PRIMARY]
GO