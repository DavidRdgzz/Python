nums = [3, 7, 2, 9]
#Suma de todos
suma = sum(nums)
print(f"suma de todos: {suma}")

#Cual es el maximo
maximo = max(nums)
print(f"Este es el numero maximo: {maximo}")

#contar ocurrencias
numero= 9
ocurr= 0
for n in nums:
    if n == numero:
       ocurr += 1
print(f"{numero} en la lista, aparece {ocurr} veces")

#Calcular la media de una lista de enteros
contador = 0
total = 0
for n in nums:
    total += n
    contador += 1
media= total / contador
print (f"La media es {media}")

#Crea una lista solo con los pares
pares = 0
for x in nums:
    if x %2 == 0:
        pares += 1
        print(f"Esta es la lista de pares: {pares}")

#Dado nums halla max(nums) - min(nums) usando for
for x in nums:
    ola= max(nums) - min(nums)
print (f"Este es el max - min {ola}")

#Pide un numero
typeshi= int(input("Introduce un numero: "))
for x in range(len(nums)):
    if nums [x] == typeshi:
        indice = x
        indice += 1
        break
print(f"El numero {typeshi} aparece en el indice {indice}")