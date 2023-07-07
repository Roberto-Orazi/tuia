#!bin/bash
#PRACTICA 5

#EJERCICIO 1
#CREAR LOS DIRECTORIOS tuia/edp/bin en el directorio actual
mkdir -p tuia/edp/bin
#Posteriormente crear un script en ese directorio que muestre por pantalla "hello world".
#agregar el directorio a la variable PATH para poder ejecutar el script como un comando corriente
echo 'echo "hello world"' > tuia/edp/bin/hello.sh
chmod +x tuia/edp/bin/hello.sh
export PATH=$PATH:$(pwd)/tuia/edp/bin

#EJERCICIO 2
#crear un script que reciba exactamente dos argumentos, el primero correspondera a un numero de mes y el segundo a un año.
#debera mostrar por pantalla el calendario del mes y año con el dia destacado
#tip analizar el comando cal
mes=$1
anio=$2
echo 'cal $1 $2' > tuia/edp/bin/calendario.sh #NO ANDA PORQUE NO ME ANDA EL CAL
chmod +x tuia/edp/bin/calendario.sh

#EJERCICIO 3
#crear un script que reciba una cantidad e argumentos is ndefinir e inidque si recibio una cantidad par o impar
echo 'if [ $# -eq 0 ]; then
    echo "No se recibieron argumentos"
elif [ $(($# % 2)) -eq 0 ]; then
    echo "Se recibieron una cantidad par de argumentos"
else
    echo "Se recibieron una cantidad impar de argumentos"
fi' > tuia/edp/bin/parimpar.sh
chmod +x tuia/edp/bin/parimpar.sh

#EJERCICIO 4
#Crear un script que reciba una cnatidad de argumentos no limitados y los escriba todos juntos en un archivo llamado /tmp/args. Finalmente mostrar el archivo
echo 'echo "$@" > /tmp/args
cat /tmp/args' > tuia/edp/bin/args.sh
chmod +x tuia/edp/bin/args.sh

#EJERCICIO 5
echo 'dia=$1;mes=$2;anio=$3
if [ $1 -gt 1 ] && [ $1 -le 31 ]; then
    echo "El dia es correcto"
else
    echo "El dia es incorrecto"
fi
if [ $2 -gt 1 ] && [ $2 -le 12 ]; then
    echo "El mes es correcto"
else
    echo "El mes es incorrecto"
fi
if [ $3 -gt 1 ] && [ $3 -le 2023 ]; then
    echo "El año es correcto"
else
    echo "El año es incorrecto"
fi' > tuia/edp/bin/fecha.sh
chmod +x tuia/edp/bin/fecha.sh

#EJERCICIO 5 v2
echo 'if [ $1 -gt 1 ] && [ $1 -le 31 ]; then
    if [ $2 -gt 1 ] && [ $2 -le 12 ]; then
        if [ $3 -gt 1 ] && [ $3 -le 2023 ]; then
            echo "La fecha es correcta"
        else
            echo "La fecha no es correcta"
        fi
    else
        echo "La fecha no es correcta"
    fi
else
    echo "La fecha no es correcta"
fi
' > tuia/edp/bin/fecha2.sh
chmod +x tuia/edp/bin/fecha2.sh

#Ejercicio6
#crear un script que reciba la ruta absoluta a un arhcivo e indique si existe o no y si se trata de un archivo regular o un directorio
echo 'if [ -e $1 ]; then
    echo "El archivo existe"
    if [ -f $1 ]; then
        echo "Es un archivo regular"
    elif [ -d $1 ]; then
        echo "Es un directorio"
    fi
else
    echo "El archivo no existe"
fi' > tuia/edp/bin/existe.sh
chmod +x tuia/edp/bin/existe.sh

#Ejercicio7
#crear un script qeu reciba una unica cadena como argumento y determine si esa cadena es o no palindromo
#tip usar el comando rev
echo 'if [ $(echo $1 | rev) = $1 ]; then
    echo "Es palindromo"
else
    echo "No es palindromo"
fi' > tuia/edp/bin/palindromo.sh
chmod +x tuia/edp/bin/palindromo.sh

#Ejercicio8
#crear un script que reciba dos rutas a archivos de texto y que indique si estos archivos tienen la misma cantidad de lineas. validar que los archivos existen y se pueden leer
