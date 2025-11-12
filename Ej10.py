

print("=== CALCULADORA DE FACTURA ===")
print("Introduce los precios de los productos.")
print("Escribe 0 para terminar y ver el total.")
print()

total = 0

while True:
    precio = float(input("Introduce un precio (0 para terminar): "))
    
    if precio == 0:
        break
    
    total += precio


print()
print(f"El total de la factura es: {total:.2f} €")
