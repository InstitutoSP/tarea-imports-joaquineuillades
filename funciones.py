#Funciones calculadora

def suma(a,b):
    resultado = a+b
    return resultado

def resta(a,b):
    resultado = a-b
    return resultado

def multi(a,b):
    resultado = a*b
    return resultado

def dividido(a,b):
    resultado = a/b
    return resultado


def ord_mayor(arreglo):
    n = len(arreglo)

    for i in range(n-1):
        for j in range(n-1-i):
            if arreglo[j] < arreglo[j+1]:
                temp=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=temp


def ord_menos(arreglo):
    n = len(arreglo)

    for i in range(n-1):
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1]:
                temp=arreglo[j]
                arreglo[j]=arreglo[j+1]
                arreglo[j+1]=temp                

def ord_nombre(nombre):

    nombre.sort()