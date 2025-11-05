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
    diff = abs(g - t)
    if diff == 0:
        d = time.time() - s
        print(f"Muy bien, has adivinado el número {t} en {d:.2f} segundos.")
        break
    elif diff <= 3:
        print("Caliente 🔥")
    elif diff > 7:
        print("Frío ❄️")
    else:
        print("Templado")