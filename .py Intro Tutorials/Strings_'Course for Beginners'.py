course = 'Python for Beginners'
# "Python's Course for Beginners" = return value w/n ' '
# "" can be used w/n ' '; 'Python for "Beginners"'
print(course)
print('Python for "Beginners"')

# '''' allows for long script to be returned from print()
course1 = '''
Hi Robert

Here is our first email to you.

Thank you,
The Support Team

'''
print(course1)
# [] = given character index w/n a string
# Hello There!
# 01234 = character index ; do not count space between words
course2 = 'Python for Beginners'
print(course2[0])
print(course2[2])
# index can be negative value
# negative index is the last character in the word
print(course2[-1])
print(course2[-19])
# [:] can be used to copy string
# length of string depends on index value used w/n [:]
another = course2[:]
print(another)
another1 = course2[0:]
print(another1)
another2 = course2[1:19]
print(another2)

name = "Jennifer"
print(name[1:-1])
