is_hot = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")

is_hot = False  # boolean value is false
if is_hot:
    print("It's a hot day")
print("Enjoy your day")
# line 7 will cause line 9 print() to not return string value in run program

is_hot2 = True  # will not return string value from else: statement
if is_hot2:
    print("It's a hot day")
    print("Drink plenty of water")
else:  # executes code if above statement is not true
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

is_hot2 = False  # will return string value from else: statement
if is_hot2:
    print("It's a hot day")
    print("Drink plenty of water")
else:  # executes code if above statement is not true
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

# using else: & elif: statements

is_hot3 = False  # will not return string value from if: statement
is_cold = True   # will return string value from elif: statement
if is_hot3:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

is_hot3 = False  # will not return string value from if: statement
is_cold = False  # will return string value from else: statement
if is_hot3:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:  # boolean value in line 46 results in return of else: statement in run program
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

# Exercise
# price of a house is $1M.
# If buyer has good credit, they need to put down 10%,
# otherwise they need to put down 20%. Print the down payment.

price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: {down_payment}")  # to return '$' in return output add '$" before {} in line 68
print(f"Down payment: ${down_payment}")

# LOGICAL OPERATORS
# 'AND' : both
# 'OR' : at least one
# 'NOT' : inverses boolean value
# conditions: If applicant has high income AND good credit
#       print(Eligible for loan) in run program
# 'and' operator must fulfill both conditions to print if: msg in run program
has_high_income = True
has_good_credit = True  # if either value were false no if: statement will print in output
if has_high_income and has_good_credit:  # both values must be true for if: statement to print output
    print("Eligible for loan")
# 'or' operator must only fulfill at least one of above conditions
has_high_income = False
has_good_credit = True  # if both conditions are false no msg will appear in run program
if has_high_income or has_good_credit:  # at least one value must be true to print output msg
    print("Eligible for loan")
# 'not' operator inverses boolean value
has_good_credit = True
has_criminal_record = True  # 'not' operator will be false and result in no msg in output screen
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
