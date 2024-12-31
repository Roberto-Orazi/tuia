from collections import Counter
import os

print("Ruta absoluta a donde estas parado:", os.getcwd())


def are_anagrams(word1, word2):
    """
    Determinamos si son anagrama o no contando la cantidad de veces que se repite cada letra
    """
    return Counter(word1.lower()) == Counter(word2.lower())


def process_file(filename):
    """
    Leemos los pares de letras y usamos la funcion que creamos anteriormente para checkear si son anagramas.
    """
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        if not lines:
            print("El archivo esta vacio.")
            return

        anagram_count = 0
        for line in lines:
            if ":" in line:
                word1, word2 = map(str.strip, line.strip().split(":"))
                if are_anagrams(word1, word2):
                    print(f"{word1} : {word2} -> Anagrama")
                    anagram_count += 1
                else:
                    print(f"{word1} : {word2} -> No Anagrama")

        print(f"\nTotal de anagramas: {anagram_count}")

    except FileNotFoundError:
        print(
            "El archivo no se encontro, acordate de usar la ruta absoluta o pararte en la carpeta donde tenes los archivos antes de correr el archivo."
        )
    except Exception as e:
        print(f"Error: {e}")


filename = input(
    "Ingresa el nombre del archivo, recorda estar en la carpeta sino pone la ruta absoluta antes: "
).strip()
process_file(filename)
