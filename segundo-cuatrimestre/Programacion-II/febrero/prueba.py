def recursiva(numero:int) -> str:
    if (numero==0):
        return "0"
    digito=numero%10
    print(digito)
    resto = recursiva(numero//10)
    print('resto',resto)
    return str(resto)+str(digito)

prueba=recursiva(10)

print(prueba)



def calcular(a,b):
    if a==0:
        return b+1
    if b==0:
        return calcular(a-1,1)
    intermedio=calcular(a,b-1)
    return calcular(a-1,intermedio)

print(calcular(1,0))


class Entidad:
    def __init__(self,vida_inicial:int):
        self.vida=vida_inicial

class Enemigo(Entidad):
    def __init__(self,vida_inicial:int):
        super().__init__(vida_inicial)

class Jugador(Entidad):
    def __init__(self,vida_inicial:int):
        super().__init__(vida_inicial)
        self.enemigos_golpeados=[]

    def golpeado(self,cuanto):
        self.vida-=cuanto

    def golpear(self,enemigo,cuanto):
        enemigo.vida -= cuanto
        self.enemigos_golpeados.append(enemigo)

enemigo1 = Enemigo(50)
jugador = Jugador(100)
jugador.golpear(enemigo1, 20)
print(enemigo1.vida)
print(jugador.enemigos_golpeados)


class Cosa:
    def __init__(self,valor):
        self.valor=valor

class Coleccion:
    def __init__(self):
        self.coleccion=[]

    def agregar_cosa(self,cosa:Cosa):
        self.coleccion.append(cosa)

cosa=Cosa('valor')
coleccion=Coleccion()
coleccion.agregar_cosa(cosa)