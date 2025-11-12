nota= float(input("Dime tu nota:"))
if 0 <= nota <= 10:
    if 0<= nota <5:
        print("Tu nota es insuficiente")
    elif 5<= nota <6:
        print("Tu nota es suficiente")
    elif 6<= nota <7:
        print("Tu nota es un bien")
    elif 7<= nota <8:
        print("Tu nota es un notable")
    elif 9<= nota <10:
        print("Tu nota es un sobresaliente")
else:
    print("Nota no válida")
