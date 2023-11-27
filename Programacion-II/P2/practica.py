# Por divide & conquer:
# Decir si una lista y un numero ese numero pertenece

def caso_base(problema):
    return len(problema) <= 1
def resolver_caso_base(problema):
    if len(problema) == 0:
        return False
    else:
        return problema[0]

def dividir(problema):
    mitad=len(problema)//2
    return(problema[:mitad], problema[mitad:])
def combinar(s1,s2):
    return s1 or s2
def resolver(problema, numero):
    if caso_base(problema):
        return resolver_caso_base(problema) == numero
    mitad1,mitad2=dividir(problema)
    s1,s2=resolver(mitad1,numero),resolver(mitad2,numero)
    return(combinar(s1,s2))



asd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 123, 123235234554, 123123, 23]
numeroasd = 233
if resolver(asd, numeroasd):
    print('Está en la lista.')
else:
    print('No está en la lista.')

