#Bibliotecas
import math

#Declara variables
radio = float(input("Ingresa su radio :"))

#Proceso
area = math.pi * pow(radio, 2)
perimetro = 2 * math.pi * radio

#Salida de datos
print("El área del ciculo es: ", round(area, 2))
print("El perímetro del ciculo es: ", round(perimetro, 2))