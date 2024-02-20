"""Escribe un programa en Python que permita al usuario ingresar su nombre, edad, dirección y número de teléfono, y luego muestre estos datos en pantalla."""


usuarios = {}

print("Bienvenido, por favor ingrese sus datos a continuacion")
nombre = input("Nombre -> ")
edad = int(input("Por favor ingrese su edad (solo numeros)-> "))
direccion = input("Por favor ingrese su direccion -> ")
telefono = int(input("Por favor ingrese su numero de telefono -> "))

usuarios.update({nombre:{edad, direccion, telefono }})
exito= usuarios.items()
print(f"Los datos del usuario han sido guardados con exito {exito}")