#!/bin.bash
exit [código]

# Verificar si el archivo existe
if [ -f archivo.txt ]; then
    echo "El archivo existe."
else
    echo "El archivo no existe."
    exit 1 # Salir con código de error 1
fi

# Realizar una operación y verificar el resultado
resultado=$(comando)
if [ $resultado -eq 0 ]; then
    echo "La operación fue exitosa."
    exit 0 # Salir con código de éxito 0
else
    echo "Ocurrió un error en la operación."
    exit 2 # Salir con código de error 2
fi
