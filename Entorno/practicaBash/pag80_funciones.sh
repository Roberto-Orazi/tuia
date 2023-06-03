#!/bin/env bash

function mostrar_mult {
   mult=$(($1 * $2))
   echo "$1 x $2 = $mult"
}

read -p "Introduzca un numero positivo: " n

for i in $(seq 0 9);
do
  mostrar_mult $n $i
done

exit 0
