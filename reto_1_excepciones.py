from abc import ABC, abstractmethod
import math

class InvalidPointError(Exception):
    def __init__(self, message="Points must be valid instances of the Point class."):
        super().__init__(message)

class InvalidDimensionError(Exception):
    def __init__(self, message="Width and height must be greater than zero."):
        super().__init__(message)

class NotASquareError(Exception):
    def __init__(self, message="The given points do not form a valid square."):
        super().__init__(message)

def operar(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            raise ZeroDivisionError("No puedes dividir por cero") #Valida que el denominador no sea 0.
    else:
        raise ValueError("Operador no válido: " + operador) #Valida que se haya ingresado un operador valido.

def es_palindromo(palabra):
    palabra = palabra.lower()
    izquierda = 0
    derecha = len(palabra) - 1

    while izquierda < derecha:
        if palabra[izquierda] != palabra[derecha]:
            return False
        izquierda += 1
        derecha -= 1

    return True
print(es_palindromo("reconocer"))
print(es_palindromo("python")) 

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtrar_primos(lista):
    # Valida que todos los elementos sean enteros
    if not all(isinstance(n, int) for n in lista):
        raise TypeError("La lista debe contener solo números enteros")

    primos = []
    for n in lista:
        if es_primo(n):
            primos.append(n)
    return primos

print(filtrar_primos([1, 2, 3, 4, 5, 6, 7]))

    
def mayor_suma_consecutiva(lista):
    if len(lista) < 2:
        return None
    mayor = lista[0] + lista[1]
    for i in range(1, len(lista) - 1):
        suma = lista[i] + lista[i + 1]
        if suma > mayor:
            mayor = suma
    return mayor
print(mayor_suma_consecutiva([1, 3, 2, 5, 4]))

def palabras_con_mismos_caracteres(lista):
    resultado = []
    if not lista: #Valida que la lista no esté vacía.
        raise ValueError("La lista no puede estar vacía")
    for palabra in lista:
        for otra in lista:
            if palabra != otra and sorted(palabra) == sorted(otra):
                if palabra not in resultado:
                    resultado.append(palabra)
    return resultado
print(palabras_con_mismos_caracteres(["amor", "roma", "perro"]))

try:
    print(operar(10, 3, '/'))
    
except ZeroDivisionError as e:
    print("Error capturado:", e)
    
except ValueError as i:
    print("Error capturado ", i)
    
except TypeError as o:
    print("Error capturado: ", o)
    
finally:
    print("Yay")


