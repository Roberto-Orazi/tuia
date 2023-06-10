#Ahora que sabemos acceder a los datos, les propongo crear una funcion que reciba como argumento el nombre del archivo y
#retorne una lista con los valores de las filas: Ejemplo: [['nombre', 'apellido', 'edad'],['Carlos', 'Baute', '49']]

def create_csv():
    ejemplo = open('ejemplo.csv', 'x')
    ejemplo.close()
create_csv()

def write_csv():
    ejemplo = open('ejemplo.csv', 'w')
    ejemplo.write('nombre,apellido,edad\n')
    ejemplo.write('Carlos,Baute,49\n')
    ejemplo.write('Ricardo,Montaner,62\n')
    ejemplo.write('Luis,Fonsi,43\n')
    ejemplo.close()
write_csv()

def read_csv():
    ejemplo = open('ejemplo.csv', 'r')
    for line in ejemplo:
        print(line)
    ejemplo.close()
read_csv()

