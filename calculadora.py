import time

n1= int(input("Introduce un numero:  ")) 
op= input("Introduce la operacion (+, -, *, /): ") 
n2= int(input("Introduce otro numero: "))
print("Calculando resultado...")
time.sleep(2)
print("Ya casi esta...")
time.sleep(2)
if op == "+":
    print("El resultado es: ", n1+n2)
elif op == "-":
    print("El resultado es: ", n1-n2)
elif op == "*":
    print("El resultado es: ", n1*n2)
elif op == "/":
    if n2 != 0:
        print("El resultado es: ", n1/n2)
    else:
        print("Error: Division por cero no permitida.")
else:
    print("Pon un simbolo permitido")