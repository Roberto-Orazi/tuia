#!/bin.bash
edad= $20

if [$edad -eq 18]; then #eq es igual que
    echo "Tienes 18 años"
elif [$edad -gt 18]; then #gt es mayor que
    echo "Eres mayor de edad"
elif [$edad -lt 18]; then #lt es menor que
    echo "Eres menor de edad"
else                      # el ultimo elif esta demas pero es para explicar el lt
    echo "No se que eres" #ACA IRIA ES MENOR DE EDAD PERO AGREGAMOS EL LT PARA EXPLICARLO
fi                        #fin del if

#COMPARACIONES
# -eq (equal) es igual que
# -ne (not equal) es distinto que
# -gt (greater than) es mayor que
# -lt (less than) es menor que
# -ge (greater or equal) es mayor o igual que
# -le (less or equal) es menor o igual que
# -z (zero) es cadena vacia
# -n (not zero) es cadena no vacia
# = es igual que
# != es distinto que
# -e (exist) es archivo existe
# -f (file) es archivo comun
# -d (directory) es directorio
# -r (read) es archivo tiene permiso de lectura
# -w (write) es archivo tiene permiso de escritura
# -x (execute) es archivo tiene permiso de ejecucion
# -nt (newer than) es archivo1 mas nuevo que archivo2
# -ot (older than) es archivo1 mas viejo que archivo2
# -ef (equal file) es archivo1 es el mismo que archivo2

#OPERADORES LOGICOS
# && es and
if [ $edad -gt 18 ] && [ $nombre = "Juan" ]; then
    echo "La edad es mayor a 18 y el nombre es Juan."
fi
# || es or
if [ $edad -eq 18 ] || [ $nombre = "Juan" ]; then
    echo "La edad es igual a 18 o el nombre es Juan."
fi
# ! es not
if ! [ $edad -gt 18 ]; then
    echo "La edad no es mayor a 18."
fi

#COMPARADORES
# == es igual
if [ $edad == 18 ]; then
    echo "La edad es igual a 18."
fi
# != es distinto
if [ $edad != 18 ]; then
    echo "La edad es distinta a 18."
fi
# < es menor que
if [ $edad -lt 18 ]; then
    echo "La edad es menor a 18."
fi
# > es mayor que
if [ $edad -gt 18 ]; then
    echo "La edad es mayor a 18."
fi
# <= es menor o igual que
if [ $edad -le 18 ]; then
    echo "La edad es menor o igual a 18."
fi
# >= es mayor o igual que
if [ $edad -ge 18 ]; then
    echo "La edad es mayor o igual a 18."
fi

#ANIDACIONES DE CONDICIONALES
edad=25
genero="masculino"

if [$edad -ge 18]; then
    echo "Eres mayor de edad"

    if [$genero = "masculino"]; then
        echo "Eres hombre y mayor de edad"
    else
        echo "Eres mujer y mayor de edad"
    fi
else
    echo "Eres menor de edad"
fi

