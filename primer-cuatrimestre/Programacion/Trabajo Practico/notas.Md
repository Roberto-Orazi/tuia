## ARCHIVO CSV
- Para abrir
  ````
  Crear archivo
  open('datos.csv', 'x')
  Leer archivo
  open('datos.csv', 'r')
  Escribir archivo
  open('datos.csv', 'w')
  Añadir cosas al final del archivo, y si esta vacio lo agrega
  open('datos.csv', 'a')

  archivo = open('datos.csv', 'w')
  archivo.close() Siempre hay que cerrar el archivo para guardar los cambios
  ````

## DESCARGAR ARCHIVOS CSV DESDE URL

````
def descargarCsv(url: str, archivo_salida: str) -> None:
  consulta =
````