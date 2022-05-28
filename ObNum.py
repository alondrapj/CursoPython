num = int(input("Ingresa un número, puede ser positivo o negativo: "))

if (num < 0 and num > -100):
    for i in range(-1, -100, -2):
        print(f'{i}')
elif(num > 0 and num < 100):
    for i in range(2, 101, 2):
        print(f'{i}')
else:
    print("ERROR")