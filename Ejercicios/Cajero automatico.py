saldo = 1000  

print(f"Saldo disponible:{saldo}")

while True:
    print("¿Qué operación desea realizar?")
    print("1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        
        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor a 0")
        elif cantidad > saldo:
            print("Error: Fondos insuficientes")
        else:
            saldo -= cantidad
            print(f"Retiro exitoso. Ha retirado ${cantidad}")      
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a depositar: $"))
        
        if cantidad <= 0:
            print("Error: La cantidad debe ser mayor a 0")
        else:
            saldo += cantidad
            print(f"Depósito exitoso. Ha depositado ${cantidad}")
            print(f"Su nuevo saldo es: ${saldo}")
            
    elif opcion == "3":
        # Salir
        print("Gracias por usar nuestro cajero automático")
        break
        
    else:
        print("Opción inválida. Por favor seleccione 1, 2 o 3")

print("¡Hasta luego!")