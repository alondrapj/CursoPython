#FUNCIONES: Tareas o acciones a ejecutar

def Sumar(a, b):
    return a + b

def Restar(a,b):
    resta = a - b
    return resta

def Multiplicar(a, b):
    mult = a * b
    return mult

def Dividir(a, b):
    div = a / b
    return div


#MANDAR A LLAMAR O INVOCAR LAS FIONCONES

s = Sumar(10, 2)
#r = Restar(20, 4)
m = Multiplicar(12, 6)

#SALIDA DE DATOS
print("La suma =", s)
print("La resta =", Restar(20, 4))
print("La división =", Dividir(10, 2))
print("La multiplicación =", m)
