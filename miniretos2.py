
print("Ejemplos rápidos:")
lst = [3,7,2,9]
print("max:", max(lst) if lst else None)

s = "Hola Mundo"
print("vocales:", sum(1 for ch in s.lower() if ch in "aeiou"))

n = 7
prime = True
if n < 2:
    prime = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1
print(f"{n} primo? {prime}")

lst2 = [1,2,2,3]
print("sin repetidos:", list(dict.fromkeys(lst2)))

while True:
    print("\n1:+ 2:- 3:* 4:/ 5:salir")
    o = input("> ").strip()
    if o == "5":
        break
    if o not in ("1","2","3","4"):
        print("opción inválida"); continue
    try:
        a = float(input("a: ")); b = float(input("b: "))
    except:
        print("entrada no válida"); continue
    if o == "1":
        print(a + b)
    elif o == "2":
        print(a - b)
    elif o == "3":
        print(a * b)
    else:
        print("err" if b == 0 else a / b)

print("Ejemplos rápidos:")
lst = [3,7,2,9]
print("max:", max(lst) if lst else None)

s = "Hola Mundo"
print("vocales:", sum(1 for ch in s.lower() if ch in "aeiou"))

n = 7
prime = True
if n < 2:
    prime = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime = False
            break
        i += 1
print(f"{n} primo? {prime}")

lst2 = [1,2,2,3]
print("sin repetidos:", list(dict.fromkeys(lst2)))

while True:
    print("\n1:+ 2:- 3:* 4:/ 5:salir")
    o = input("> ").strip()
    if o == "5":
        break
    if o not in ("1","2","3","4"):
        print("opción inválida"); continue
    try:
        a = float(input("a: ")); b = float(input("b: "))
    except:
        print("entrada no válida"); continue
    if o == "1":
        print(a + b)
    elif o == "2":
        print(a - b)
    elif o == "3":
        print(a * b)
    else:
        print("err" if b == 0 else a / b)