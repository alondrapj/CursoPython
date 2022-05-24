#Declarar variables
calif1 = int(input("Ingresa la primer calificación: "))
calif2 = int(input("Ingresa la segunda calificación: "))
calif3 = int(input("Ingresa la tercer calificación: "))

#Proceso
sum_promedio = calif1 + calif2 + calif3
prom_final = sum_promedio / 3

if (prom_final >= 6 and prom_final <= 10):
    print("Aprobado")
elif (prom_final == 6):
    print("Ta bien pansaso")
elif (prom_final >=0 and prom_final <=6):
    print("Reprobado")
elif (prom_final <=0 or prom_final >10):
    print("ERROR EN PROMEDIO")

