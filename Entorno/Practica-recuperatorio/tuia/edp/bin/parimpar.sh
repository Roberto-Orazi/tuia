if [ $# -eq 0 ]; then
    echo "No se recibieron argumentos"
elif [ $(($# % 2)) -eq 0 ]; then
    echo "Se recibieron una cantidad par de argumentos"
else
    echo "Se recibieron una cantidad impar de argumentos"
fi
