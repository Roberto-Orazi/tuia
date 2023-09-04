ingreso_mensual=100000
gasto_mensual=8000

if ingreso_mensual>10000:
    print('Estas bien economicamente en cualquier parte del mundo')
    if gasto_mensual < 7000:
        print('Ahora si estas bien')
    else:
        print('Estas Gastando mucho')

elif ingreso_mensual>5000: #esto seria un else if, en python se usa elif
    print('estas bien economicamente en Europa')
    if ingreso_mensual - gasto_mensual > 3000 :
        print('Ahora si estas bien en Europa')
    else:
        print('Estas Gastando mucho')

elif ingreso_mensual>1000:
    print('estas bien economicamente en Latinoamerica')
    if ingreso_mensual - gasto_mensual < 0 :
        print('Estas en deficit')

elif ingreso_mensual>500:
    print('estas bien economicamente en Argentina')

elif ingreso_mensual>200:
    print('estas bien economicamente en Venezuela')

else:
    print('Sos pobre')

