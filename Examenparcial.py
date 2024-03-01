# 1. Función para calcular la suma de todos los elementos de una lista
def suma_lista(lista):
    return sum(lista)

# 2. Función para invertir una cadena
def inverso_palabra(cadena):
    return cadena[::-1]

# 3. Programa para sumar los números pares de una lista ingresada por el usuario
def suma_pares():
    numeros = input("Ingrese una lista de números separados por espacios: ").split()
    numeros = [int(numero) for numero in numeros]
    suma = sum(numero for numero in numeros if numero % 2 == 0)
    print("La suma de los números pares en la lista es:", suma)

# 4. Creación de un diccionario representando un libro y adición de un nuevo campo
libro = {
    "título": "El nombre del viento",
    "autor": "Patrick Rothfuss",
    "año de publicación": 2007
}

# Agregar el campo "género"
libro["género"] = "Fantasía"

# Imprimir el diccionario actualizado
print("Diccionario del libro:", libro)
