"""Escribe un programa en Python que realice operaciones matemáticas simples (suma, resta, multiplicación y división) utilizando una función. El programa debe permitir al usuario ingresar dos números y seleccionar una operación para realizar."""

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero."


print("Por favor ingrese el primer numero")
num1 = int(input("-> "))
print(f"que hara con {num1} sumar(1), restar(2), multiplicar(3), dividir(4)")
operacion = int(input("-> "))
print("ingrese segundo numero para la operacion")
num2=int(input("-> "))


rSuma = sumar(num1,num2)
rResta = restar(num1,num2)
rDividir = dividir(num1,num2)
rMultiplicar = multiplicar(num1,num2)

if operacion == 1:
    print(f"el resultado es: {rSuma}")
elif operacion == 2:
    print(f"El Resultado es: {rResta}")
elif operacion == 3:
    print(f"El Resultado es: {rMultiplicar}")
elif operacion == 4:
    print(f"El Resultado es: {rDividir}")
else :
    print("Error")                
     