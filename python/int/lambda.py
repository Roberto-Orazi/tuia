### Lambdas ###
from typing import Callable

sum_two_values: Callable[[int,int],int] = lambda first_value, second_value: first_value + second_value
print(sum_two_values(1,2))

multiply_values = lambda first_value, second_value: first_value*second_value
print(multiply_values(2,3))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2,4))
