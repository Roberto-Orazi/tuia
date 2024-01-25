#num1 = int(input("Ingrese un numero ")) 

#num2 = int(input("Ingrese un numero ")) 

#num3 = int(input("Ingrese un numero "))
num1 = 1; num2=2;num3=3
if(num1>num2 and num1>num3): #(num2 < num1 > num3)
    print("Num1 es el mayor")
elif(num2 > num3): #(num1 < num2 > num3)
    print("num2 es el mayor")
else:
    print("num3 es el mayor")
    
if(num1>num2):
    if(num2>num3):
        print("Num1 es el mayor")
else:
    if num2>num3:
        print("num2 es el mayor")
    else:print("num3 es el mayor")
    
print(f"El mayor numero es, {max(num1,num2,num3)}")

mayor = 15
print("hola", mayor) # CON EL + NO SE PUEDE CONCATENAR

