
#Ejercicio 1


class Dinero:
  """
  Concepto abstracto que no deberemos instanciar nunca directamente
  """

  def monto(self) -> float:
    """
    Todo dinero, cualquiera sea su procedencia, debería proveernos con algún metodo de saber cuál es el monto que este
    representa.

    Este método retorna un flotante con el valor total real que cada instancia tiene dentro.

    Será más claro cuando lo veamos en la práctica.
    """
    pass

  def __str__(self) -> str:
    """
    Por completitud, y para corroborar nuestros programas, nos gustaría que todas las clases que deriven Dinero tengan
    alguna forma de representación por pantalla.
    """
    pass



class Moneda(Dinero):

  Denominaciones = { 1, 2, 5 }

  def __init__(self, denominacion: int):
    if denominacion in Moneda.Denominaciones:
        self.denominacion = denominacion
    else:
        print(f'Ingrese un valor $1, $2 o $5, usted ingreso ${denominacion}')

  def monto(self) -> float:
      return self.denominacion


  def __str__(self) -> str:
    return(f'Moneda de {self.denominacion}')

moneda_5=Moneda(5)
valor_5=moneda_5.monto()
moneda_4=Moneda(4)
moneda_3=Moneda(3)
moneda_2=Moneda(2)
valor_2=moneda_2.monto()
moneda_1=Moneda(1)
valor_1=moneda_1.monto()

#Ejercicio 2
billetera=[valor_1,valor_1,valor_5,valor_1,valor_1,valor_2,valor_1,valor_1,valor_1,valor_5]

total_billetera=0
for i in billetera:
    print(billetera[i])
    total_billetera+=billetera[i]

print(total_billetera)

#Ejercicio 3
class Billete(Dinero):
    Denominaciones={10, 20, 50, 100, 200, 500, 1000}

    def __init__(self, denominacion: int):
        if denominacion in Moneda.Denominaciones:
            self.denominacion = denominacion
        else:
            print(f'Ingrese un valor $10, $20, $50, $100, $200, $500 o $1000 usted ingreso ${denominacion}')

    def monto(self) -> float:
      return self.denominacion


    def __str__(self) -> str:
        return(f'Moneda de {self.denominacion}')


billete_1=Billete(50)
valor_1=billete_1.monto()
billete_2=Billete(20)
billete_3=Billete(100)
billete_4=Billete(500)
