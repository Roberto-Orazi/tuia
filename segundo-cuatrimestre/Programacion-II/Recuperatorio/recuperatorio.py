'''
1. Crear una clase caja para representar cuanto dinerop hay en una caja de un negocio, desglosado por tipo de billete, hay 6 billetes de 500, 7 de 100 etc, las denominaciones son
1, 2, 5, 10, 20, 50, 100, 200, 500, 1000
para crear el objeto se crea asi:
c=caja({500:6,200:4})
'''
class Caja:
    def __init__(self,billetes:dict)->None:
        if billetes is not None:
            self.billetes=billetes
        else:
            self.billetes={1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0, 1000: 0}

    def agregarBilletes(self, agregrar_billetes:dict):
        for denominacion, cantidad in agregrar_billetes.items():
            if denominacion in self.billetes:
                print(denominacion)
                self.billetes[denominacion]+=cantidad
            else:
                print(f"Denominación {denominacion} no válida.")

    def sacarBilletes(self, vuelto: int) -> dict:
        def es_solucion(solucion_actual: dict, vuelto_restante: int) -> bool:
            return vuelto_restante == 0

        def elegir_candidato(problema: dict) -> int:
            return max(problema)

        def es_factible(solucion: dict, vuelto_restante: int) -> bool:
            return sum(solucion.values()) <= vuelto_restante

        def resolver(problema: dict, vuelto_restante: int) -> dict:
            solucion = {}
            while vuelto_restante > 0 and not es_solucion(solucion, vuelto_restante):
                x = elegir_candidato(problema)
                if es_factible(solucion, vuelto_restante):
                    if x in problema and problema[x] > 0:
                        solucion[x] = solucion.get(x, 0) + 1
                        problema[x] -= 1
                        vuelto_restante -= x
                    else:
                        break
                else:
                    break
            return solucion if es_solucion(solucion, vuelto_restante) else {}

        resultado = resolver(self.billetes.copy(), vuelto)
        return resultado


    def sumarBilletes(self)->int:
        total=0
        for denominacion,cantidad in self.billetes.items():
            total+=(denominacion*cantidad)
        return total

caja_negocio = Caja({500: 6, 200: 4, 100: 10, 50: 5, 20: 20, 10: 10, 5: 50, 2: 100, 1: 200})
print("Caja antes de realizar transacciones:", caja_negocio.billetes)

caja_negocio.agregarBilletes({100: 10, 20: 5})
print("Caja después de agregar billetes:", caja_negocio.billetes)

# Obtener billetes para el vuelto
vuelto = 120
billetes_necesarios = caja_negocio.sacarBilletes(vuelto)
print(f"Billetes necesarios para un vuelto de {vuelto}:", billetes_necesarios)

total_billetes = caja_negocio.sumarBilletes()
print("Valor total de billetes en la caja:", total_billetes)

'''
2. Escribe un metodo invertir de la clase ListaEnlazada que invierta el orden de la lista, puede considerar que estan definidos todos lso metodos de la interfaz lista
'''
from typing import Any

class Nodo:
    def __init__(self,dato:Any=None, prox: 'Nodo' | None = None):
        self.dato=dato
        self.prox=prox

    def __str__(self):
        return str(self.dato)

class ListaEnlazada:
    def __init__(self)->None:
        self.prim=None
        self.len=0

    def insert(self,i:int,x:Any)->None:
        if i < 0 or i > self.len:
            print('Posicion invalida')
            return

        nuevo= Nodo(x)
        if i == 0:
            nuevo.prox=self.prim
            self.prim=nuevo
        else:
            n_ant=self.prim
            for pos in range(1,i):
                n_ant=n_ant.prox

            nuevo.prox = n_ant.prox
            n_ant.prox=nuevo

        self.len+=1

    def pop(self, i:int | None = None)->Any:
        """
        Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se muestra un mensaje de error y se retorna inmediatamente.
        Si no se recibe la posición, devuelve el último elemento.
        """
        if i is None:
            i=self.len-1

        if i<0 or i>=self.len:
            print('Posicion invalida')
            return

        if i==0:
            dato=self.prim.dato
            self.prim=self.prim.prox
            # Saltea la cabeza de la lista

        else:
            n_ant=self.prim # Buscamos nodos en pos i - 1 y i
            n_act=n_ant.prox
            for pos in range(1,i):
                n_ant=n_act
                n_act=n_ant.prox

            dato=n_act.dato
            n_ant.prox=n_act.prox # Guardamos el dato y descartamos el nodo

        self.len-=1
        return dato

    def remove(self,x:Any)->None:
        """
        Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, imprime un mensaje de error
        y retorna inmediatamente.
        """
        if self.len==0:
            print('La liista esta vacia')
            return

        if self.prim.dato==x:
            self.prim=self.prim.prox
            # Saltea la cabeza de la lista

        else:
            n_ant=self.prim
            n_act=n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant=n_act
                n_act=n_ant.prox

            if n_act==None:
                print('el valor no esta en la lista')
                return
            # Ahi buscamos el nodo anterior al que contiene a x(n_ant)

        n_ant=n_act.prox
        self.len-=1
        # Por ultimo descartamos el nodo

