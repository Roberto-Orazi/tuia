def funcion(contador:int):
    if contador == 0:
        print('contador',contador)
        return
    print('contador antes recursivo', contador)
    funcion(contador-1)
    print('contador despues')
    print(contador)

funcion(5)