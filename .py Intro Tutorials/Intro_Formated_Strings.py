first = 'Robert'
last = 'Anderson'
message = first + ' [' + last + '] is a coder.'
# Robert [Anderson] is a coder
print(message)
# formatted strings make it easier to visualize the output.
# prefix = f'{variable name}'
msg = f'{first} [{last}] is a coder.'
print(msg)

course3 = 'Python for Beginners'
print(len(course3))
# len(function) enforce limit of characters on input fill
# general purpose functions are preset programs on python
print(course3.upper())
print(course3)
print(course3.lower())
# prints return characters in all UPPERCASE characters.
print(course3.find('P'))
# find(meth/fun) returns index value of a character w/n string
# case-sensitive
print(course3.find('B'))
print(course3.find('p'))
# replace(meth/fun)
print(course3.replace('Beginners', 'Absolute Beginners'))
print(course3.replace('th', 'g'))
print('Python' in course3)  # in operator produces a boolean expression
print('python' in course3)
