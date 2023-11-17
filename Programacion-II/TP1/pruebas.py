cadena='mati puto'
cadena_numerica=hash(cadena)
cadena_ascii=0
for caracter in cadena:
    valor_num=ord(caracter)
    cadena_ascii+=valor_num
cadena_ascii=sum(ord(caracter) for caracter in cadena)

print(cadena_ascii)
