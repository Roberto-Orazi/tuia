#!/usr/bin/env bash

if [ $# -lt 1 ]
then
   echo "Error de uso, debe indicar el archivo"
   echo "Ejemplo uso: $(basename $0) NOMBRE_ARCHIVO"
   exit 1
fi

FILE=$1

[ ! -e $FILE ] && echo "Archivo $FILE no existe!!" && exit 2

[ ! -f $FILE ] && echo "$FILE no es un archivo regular!!" && exit 3

MODES=$(stat --print="%a" $FILE)
SIZE=$(stat --print="%s" $FILE) #entrega tamaño en bytes
echo "El archivo $FILE tiene los permisos $MODES y su tamaño es de $((SIZE/1024))KB"
