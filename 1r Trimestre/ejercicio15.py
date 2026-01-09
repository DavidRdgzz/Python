a= []
x= 1
while x != 0:
    x= int(input("pon numero (0 para terminar): "))
    if x != 0:
        a.append(x)
b= int(input("numero a buscar: "))
p= []
i= 0
while i<len(a):
    if a[i] ==b:
        p.append(i+1)
    i= i+1
print("posiciones:",p)
