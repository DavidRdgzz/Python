# FacturaSimple.py — Plantilla (rellena los TODO)
print("=== FACTURA SIMPLE (sin listas) ===")

# 1) Pide N en 1..50 (usa while para validar)
N = int(input("cuantas lineas tendrá la factura (1-50)? "))
while N < 1 or N > 50:
    print("error, debe estar entre 1 y 50")
    N = int(input("cuantas lineas tendra la factura (1-50)? "))

total_bruto = 0.0
baratas = 0
medias = 0
caras = 0
precio_min = 0
precio_max = 0

# 2) Recorre 1..N con for
for i in range(1, N + 1,):
    print(f"linea {i}")
    
    # 2.a) Precio >= 0 (validar con while)
    precio = float(input("precio: "))
    while precio < 0:
        print("error, el precio debe ser >= 0")
        precio = float(input("precio: "))
    
    # 2.b) Cantidad >= 1 (validar con while)
    cantidad = int(input("cantidad: "))
    while cantidad < 1:
        print("error, la cantidad debe ser >= 1")
        cantidad = int(input("cantidad: "))
    
    # 2.c) Clasifica el precio con if/elif/else y lleva contadores
    if precio < 5:
        baratas += 1
    elif precio <= 20:
        medias += 1
    else:
        caras += 1
    
    # 2.d) Actualiza min/max
    if precio_min == 0 or precio < precio_min:
        precio_min = precio
    if precio_max == 0 or precio > precio_max:
        precio_max = precio
    
    # 2.e) Acumula subtotal en total_bruto
    subtotal = precio * cantidad
    total_bruto += subtotal

# 3) Tramos de descuento con if/elif/else
if total_bruto >= 100:
    p_desc = 15
elif total_bruto >= 50:
    p_desc = 10
elif total_bruto >= 20:
    p_desc = 5
elif total_bruto <20:
    p_desc = 0
else:
    print("error en el descuento")

# 4) Calcula descuento, base, iva y total
descuento = total_bruto * p_desc / 100
base = total_bruto - descuento
iva = base * 0.10
total_final = base + iva 

# 5) Muestra resumen con 2 decimales
print("======================================")
print("RESUMEN DE FACTURA")
print("======================================")
print(f"total bruto:{total_bruto:.2f}$")
print(f"descuento ({p_desc}%):-{descuento:.2f}$")
print(f"base:{base:.2f} $")
print(f"IVA (10%):{iva:.2f} $")
print(f"TOTAL:{total_final:.2f} $")
print("======================================")
print("ESTADISTICAS")
print("======================================")
print(f"lineas baratas (<5€):{baratas}$")
print(f"lineas medias (5-20€):{medias}$")
print(f"lineas caras (>20€):{caras}$")
print(f"precio minimo:{precio_min:.2f}$ ")
print(f"precio maximo:{precio_max:.2f}$ ")