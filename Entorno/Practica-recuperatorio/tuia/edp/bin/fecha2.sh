if [ $1 -gt 1 ] && [ $1 -le 31 ]; then
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

