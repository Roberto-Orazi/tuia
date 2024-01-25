dia=$1;mes=$2;anio=$3
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
fi
