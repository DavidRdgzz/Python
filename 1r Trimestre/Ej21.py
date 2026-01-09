import random
import time

t = random.randint(1, 100)
s = time.time()

while True:
    try:
        g = int(input("Introduce un número (1-100): "))
    except ValueError:
        print("Entrada no válida")
        continue
    if g < 1 or g > 100:
        print("Fuera de rango (1-100)")
        continue
    if g < t:
        print("Más alto")
        time.sleep(0.15)
    elif g > t:
        print("Más bajo")
        time.sleep(0.15)
    else:
        d = time.time() - s
        print(f"Muy bien, has adivinado el número {t} y {d} segundos.")
        break
