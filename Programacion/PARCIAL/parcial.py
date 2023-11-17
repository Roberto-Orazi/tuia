el=[1,2,3,4,5]
subel=el[:-3]
print(subel[0],subel[1])
subel2=el[-2:1]
print(subel2)


A = int(input('Ingrese un numero '))
B = int(input('Ingrese un numero '))
C = int(input('Ingrese un numero '))

lista = [A,B,C]
print(lista)
lista.sort()
print(lista)
tupla=lista
tuple(tupla)
print(tupla)

tupla=('ficon trolo')
print(tupla)

def divisor(m,n):
    if(m%n == 0):
        return True
    else:
        return False


def suma(m,n):
    sum=0
    for i in range(1, n):
        if divisor(m,i):
            sum+=i
    return sum

wachin=suma(12,6)
print(wachin)
