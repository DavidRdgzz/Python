n1= int(input("Dime la primera nota: "))
n2= int(input("Dime la segunda nota: "))
n3= int(input("Dime la tercera nota: "))
nfinal= n1*0.3 + n2*0.2 + n3*0.5 

if n1 < 4 and n2 < 4 and n3 < 4:
    print("Tu nota final es un 0")
elif n1 < 4 or n2 < 4 or n3 < 4:
    print("Tu nota es un 2")
elif n1 > 4 and n2 > 4 and n3 > 4:
    print(f"Tu nota es {nfinal}")
else:
    print("Vuelve a introducir las notas bien")