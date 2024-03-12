# Buenas practicas

# Funciones de busqueda
- VLOOKUP(BUSCARV)
La funcion Vlookup o busqueda vertical, busca en una columna de una tabla un valor especifico y recupera un valor relacionado en otra columna.
```
VLOOKUP(valor_busqueda,rango,indice,[esta_ordenada])
```

- HLOOKUP(BUSCARH)
La funcion HLOOKUP o busqueda horizontal, hace lo mismo que vlookup pero horizontalmente
```
HLOOKUP(valor_busqueda,rango,indice,[esta_ordenada])
HLOOKUP(B5,B1:J3,2,FALSE)
```

- INDEX(INDICE)
Me da el valor que esta en esa celda
```
INDEX(rango,fila,columna)
INDEX(B5:B13,5,3)
```

- MATCH(COINCIDIR)
Devuelve la posicion(indice) de un valor dentro de un rango.
```
MATCH(valor_busqueda,rango,[tipo_coincidencia])
MATCH(H2,B3:B9,0) si ponemos 0 es busqueda exacta
```
Si ponemos 1 nos busca el mas cercano para arriba y si ponemos -1 el mas cercano para abajo


