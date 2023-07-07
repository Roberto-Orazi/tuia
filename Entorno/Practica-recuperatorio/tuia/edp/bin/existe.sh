if [ -e $1 ]; then
    echo "El archivo existe"
    if [ -f $1 ]; then
        echo "Es un archivo regular"
    elif [ -d $1 ]; then
        echo "Es un directorio"
    fi
else
    echo "El archivo no existe"
fi
