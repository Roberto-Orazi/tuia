# Prueba tecnica

Primero tenemos que ingresar el nombre del archivo, si no encuentra el archivo o si el archivo esta vacio tambien hay
que tenerlo en cuenta. En mi caso voy a usar os para tener la ruta absoluta ya que muchas veces pasa que corremos el
codigo desde otra ruta entonces os nos va a dar la ruta exacta donde nos vamos a parar.

Tenemos un txt con 2 palabras separadas por : en cada linea, por ende vamos a tener que guardar esas 2 palabras y
verificar la cantidad de veces que aparece cada letras. Para esto vamos a usar counter de
python(https://www.geeksforgeeks.org/python-counter-objects-elements/).

Primero tenemos que separar las palabras por linea con un for, y luego vamos a hacer un
split(https://www.freecodecamp.org/espanol/news/metodos-de-cadenas-split-y-join-en-python/) con el : para separar las 2
palabras una vez que tenemos esas 2 palabras separadas vamos a usar una funcion o metodo de python llamado counter, esta
funcion nos va a devolver true o false ya que va a ser una comparacion de las 2 palabras por separado, una vez que
usamos la funcion y nos devuelve true vamos a poner un contador para sumar la cantidad de anagramas que tenemos en
nuestro archivo y tenemos que imprimir todas las pares de palabras y decir si son o no anagrama.

Para testear que la funcion ande bien y ahorrarme usar la funcion counter podria verificar primero el largo de las
palabras

```Python
if len(palabra1) == len(palabra2):
    if son_anagramas(palabra1, palabra2):
        contador += 1
        print(f"Palabra 1: {palabra1}, Palabra 2: {palabra2} son anagramas")
else: print(f"Palabra 1: {palabra1} y Palabra 2: {palabra2} no son anagramas")
```
