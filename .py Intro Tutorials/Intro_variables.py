# price = 10 variables temp store data in CPU memory Price = var 10 = value
price = 20  # integer = number w/out decimal point, whole number
# floats = numbers w/ decimal point
# simple values numbers, integers, floats, strings, or booleans
print(price)  # function prints value of variable 'price'

# receiving input from user using input() function.
# print()
# input() asks for data from user
name = input('What is you name? ')  # prints string w/n ' ' allows for user input
print('Hi ' + name)

favorite_color = input('What is your favorite Color? ')
print(name + ' likes ' + favorite_color)

birth_year = input('Birth year: ')  # birth_year variable set to string not integer causing Type Error:
# '1993' (string) vs 1993 (integer)
print(type(birth_year))
# type(function)
# prints variable type; string, integer, boolean
age = 2022 - int(birth_year)  # variable must have input value converted to integer to show print as number
print(type(age))
# int() = integer, whole numbers
# float() = number w/ decimal point
# bool() = True/False
print('Robert is')
print(age)
# using input function always results w/ string, numerical values must be converted to integers or floats

weight_lbs = input('Weight (lbs): ')  # returns a string
weight_kg = int(weight_lbs) * 0.45  # adding int() converts string value for weight_lbs to integer
print("Robert's weight in kiloGrams:")
print(weight_kg)  # program will return value as a number
# https://www.youtube.com/watch?v=_uQrJ0TkZlc .py tutorial 29:30
