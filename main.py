import funciones as fn

while (True):
  print("Estas son tus opciones: Suma, Resta, Division, Multiplicacion o salir")
  texto = input("Seleccione una opcion: ")
  if texto == "salir":
     print("Nos Vemos")
     break
  num = int(input("Seleccione un numero: "))
  num2 = int(input("Seleccione otro numero: "))

  if texto == "Suma":
    print(fn.suma(num,num2))
  elif texto == "Resta":
     print(fn.resta(num,num2))
  elif texto == "Division":
     print(fn.dividido(num,num2))
  elif texto == "Multiplicacion":
     print(fn.multi(num,num2))