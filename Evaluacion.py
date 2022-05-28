aciertos = 0 #Variable como contador
print("-----------BIENVENIDO AL EXAMEN-----------")
print("1. Herramienta de programación, parecido al lenguaje español utilizado para crear código:")
print("a) IDE")
print("b) Pseudocódigo")
print("c) Copilador")
print("d) ANSI/ISO")

resp1 = (input("Ingresa tu respuesta: "))
if (resp1 == "b"):
    aciertos = aciertos + 1
else:
    print("Respuesta incorrecta")

print("2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados:")
print("a) Información")
print("b) Datos")
print("c) Programa")
print("d) Código")

resp2 = (input("Ingresa tu respuesta: "))
if (resp2 == "a"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

print("3. Insitituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo :")
print("a) IEEE")
print("b) IDE")
print("c) ANSI/ISO") #Esta es
print("d) VSCode")

resp3 = (input("Ingresa tu respuesta :"))
if (resp3 == "c"):
    aciertos = aciertos + 1
else:
    print("Respues Incorrecta")

print("4. Serie de pasos consecutivos, ordenados y finitos que siguen para resolver un problema :")
print("a) Proceso")
print("b) Solución")
print("c) Función")
print("d) Algoritmo") #esta es

resp4 = (input("Ingresa tu respuesta :"))
if (resp4 == "d"):
    aciertos = aciertos + 1
else:
    print("Respuesta incorrecta")

print("5. Conjunto de elementos que se relacionan para cumplir una función determinada :")
print("a) Estructura")
print("b) Datos")
print("c) Operación")
print("d) Sistema") #esta era

resp5 = (input("Ingresa tu respuesta :"))
if (resp5 == "d"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

print("6. Componente de una IDE que se encarga de trducir el código fuente a código máquina :")
print("a) Depurador")
print("b) Editor de Texto")
print("c) Terminal de Salida")
print("d) Copilador/Intérprete") # Ta bien

resp6 = (input("Ingresa tu respuesta :"))
if(resp6 == "a"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

print("7. Elemento que se usa para almacenar una cantidad donde cambia su valor :")
print("a) Constante")
print("b) Variable") # tas bien
print("c) Libreria")
print("d) Tipo de dato")

resp7 = (input("Ingresa tu respuesta :"))
if(resp7 == "b"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

print("8. Conjutno de símbolos, letras, números que no tiene un significado :")
print("a) Datos") #esta
print("b) Estructura")
print("c) Información")
print("d) Sistema")

resp8 = (input("Ingresa tu respuesta :"))
if(resp8 == "a"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

print("9. Disciplina qu argumenta conclusiones a aprtir de premisas mediante un razonamiento :")
print("a) Filosofía")
print("b) Socilogía")
print("c) Lógica") #es esta
print("d) Argumentación")

resp9 = (input("Ingresa tu respuesta :"))
if(resp9 == "c"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

print("10. Medida, patrón, modelo o norma universal apra realizar una actividad oprducir un objeto :")
print("a) Evento")
print("b) Estándar") #no c
print("c) Calidad")
print("d) Productividad")

resp10 = (input("Ingresa tu respuesta :"))
if(resp10 == "b"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

print("11. Conjunto de elementos ordenado que componen y son la base de algo físico o no físico :")
print("a) Estructura") # esta
print("b) Sistema")
print("c) Objeto")
print("d) Virtual")

resp11 = (input("Ingresa tu respuesta :"))
if(resp11 == "a"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

print("12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar :")
print("a) Operaciones/Cálculos")
print("b) Sintaxis")
print("c) Programas de Computadora") #sospecho
print("d) Comando")

resp12 = (input("Ingresa tu respuesta :"))
if(resp12 == "c"):
    aciertos = aciertos + 1
else:
    print("Respuesta Incorrecta")

resultados = (aciertos/12)*10

print("Tu calificación final es de :", resultados)







