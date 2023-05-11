# strings en Python estan rodeadas de comillas simples o dobles. veamos algunos ejemplos:

name = 'John'
age = 37

# Concatenacion

print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

print('My name is {name} and I am {age}'.format(name=name, age=age))

# Arguments by position

print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)

print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'helloworld'

# Capitalize string

print(s.capitalize())

# Make all uppercase

print(s.upper())

# Make all lower

print(s.lower())

# Swap case

print(s.swapcase())

# Get length

print(len(s))

# Replace

print(s.replace('world', 'everyone'))

# Count

sub = 'h'
print(s.count(sub))

#starts with

print(s.startswith('hello'))

# ends with

print(s.endswith('d'))

# Split into a list

print(s.split())

# Find position

print(s.find('r'))

# Is all alphanumeric

print(s.isalnum())

# Is all alphabetic

print(s.isalpha())

# Is all numeric

print(s.isnumeric())
