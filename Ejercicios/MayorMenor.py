print("=== PROGRAMA MAYOR Y MENOR ===")
print("Introduce una secuencia de numeros positivos")

N = int(input("¿Cuántos numeros vas a introducir? "))

while N <= 0:
    print("Error: Debes introducir al menos 1 numero")
    N = int(input("¿Cuántos numeros vas a introducir? "))

mayor = 0
menor = 0

for i in range(N):
    numero = float(input(f"Introduce el numero {i+1}: "))
    
    while numero <= 0:
        print("error, el numero debe ser positivo")
        numero = float(input(f"Introduce el numero {i+1}: "))
    
    if i == 0:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

print("=== RESULTADOS ===")
print(f"Numero mayor: {mayor}")
print(f"Numero menor: {menor}")