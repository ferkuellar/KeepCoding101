# se pueden hacer operaciones con los numeros o artmeticas
# suma, multiplicacion, division, resta, potencia, modulo

print(2 + 2)
print(2 * 2)
print(2 / 2)
print(2 - 2)
print(2 + 2 + 5 + 6 + 7 + 8 + 9 + 10)
print(2 * 2 * 5 * 6 * 7 * 8 * 9 * 10)

# tambien se pueden concatenar dos cadenas de texto dentro de # print()

first_name = "Juan"
last_name = "Perez"
print(first_name + " " + last_name)

# caracteres de espaciado y salto de linea \n \t \b \r \f \v
# \n salto de linea
# \t tabulacion
# \b retroceso
# \r retorno de carro
# \f salto de pagina
# \v tabulacion vertical
# \\ barra invertida \
# \' comilla simple '
# \" comilla doble "
# \a alerta

print("Hola\nMundo")
print("Hola\tMundo")
print("Hola\bMundo")
print("Hola\rMundo")
print("Hola\fMundo")
print("Hola\vMundo")
print("Hola\\Mundo")
print("Hola\'Mundo'")
print("Hola\"Mundo")
print("Hola\aMundo")

# funcion sin nueva linea al final 
# print("Hola", end=" ")
# funcion con nueva linea al final

print("this is frist line", end="-->")
print("this is second line")

# el atributo end es para que no se haga un salto de linea al final del print esta funcion evita el salto de linea.
# en lugar de hacer un salto de linea al final del print se puede poner cualquier caracter o cadena de texto.
# sin embargo, si se quiere hacer un salto de linea al final del print se puede hacer de la siguiente manera:

print("this is frist line", end="\n")
print("this is second line")
