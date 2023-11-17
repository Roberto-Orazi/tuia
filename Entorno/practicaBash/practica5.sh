#1

echo "hello world"

#2
echo "ingresar un mes"
read mes
echo "ingresar un ano"
read ano
echo "Hoy es $mes/$ano"

#3
echo "ingresar un numero"
read numero
i=0
while [ $numero != '' ]; do
    echo "ingresar un numero"
    read numero
    i=$((i + 1))
done
par=$(($i%2))
if [ $par -eq 0 ]; then
    echo "el numero de numeros ingresados es par"
else
    echo "el numero de numeros ingresados es impar"
fi

#Crearunscriptquerecibaunacantidaddeargumentos(nolimitado)ylosescriba (todos juntos) en un archivo llamado /tmp/args. Finalmente mostrar el archivo.
for i in "$@"; do
    echo "$i" >> /tmp/args
done

