# Programa que lee información de personas (nombre y edad) de un fichero de texto,
# y muestra por pantalla los datos de la persona más joven y más vieja del fichero.

import os

def leer_personas(fichero):
    """Lee el fichero y devuelve una lista de tuplas (nombre, edad)"""
    personas = []
    if not os.path.exists(fichero):
        print(f"Error: El fichero '{fichero}' no existe.")
        return personas
    
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            for num_linea, linea in enumerate(f, 1):
                linea = linea.strip()
                if not linea:
                    continue
                if ";" not in linea:
                    print(f"Advertencia línea {num_linea}: formato incorrecto")
                    continue
                token = linea.split(";")
                if len(token) != 2:
                    print(f"Advertencia línea {num_linea}: debe tener nombre;edad")
                    continue
                try:
                    nombre = token[0].strip()
                    edad = int(token[1].strip())
                    personas.append((nombre, edad))
                except ValueError:
                    print(f"Advertencia línea {num_linea}: edad debe ser un número")
    except Exception as e:
        print(f"Error al leer el fichero: {e}")
    
    return personas

def obtiene_edad(persona):
    """Devuelve la edad de una persona"""
    return persona[1]

def persona_mas_joven(personas):
    """Devuelve la persona más joven de la lista"""
    joven = personas[0]
    for persona in personas:
        if obtiene_edad(persona) < obtiene_edad(joven):
            joven = persona
    return joven

def persona_mas_vieja(personas):
    """Devuelve la persona más vieja de la lista"""
    vieja = personas[0]
    for persona in personas:
        if obtiene_edad(persona) > obtiene_edad(vieja):
            vieja = persona
    return vieja

# --- Programa principal ---
print("Leyendo fichero 'personas.txt'...")
personas = leer_personas("personas.txt")
print(f"Se han leído {len(personas)} personas.")

if personas:
    joven = persona_mas_joven(personas)
    vieja = persona_mas_vieja(personas)
    print(f"La persona más joven es: {joven[0]} ({joven[1]} años)")
    print(f"La persona más vieja es: {vieja[0]} ({vieja[1]} años)")
else:
    print("No hay datos válidos en el fichero.")