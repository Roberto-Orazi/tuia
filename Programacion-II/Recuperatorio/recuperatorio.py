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