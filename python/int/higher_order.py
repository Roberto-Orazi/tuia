### Higher Order Functions ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(1, 2, sum_one))
print(sum_two_values_and_add_value(1, 2, sum_five))


### Closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(5)
print(add_closure(10))
print(sum_ten(3)(2))

### Built in higher order functions ###
numbers=[2,5,9,10,21]

# Map
def multiply_two(number):
    return number*2
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number*2, numbers)))

# Filter
def is_odd(number):
    if(number%2 == 0):
        return number

def is_even(number):
    if(number%3 ==0 and number%2 != 0):
        return number

def filter_greater_than_ten(number):
    if number > 10:
        return number

print(list(filter(is_odd, numbers)))
print(list(filter(is_even, numbers)))
print(list(filter(filter_greater_than_ten, numbers)))

# Reduce
from functools import reduce
def sum_two_values(first_value,second_value):
    return first_value+second_value

print(reduce(sum_two_values, numbers))