SELECT COUNT(*) AS TotalViajes
FROM Viajes v
JOIN Direcciones d ON v.IdDireccionOrigen = d.Id
JOIN Ciudades c ON d.IdCiudad = c.Id
JOIN Provincias p ON c.IdProvincia = p.Id
WHERE p.Provincia = 'Santa Fe';


SELECT TOP 3 cond.Nombre AS NombreConductor, SUM(v.KmsRecorridos) AS TotalKilometros
FROM Viajes v
JOIN Conductores cond ON v.IdConductor = cond.Dni
WHERE YEAR(v.FechaSalidaEst) = 2023
GROUP BY cond.Nombre
ORDER BY TotalKilometros DESC;

SELECT v.IdConductor, cond.nombre AS NombreConductor, v.Kmsrecorridos, v.FechaSalidaEst AS ViajesRecientes
FROM Viajes v
JOIN Conductores cond ON v.IdConductor = cond.dni
WHERE YEAR(v.FechaSalidaEst) = 2023
ORDER BY v.KmsRecorridos DESC;