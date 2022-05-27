from re import S
from tkinter import N


def Imprimir():
    num = [5, 4, 8, 9, 13, 24, 56, 8, 26, 76]
    num.sort()
    return num

n = Imprimir()

print("Elementos numericos", n)