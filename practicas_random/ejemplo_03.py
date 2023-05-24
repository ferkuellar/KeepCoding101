# Explica los operadores con ejemplos, en este archiv se aprenderan sobre los opreadores a detalle.

# Operadores aritmeticos
# operaderes relacionales
# operadores de asignacion
# operadores logicos
# operadores bit a bit
# operadores de membresia
# operadores de identidad

# Operadores aritmeticos

# todos los operadores matematicos basicos como suma, resta, multiplicacion, division, modulo, exponente, division entera.

# suma y resta

a = 2
b = 7
print(a + b)
print(a - b)

c = 2.5
d = 3

print(c + d)
print(c - d)

# toma nota si la suma es un numero entero con un numero flotante el resultado sera un numero flotante.

# esto es por que python convierte el numero entero a un numero flotante para poder realizar la operacion, python siempre va a convertir el numero entero a un numero flotante para poder realizar la operacion.

# multiplicacion y exponente

a = 5 
b = 7

print(a * b)
print(3.5 * 2)

# exponente nos da m ^ n (m elevado a la n)

print(2 ** 3)
print(2 ** 3.5)

# division ( / ) y division entera ( // )

# division ( / ) nos da un numero flotante como resultado

a = 5
b = 2

print(a / b) # da la rspuesta correcta (recomedado)

# division entera ( // ) nos da un numero entero como resultado

print(a // b) # quita el numero despues del punto da la respuesta incorrecta

# la division flotante es la division normal que conocemos, la division entera es la division que nos da un numero entero como resultado.

# la division entera es util cuando queremos saber cuantas veces un numero cabe en otro numero.

# modulo ( % )

# el modulo nos da el residuo de una division

# el modulo es util cuando queremos saber si un numero es par o impar.

# si el residuo es 0 el numero es par, si el residuo es 1 el numero es impar.

# si el residuo es 0 el numero es multiplo del numero que estamos dividiendo, si el residuo es 1 el numero no es multiplo del numero que estamos dividiendo.

a = 5
b = 2

print(a % b)
print(10 % 2)

# Operadores relacionales

# los operadores relacionales nos sirven para comparar dos valores.
# los operadores relacionales nos dan como resultado un valor booleano (True o False)
# los operadores relacionales son: >, <, >=, <=, ==, !=
# los operadores relacionales son: mayor que, menor que, mayor o igual que, menor o igual que, igual que, diferente que.

# menor y menor o igual que

print(5 < 10) # si es corecto regresa True si no es correcto regresa False

print (13 <= 15) # si es corecto regresa True si no es correcto regresa False

print (9 < 7 ) # si es corecto regresa True si no es correcto regresa False

# mayor que y mayor o igual que

print(5 > 10) # si es corecto regresa True si no es correcto regresa False

print (13 >= 15) # si es corecto regresa True si no es correcto regresa False

print (9 > 7 ) # si es corecto regresa True si no es correcto regresa False

# igual que y diferente que

print(5 == 10) # si es corecto regresa True si no es correcto regresa False

print (13 != 15) # si es corecto regresa True si no es correcto regresa False

print (9 == 7 ) # si es corecto regresa True si no es correcto regresa False

# Operadores de asignacion

# los operadores de asignacion nos sirven para asignar un valor a una variable.
# los operadores de asignacion son: =, +=, -=, *=, /=, %=, //=, **=.
# los operadores de asignacion son: asignacion, suma y asignacion, resta y asignacion, multiplicacion y asignacion, division y asignacion, modulo y asignacion, division entera y asignacion, exponente y asignacion.


# asignacion ( = )

num = 5
print(num)

# suma y asignacion ( += )

num += 10 # es lo mismo que num = num + 10
print(num)  # el resultado es 15

# resta y asignacion ( -= )

num -= 10 # es lo mismo que num = num - 10
print(num)  # el resultado es 5

# multiplicacion y asignacion ( *= )

num *= 5 # es lo mismo que num = num * 5
print(num)  # el resultado es 50

# division entera y asignacion ( //= )

num //= 2 # es lo mismo que num = num // 2
print(num)  # el resultado es 5

# division y asignacion ( /= )

num /= 3 # es lo mismo que num = num / 3
print(num)  # el resultado es 5.0

# modulo y asignacion ( %= )

num %= 2 # es lo mismo que num = num % 2
print(num)  # el resultado es 5.0

# operadores logicos
# los operadores logicos nos sirven para comparar dos valores booleanos.
# los operadores logicos nos dan como resultado un valor booleano (True o False)
# los operadores logicos son: and, or, not.

# and

print( 5 > 3 and 4 < 1 ) # si es corecto regresa True si no es correcto regresa False

print( 5 > 3 and 4 > 1 ) # si es corecto regresa True si no es correcto regresa False

# or
# si uno de los valores es True el resultado es True, si los dos valores son False el resultado es False.

print( 5 > 3 or 4 < 1 ) # si es corecto regresa True si no es correcto regresa False

print( 5 < 3 or 4 < 1 ) # si es corecto regresa True si no es correcto regresa False

# not
# si el valor es True el resultado es False, si el valor es False el resultado es True.

print(not 5 > 3) # si es corecto regresa True si no es correcto regresa False