import random

numero = random.randint(1, 10)
prg = int(input("Adivina el número (del 1 al 10): "))

while prg != numero:
    if prg < numero:
        print("Te has quedado corto")
    else:
        print("Te has pasado")
    prg = int(input("Intenta de nuevo: "))

print("¡Muy bien! Has adivinado el número")
