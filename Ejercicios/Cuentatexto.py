txt= (str(input("Pon el texto: ")))
busc= txt.find("Python")
if busc <= 0:
    print("No hay python en el texto") 
else:
    print(f"Python aparece un total de {busc} veces")