'''
Si condicion cumple: si es true entra si es false no
    se ejecuta un codigo
si no se cumple la condicion anterior(si la condicion anterior es falsa)
    se ejecuta otro codigo
if condicion:
    accion
else:
    otra accion
if true:
    se ejecuta
if false:
    no se ejecuta
'''

edad_menor=17
edad_mayor=18

if edad_mayor>=18:
    print('Podes pasar')
else:
    print('No podes pasar')

if edad_menor>=18:
    print('Podes pasar')
else:
    print('No podes pasar')

contraseña='Prueba123'

if contraseña=='Prueba123':
    print('Iniciando sesion')
else:
    print('Contraseña equivocada')