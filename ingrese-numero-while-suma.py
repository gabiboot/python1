n = False
respuesta = True
lista = []

while respuesta :
 print("ingresa numero que quieres sumar")
 numero = int(input("->"))
 lista.append(numero)
 suma = sum(lista)


 salir = input("¿Quieres sumar otro numero? (s/n): ")
 if salir == "n":
  respuesta = False


print(f"la suma de tus numeros es {suma}") 

