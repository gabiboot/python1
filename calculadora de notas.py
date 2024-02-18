
nombreAlumno = input("Introduzca nombre del alumno ")
nota1 = int(input("introducir nota  1 de alumno -> "))
nota2 = int(input("introducir nota  2 de alumno -> "))
nota3 = int(input("introducir nota  3 de alumno -> "))
sumaNota= nota1 + nota2 + nota3
promedio = sumaNota//3
print("alumno : ",nombreAlumno,"tiene promedio: ",promedio);

while sumaNota <= 30:

  if promedio > 7:
    print("Fleicidades, aprobaste el curso")
  elif promedio <= 7 & promedio > 4:
    print("pasaste pero puedes mejorar") 
  elif promedio <= 3:
    print("LO SIENTO, REPROBASTE, BURRO")
    break;

print("por favor ingresa NOTAS VALIDAS del 1 al 10")

