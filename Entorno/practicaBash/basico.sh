#Si o si tiene que arrancar con la siguiente linea:
#!bin/bash

#los comentarios son como en python

# Variables
nombre="juan"
edad=25
#MUY IMPORTANTE QUE ESTE TODO JUNTO SIN ESPACIOS, EN DECLARACION DE VARIABLE
#NO CAMBIA LAS COMILLAS DOBLES DE LAS SIMPLES PERO EN LOS ECHO SI
#para acceder al valor de una variable se usa el signo dolar

echo "hola, $nombre. Tenes $edad años"

#para ejecutar el script se usa el comando bash
#bash basico.sh

#$0 es el nombre del script
#$1 es el primer parametro
#$2 es el segundo parametro
#etc
#$@ son todos los parametros pasados al script
#como una lista de elementos separados por espacios
#$* es lo mismo que $@ pero como un solo string
#$# es la cantidad de parametros pasados al script

echo "El script se llama: $0"
echo "El primer argumento es: $1"
echo "Todos los argumentos: $@"
echo "Número total de argumentos: $#"

#./basico.sh arg1 arg2 arg3

#se obtiene lo siguiente
#El script se llama: ./basico.sh
#El primer argumento es: arg1
#Todos los argumentos: arg1 arg2 arg3
#Número total de argumentos: 3

#COMANDO EXPR
resultado=$(expr 2 + 2)
echo "Suma: $resultado" #resultado es 4

#DOBLE PARENTESIS
resultado=$((10 - 2))
echo "Resta: $resultado" # Resultado: 8

#LET
let resultado="4 * 3"
echo "Multiplicación: $resultado" # Resultado: 12

#COMANDO BC
resultado=$(echo "scale=2; 10 / 3" | bc)
echo "División: $resultado" # Resultado: 3.33
