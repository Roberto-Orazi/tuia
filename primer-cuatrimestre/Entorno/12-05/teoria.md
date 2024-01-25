# ejercicio 1
Crear un script para mostrar por pantalla los numeros pares del n al 2
n es un argumento recibido por la linea de comandos y debe ser un entero mayor a 2
````
#OPCION 1
LIMIT=$1

if [$(($LIMIT%2)) -eq 1]
then
    LIMIT=$(($LIMIT -1))
    echo $LIMIT
fi
#OPCION 2
for i in $(seq $LIMIT -2 2)
do
    echo $i
done
````