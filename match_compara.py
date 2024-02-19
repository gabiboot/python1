numero = int(input("Por favor ingrese un numero entero"))

match numero:
    case numero if  numero < 0 :
        print("es un numero negativo")
    case numero if  0 <= numero <=9 : 
        print("El numero esta en el rango de 0 a 9")
    case numero if numero >= 10 :
        print("El numero es superior o igual a 10")
    case _:
        print("numero no reconocido")            
