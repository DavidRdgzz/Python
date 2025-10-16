n_chicos = int(input("Introduce un numero de chicos: "))
n_chicas = int(input("Introduce un numero de chicas: "))
total_p = n_chicas + n_chicos
p_chicas = n_chicas / total_p * 100
p_chicos = n_chicos / total_p * 100
print(f'El porcentaje de chicos es: {p_chicos:.2f}%')
print(f'El porcentaje de chicas es: {p_chicas:.2f}%')
print("El porcentaje de las chicas es de %.2f %%"%(p_chicas))