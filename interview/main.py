from collections import Counter
import os
from typing import Any

print("Ruta absoluta a donde estas parado:", os.getcwd())


def son_anagramas(palabra1: str, palabra2: str) -> bool:
    """
    Esta funcion devuelve true o false dependiendo si la palabra 1 o 2 son anagramas o no
    """
    return Counter(palabra1.lower()) == Counter(palabra2.lower())


def main(nombre_archivo: str) -> None:
    """
    La funcion main imprime las 2 palabras y dice si son anagramas o no, y imprime la cantidad total de palabras, las
    que fueron anagramas y las que no.
    """
    contador = 0
    try:
        with open(nombre_archivo, "r") as file:
            lineas = file.readlines()

        if not lineas:
            print("El archivo está vacío.")
            return

        for linea in lineas:
            linea = linea.strip()  # El metodo split elimina los espacios y genera una

            if linea:
                palabra1, palabra2 = linea.split(" : ")
                if son_anagramas(palabra1, palabra2):
                    contador += 1
                    print(f"Palabra 1: {palabra1}, Palabra 2: {palabra2} son anagramas")

                else:
                    print(
                        f"Palabra 1: {palabra1} y Palabra 2: {palabra2} no son anagramas"
                    )

        print(
            "La cantidad total de anagramas fue:",
            contador,
        )

    except FileNotFoundError:
        print("Error, el archivo no existe o el nombre está mal.")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")


nombre_archivo = input(
    "Ingresa el nombre del archivo, acordate estar parado en la ruta: "
)

main(nombre_archivo)
