agua = int(input("Ingresa el nivel del agua en metros: "))

if (agua > 6):
    print("Desbordamiento de agua en cisterna")
elif (agua == 6):
    print("Apagar Bomba")
elif(agua >=4  and agua <= 6):
    print("Desacelerar Bomba")
elif(agua >=2 and agua <= 4):
    print("Bomba Trabajando!")
elif(agua >0 and agua <=2):
    print("Acelerar Bomba de Agua")
elif(agua ==0):
    print("Enceder Bomba de Agua")
elif(agua <0):
    print("Fuga en Cisterna")
