### List comprehension ###

my_original_list=[0,1,2,3,4,5,6,7]
print(my_original_list)

my_list=[i for i in my_original_list]
print(my_list)

my_list_plus_one=[i+1 for i in range(8)] # Aca sumamos uno al valor de la lista
print(my_list_plus_one)

my_list_square=[i*i for i in range(8)] # Aca hacemos el cuadrado
print(my_list_square)

my_list_doble=[i*2 for i in range(8)] # Aca duplicamos el valor
print(my_list_doble)

my_range=range(8)
print(list(my_range))

def sum_five(num):
    return num + 5

my_list_sum_five=[sum_five(i) for i in range(8)]
print(my_list_sum_five)

