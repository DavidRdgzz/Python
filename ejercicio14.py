entrada = input("Introduce nombres separados por comas: ")
nombres = [n.strip() for n in entrada.split(',') if n.strip()]
invertidos = list(reversed(nombres))
print(', '.join(invertidos))
