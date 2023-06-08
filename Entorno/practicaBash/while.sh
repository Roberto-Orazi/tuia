#!/bin.bash

# Ejemplo: Bucle while que cuenta hasta 5
contador=1
while [ $contador -le 5 ]; do
    echo $contador
    contador=$((contador + 1))
done
