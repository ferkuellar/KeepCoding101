# Explicar el funcionamiento de if-else en Python

# en este capitulo se hablara sobre el if-else en python, el if-else es una estructura de control que nos permite tomar decisiones en nuestro codigo, si la condicion no se cumple se ejecutara otro bloque de codigo.

# if-else

# if-else es una estructura de control que nos permite ejecutar un bloque de codigo si se cumple una condicion, si la condicion no se cumple se ejecutara otro bloque de codigo.


number =  int(input("Ingresa un numero: "))
if number > 5:
    print("El numero es es mayor a 5")
else:
    print("El numero es menor a 5")


#eplicar el funcionamiento de if-elif-else en Python

# en la practica anterior el numero revisa IF se cumple la condicion, si no se cumple la condicion revisa ELSE, pero que pasa si queremos revisar mas de una condicion, para eso existe ELIF, ELIF es una estructura de control que nos permite revisar mas de una.

# nota importante cuando se usa if-else.

# else siempre se escribe despues de un if.
# solo se puede escribir un bloque de if.
# solo se puede escribir un bloque de else.
# se puede escribir varios bloques de if usando bloques usando operadores logicos.

# solo el bloque if

num = int(input("Ingresa un numero: "))
if num > 0:
    print("El numero es positivo")

# si la c ondicion if no es veradera no se ejecutara nada.

# solo el bloque else

# num = int(input("Ingresa un numero: "))
# else:
#    print("El numero es negativo")

# el bloque else siempre debe de ir escirto dentro de un if si no se ejecutara un error.


