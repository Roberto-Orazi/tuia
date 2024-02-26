def recursiva(numero:int) -> str:
    if (numero==0):
        return "0"
    digito=numero%10
    print('digito',digito)
    resto = recursiva(numero//10)
    print('resto',resto)
    final=str(resto)+str(digito)
    print('final', final)
    return final

prueba=recursiva(2122)

print(prueba)