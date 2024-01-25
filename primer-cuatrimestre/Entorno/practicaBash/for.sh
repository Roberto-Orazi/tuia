#!/bin.bash

# Ejemplo: Iterar sobre una lista de números
for i in 1 2 3 4 5; do
    echo $i
done

#Ejemplo: Iterar sobre una lista almacenada en una variable
nombres=("juan" "maria" "pedro")
for nombre in "${nombres[@]}"; do
    echo $nombre
done

# Ejemplo: Iterar sobre una secuencia numérica
for i in {1..10}; do
    echo $i
done
