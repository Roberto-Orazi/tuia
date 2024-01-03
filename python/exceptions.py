### Exception handling ###

numberOne=5
numberTwo=1
numberTwo='1'

'''if numberOne>3 :
    sum=numberOne+numberTwo
    # Aca va a tirar error ya que esta mal siempre y cuando pase lo primero, como no pasa porque le pusimos un verificador.
    # En este caso se usa try except
else:
    print('No se cumplio la condicion')'''

try:
    print(numberOne+numberTwo)
    # Si ejecuta lo de arriba sin errores printea correctamente
    print('Se ha ejecutado bien el try')
except:
    # Esto se ejecuta si no se ejecuta el try porque tira error
    print('Se ha producido un error')
else:
    # Esto se ejecuta si y solo si se ejecuta el try.
    print('La ejecucion continua correctamente')
finally:
    # Esto se ejecuta siempre al final de todo se ejecute o no
    print('La ejecucion continua')