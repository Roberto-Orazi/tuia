'''
5! = 5*(4*3*2*1)
4! = 4*3*2*1
5! = 5 * 4!
Factorial(n) = n * factorial(n-1)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))

func = factorial(5)
print(func)

'''
fibonacci(n)= fibonacci(n-1) + fibonacci(n-2)
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
fibo=fibonacci(2)
print(fibo)

def cuenta_atras(num):
    num -=1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print('hola')

cuenta_atras(4)
