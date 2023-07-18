import subprocess
import csv
import matplotlib.pyplot as plt

gdown_command = 'gdown --fuzzy https://drive.google.com/file/d/1WWvf6yn5oS1xarapKnwr3s8l2wKWtd7d/view?usp=drive_link'
subprocess.call(gdown_command, shell=True)


wget_command = 'wget https://datos.yvera.gob.ar/dataset/09679fe3-7379-481d-a36a-6b1e3d7374b1/resource/9d4db872-0a51-4042-9daa-e55bc7a3044c/download/viajes_origen_destino_mes.csv --no-check-certificate -O previaje.csv'
subprocess.call(wget_command, shell=True)




def openFile(nombre_archivo) -> list[list[str]]:
    """
    Lee datos del archivo de entrada y retorna
    una lista con la informacion que se va a usar
    en el trabajo.
    """
    datos = []
    with open (nombre_archivo, 'r') as data:
        lector = csv.reader(data)
        next(lector)
        for fila in lector:
            datos.append(fila)
    return datos

datos_provincia = openFile("coordenadas_provincias.csv")
datos_previaje = openFile("previaje.csv")


def listToDict(datos) -> list[dict[str]]:
    """
    Toma el resultado de la lectura de datos como argumento
    y devuelve una lista de diccionarios.
    La clave es el valor en el indice 0, y los valores asociados
    son una tupla con el resto de los elementos de la lista.
    """
    provinciaList = []

    for fila in datos_provincia:
        provincia = fila[0]
        coordenada = (fila[1], fila[2])
        dicc = {provincia: coordenada}
        provincia.append(dicc)
    return provinciaList


class Provincia:
    """
    Esta clase representa una provincia.
    Sus atributos son:
        nombre: str
        coordenada: tuple
    """
    def __init__(self,
                 nombre: str,
                 coordenada: tuple
                 ) -> None:
        self.nombre = nombre
        self.coordenada = coordenada
    def __str__(self) -> str:
        return f"Provincia: {self.nombre} - Coordenada: {self.coordenada}"


def estructura(datos) -> dict[list[str]]:
    """
    Crea un diccionarios como estructura de datos para trabajar
    el archivo, donde hay una lista por cada uno de los dataset
    """
    inicio = []
    origen = []
    destino = []
    num_viajes = []
    num_viajeros = []
    num_edicion = []

    datos = datos[1:]

    for fila in datos:
        inicio.append(fila[0])
        origen.append(fila[1])
        destino.append(fila[2])
        num_viajes.append(fila[3])
        num_viajeros.append(fila[4])
        num_edicion.append(fila[5])

    datos_str = {
        "mes_inicio": inicio,
        "provincia_origen": origen,
        "provincia_destino": destino,
        "viajes": num_viajes,
        "viajeros": num_viajeros,
        "edicion": num_edicion
    }

    return datos_str


def datos_relevantes(estructura_datos: dict, *args) -> dict:
    """
    Devuelve os datos de determinados encabezados pasados por parametro
    """
    datos_relev = {}
    for arg in args:
        for encabezado, valores in estructura_datos.items():
            if arg == encabezado:
                datos_relev[encabezado] = valores
    return datos_relev


def mas_viajeros(datos_str:dict, mes, año):
    """
    Calcula cual fue la provincia que mas viajeros recibio,
    en un mes y año indicados como parametros
    """
    prov_viajeros = {}

    for fila in datos_str:
        mes_inicio = fila[0]
        prov_destino = fila[2]
        viajeros_str = fila[4]

        if not viajeros_str.isdigit():
            continue

        viajeros_num = int(viajeros_str)

        if mes_inicio == f"{mes}-{año}":
            if prov_destino in prov_viajeros:
                prov_viajeros[prov_destino] += viajeros_num
            else:
                prov_viajeros[prov_destino] = viajeros_num
    if not prov_viajeros:
        return "No hay datos disponibles para el mes y año especificados"

    prov_mas_viajeros = max(prov_viajeros, key=prov_viajeros.get)
    return prov_mas_viajeros


def calcular_promedio(datos_relevantes:dict, prov_origen:str) -> int:
    """
    Crear una funcion que calcuyle el promedio de viajeros por viaje
    en una provincia de origen especifica
    """
    total_viajeros = 0
    total_viajes = 0
    for value in range(len(datos_relevantes["provincia_origen"])):
        if prov_origen == datos_relevantes["provincia_origen"][value]:
            total_viajeros += int(datos_relevantes["viajeros"][value])
            total_viajes += int(datos_relevantes["viajes"][value])
    if total_viajes != 0:
        promedio = round((total_viajeros / total_viajes), 2)
        return f"El promedi ode viajeros por viaje en {prov_origen} fue: {promedio}"
    else:
        return f"No hay suficientes datos para calcualr el promedio en {prov_origen}"


class Viaje:
    """
    Esta clase representa un viaje, contiene los datos relevantes
    al analisis
    """
    def __init__(self, mes_inicio, provincia_origen, provincia_destino, viajes, viajeros, edicion):
        self.mes_inicio = mes_inicio
        self.provincia_origen = provincia_origen
        self.provincia_destino = provincia_destino
        self.viajes = viajes
        self.viajeros = viajeros
        self.edicion = edicion

    def __str__(self):
        return f"Viaje: {self.mes_inicio}, {self.provincia_origen}, {self.provincia_destino}, {self.viajes}, {self.viajeros}, {self.edicion}"


def datos_viajes(datos_relevantes:dict):
    """
    Crea una nueva estructura de datos con viajes y edicion como parametros
    """
    viajes_edicion = {}
    for i in range(len(datos_relevantes["viajes"])):
        viajes = datos_relevantes["viajes"][i]
        edicion = datos_relevantes["edicion"][i]
        if viajes.isdigit():
            if edicion not in viajes_edicion:
                viajes_edicion[edicion] = int(viajes)
            else:
                viajes_edicion[edicion] += int(viajes)
    return viajes_edicion

def calcular_edicion():
    """
    Calcula el proemdi ode viajes por cada edicion y crea una lista
    para las etiquetas ediciones
    """
    