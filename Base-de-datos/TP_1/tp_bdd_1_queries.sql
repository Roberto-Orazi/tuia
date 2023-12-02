SELECT COUNT(*) AS TotalViajes
FROM Viajes v
JOIN Direcciones d ON v.IdDireccionOrigen = d.Id
JOIN Ciudades c ON d.IdCiudad = c.Id
JOIN Provincias p ON c.IdProvincia = p.Id
WHERE p.Provincia = 'Santa Fe';

SELECT
    V.Id AS IdViaje,
    C.Nombre AS NombreCliente,
    CO.Ciudad AS CiudadOrigen,
    CD.Ciudad AS CiudadDestino,
    V.KmsRecorridos,
    V.FechaSalidaEst,
    V.FechaLlegadaEst
FROM Viajes V
    JOIN Clientes C ON V.IdCliente = C.Id
    JOIN DireccionesOrigenDestino DOD ON V.IdDireccionesOrigenDestino = DOD.Id
    JOIN Ciudades CO ON DOD.IdOrigen = CO.Id
    JOIN Ciudades CD ON DOD.IdDestino = CD.Id
WHERE CO.IdProvincia = (SELECT Id FROM Provincias WHERE Provincia = 'Córdoba')
    AND V.FechaSalidaEst >= '2023-01-01'
    AND V.FechaSalidaEst < '2023-07-01';


SELECT TOP 3
    cond.Nombre AS
    NombreConductor,
    SUM(v.KmsRecorridos) AS TotalKilometros
FROM Viajes v
    JOIN Conductores cond ON v.IdConductor = cond.Dni
WHERE YEAR(v.FechaSalidaEst) = 2023
GROUP BY cond.Nombre
ORDER BY TotalKilometros DESC;


SELECT
    v.IdConductor,
    cond.nombre AS NombreConductor,
    v.Kmsrecorridos, v.FechaSalidaEst AS ViajesRecientes
FROM Viajes v
JOIN Conductores cond ON v.IdConductor = cond.dni
WHERE YEAR(v.FechaSalidaEst) = 2023
ORDER BY v.KmsRecorridos DESC;