def funcion(contador):
    if contador == 0:
        return
    print(contador)
    funcion(contador-1)
    print(contador)

funcion(5)

def g(xs:list,n:int):
    if len(xs)==0:
        return False
    if xs[0]==n:
        return True
    return g(xs[1:],n)

lista_ejemplo = [1, 2, 3, 4, 5]
valor_buscado = 3
resultado = g(lista_ejemplo, valor_buscado)
print(resultado)