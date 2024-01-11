### Challenges ###
"""
100 veces del 1 al 100 imprimir el numero y si es multiplo de 3 imprime fizz, si es de 5 imprime buzz multiplos de 3 y 5
a la vez fizzbuzz
"""


def fizz_buzz(num):
    cont = 1
    while cont <= num:
        if cont % 3 == 0 and cont % 5 == 0:
            print(cont, "fizzbuzz")
        elif cont % 3 == 0:
            print(cont, "fizz")
        elif cont % 5 == 0:
            print(cont, "buzz")
        else:
            print(cont)
        cont += 1


fizz_buzz(100)


def fizz_buzz_for(num: int):
    for i in range(1, num + 1, 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


fizz_buzz_for(100)

"""
Anagrama recibe 2 palabras y devuelve true si es anagrama y false si no son anagrama no importa si existen o no las
palabras tienen que tener las mismas letras en distinto orden no pueden ser iguales las palabras
"""


def anagrama(first_word: str, second_word: str) -> bool:
    """
    Esto nos dice si las 2 palabras ingresadas son un anagrama
    """
    if first_word.lower() == second_word.lower():
        return False
    return sorted(first_word.lower()) == sorted(second_word.lower())


es_anagrama = anagrama("Amor", "Roma")
print(es_anagrama)


"""
Fibonacci Imprimir los 50 con secuencia de fibonacci
"""


def fibonacci(num: int) -> int:
    """
    Secuencia de fibonacci
    """
    prev = 0
    next = 1
    for i in range(0, num + 1, 1):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


print(fibonacci(50))

"""
Numero primo
imprimir los numeros primos entre 1 y 100
"""


def prime_number(num:int)->int:
    """
    Si es numero primo imprimirlo
    """
    for i in range(2, num, 1):
        if i % 2 == 0:
            if i == 2:
                print(i)
            else:
                pass
        elif i % 3 == 0:
            if i == 3:
                print(i)
            else:
                pass
        else:
            print(i)
    print('Final de lista')

prime_number(20)

def is_prime(number:int)->bool:
    """
    Determina si es primo, osea si se divide solo por si mismo y por 0
    """
    if number < 2:
        return False

    for index in range(2,number):
        if number % index == 0:
            return False

    return True

def prime_number_moure(number:int=0)->int:
    for number in range(1,101):
        if number >= 2:
            is_divisible=False

            for index in range(2,number):
                if number%index==0:
                    is_divisible=True
                    break

            if not is_divisible:
                print(number)
prime_number_moure()

def reversed_text(text:str)->str:
    reversed_chain=''
    for letra in text:
        reversed_chain=letra+reversed_chain
    return reversed_chain

print(reversed_text('hola como estas'))
