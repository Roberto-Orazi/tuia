#!/bin/bash
echo "Selecciona una opción (A, B, C):"
read opcion
case $opcion in
A)
    echo "Has seleccionado la opción A."
    # Código para la opción A
    ;;
B)
    echo "Has seleccionado la opción B."
    # Código para la opción B
    ;;
C)
    echo "Has seleccionado la opción C."
    # Código para la opción C
    ;;
*)
    echo "Opción inválida."
    ;;
esac

#Doble ;;
# Si se quiere ejecutar el mismo código para varias opciones,
#se puede hacer de la siguiente manera:
case variable in
    patron1)
        accion1 ;;
    patron2)
        accion2 ;;
    *)
        accion_defecto ;;
esac