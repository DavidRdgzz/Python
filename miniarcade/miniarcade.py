# MiniArcade.py
import random
import time
import os

def cargar_records():
    """Carga los mejores records desde records.txt"""
    records = {"ppt_victorias": 0, "adivina_mejor": 0, "calculo_mejor": 0}
    try:
        if os.path.exists("records.txt"):
            with open("records.txt", "r") as f:
                for linea in f:
                    if ":" in linea:
                        clave, valor = linea.strip().split(":", 1)
                        records[clave] = int(valor)
    except:
        pass  # Si hay error, usar valores por defecto
    return records

def guardar_records(records):
    """Guarda los records en records.txt"""
    try:
        with open("records.txt", "w") as f:
            for clave, valor in records.items():
                f.write(f"{clave}:{valor}\n")
    except:
        print("No se pudieron guardar los records")

def pedir_opcion():
    """Pide y valida la opcion del menu"""
    while True:
        op = input("Elige una opcion: ").strip()
        if op in {"0", "1", "2", "3", "4", "5"}:
            return op
        print("Opcion no valida. Intenta de nuevo.")

def juego_ppt(records):
    """
    Piedra, Papel o Tijera contra el ordenador
    Juega multiples rondas y lleva la cuenta
    """
    print("\n=== PIEDRA, PAPEL O TIJERA ===")
    opciones = ["piedra", "papel", "tijera"]
    victorias = 0
    derrotas = 0
    empates = 0
    
    print(f"Record actual: {records['ppt_victorias']} victorias consecutivas")
    
    while True:
        jugador = input("\nElige (piedra/papel/tijera) o 'salir': ").strip().lower()
        if jugador == "salir":
            break
        if jugador not in opciones:
            print("Opcion no valida")
            continue
        
        bot = random.choice(opciones)
        print(f"Tu eliges: {jugador}")
        print(f"Bot elige: {bot}")
        
        if jugador == bot:
            print("¡Empate!")
            empates += 1
        elif (jugador == "piedra" and bot == "tijera") or \
             (jugador == "papel" and bot == "piedra") or \
             (jugador == "tijera" and bot == "papel"):
            print("¡Ganaste!")
            victorias += 1
        else:
            print("¡Perdiste!")
            derrotas += 1
        
        print(f"Marcador -> V:{victorias} | D:{derrotas} | E:{empates}")
    
    # Actualizar record si es mejor
    if victorias > records["ppt_victorias"]:
        print(f"¡NUEVO RECORD! {victorias} victorias (anterior: {records['ppt_victorias']})")
        records["ppt_victorias"] = victorias
        guardar_records(records)
    
    print(f"\nResumen final: {victorias}V - {derrotas}D - {empates}E")
    return victorias

def juego_adivina(records):
    """
    Adivina el numero con niveles de dificultad
    Mide tiempo y da pistas Mayor/Menor
    """
    print("\n=== ADIVINA EL NUMERO ===")
    print(f"Record actual: {records['adivina_mejor']} puntos")
    print("\nElige dificultad:")
    print("1) Facil (1-20, 5 intentos)")
    print("2) Normal (1-50, 7 intentos)")
    print("3) Dificil (1-100, 10 intentos)")
    
    while True:
        dif = input("Dificultad (1/2/3): ").strip()
        if dif in {"1", "2", "3"}:
            break
        print("Opcion no valida")
    
    if dif == "1":
        rango, intentos = 20, 5
    elif dif == "2":
        rango, intentos = 50, 7
    else:
        rango, intentos = 100, 10
    
    numero = random.randint(1, rango)
    print(f"\nAdivina el numero entre 1 y {rango}")
    inicio = time.time()
    
    for i in range(intentos):
        try:
            guess = int(input(f"Intento {i+1}/{intentos}: "))
        except:
            print("Introduce un numero valido")
            continue
        
        if guess == numero:
            tiempo = time.time() - inicio
            puntos = int((intentos - i) * 50 + max(0, 100 - tiempo))
            print(f"¡CORRECTO! Lo adivinaste en {tiempo:.1f} segundos")
            print(f"Puntuacion: {puntos} puntos")
            
            if puntos > records["adivina_mejor"]:
                print(f"¡NUEVO RECORD! (anterior: {records['adivina_mejor']})")
                records["adivina_mejor"] = puntos
                guardar_records(records)
            return puntos
        elif guess < numero:
            print("Mayor!")
        else:
            print("Menor!")
    
    print(f"Perdiste. El numero era {numero}")
    return 0

def juego_calculo_mental(records, preguntas=8, tiempo_total=35):
    """
    Calculo mental con limite de tiempo
    Puntuacion por velocidad y aciertos
    """
    print(f"\n=== CALCULO MENTAL EXPRES ===")
    print(f"Record actual: {records['calculo_mejor']} puntos")
    print(f"Tienes {tiempo_total} segundos para {preguntas} operaciones")
    print("¡Cuanto mas rapido respondas, mas puntos!")
    
    input("Presiona ENTER cuando estes listo...")
    print("3... 2... 1... ¡YA!")
    time.sleep(0.5)
    
    aciertos = 0
    puntos_totales = 0
    inicio = time.time()
    
    for i in range(preguntas):
        if i < 3:
            a, b = random.randint(1, 10), random.randint(1, 10)
        else:
            a, b = random.randint(1, 20), random.randint(1, 15)
        
        op = random.choice(["+", "-", "*"])
        
        if op == "+":
            resultado = a + b
        elif op == "-":
            if a < b:
                a, b = b, a
            resultado = a - b
        else:
            resultado = a * b
        
        tiempo_restante = tiempo_total - (time.time() - inicio)
        if tiempo_restante <= 0:
            print("\n¡TIEMPO AGOTADO!")
            break
        
        progreso = "#" * (i+1) + "-" * (preguntas-i-1)
        print(f"\n[{progreso}] {i+1}/{preguntas} | Tiempo: {tiempo_restante:.1f}s")
        
        tiempo_pregunta = time.time()
        try:
            respuesta = int(input(f"{a} {op} {b} = "))
        except:
            print("Respuesta no valida")
            continue
        
        tiempo_usado = time.time() - tiempo_pregunta
        
        if respuesta == resultado:
            if tiempo_usado < 2:
                puntos_pregunta = 100
            elif tiempo_usado < 4:
                puntos_pregunta = 75
            elif tiempo_usado < 6:
                puntos_pregunta = 50
            else:
                puntos_pregunta = 25
            
            puntos_totales += puntos_pregunta
            print(f"¡Correcto! +{puntos_pregunta} puntos ({tiempo_usado:.1f}s)")
            aciertos += 1
        else:
            print(f"Incorrecto. Era {resultado}")
    
    if aciertos == preguntas:
        bonus = 200
        puntos_totales += bonus
        print(f"¡PERFECTO! Bonus: +{bonus} puntos")
    
    print(f"\n=== RESULTADOS ===")
    print(f"Aciertos: {aciertos}/{preguntas}")
    print(f"Puntuacion total: {puntos_totales} puntos")
    
    if puntos_totales > records["calculo_mejor"]:
        print(f"¡NUEVO RECORD! (anterior: {records['calculo_mejor']})")
        records["calculo_mejor"] = puntos_totales
        guardar_records(records)
    
    return puntos_totales

def juego_eco_invertido():
    """
    Eco loco: invierte texto y analiza estadisticas
    Cuenta caracteres, vocales y detecta palindromos
    """
    print("\n=== JUEGO DEL ECO INVERTIDO ===")
    print("Escribe frases y te las devolvere invertidas")
    print("Incluye estadisticas de caracteres y vocales")
    print("Linea vacia para salir")
    
    contador_frases = 0
    total_chars = 0
    total_vocales = 0
    
    while True:
        texto = input("\nTu frase: ")
        if texto == "":
            break
        
        contador_frases += 1
        invertida = texto[::-1]
        num_chars = len(texto)
        vocales = "aeiouAEIOU"
        num_vocales = sum(1 for c in texto if c in vocales)
        consonantes = sum(1 for c in texto if c.isalpha() and c not in vocales)
        espacios = texto.count(' ')
        
        total_chars += num_chars
        total_vocales += num_vocales
        
        print(f"Invertida: '{invertida}'")
        print(f"Longitud: {num_chars} caracteres")
        print(f"Vocales: {num_vocales} | Consonantes: {consonantes} | Espacios: {espacios}")
        
        if texto.lower() == invertida.lower():
            print("¡Es un PALINDROMO!")
        if num_vocales > consonantes:
            print("Frase muy vocalica")
        elif consonantes > num_vocales * 2:
            print("Frase muy consonantica")
    
    if contador_frases > 0:
        print(f"\nESTADISTICAS FINALES:")
        print(f"   Frases procesadas: {contador_frases}")
        print(f"   Caracteres totales: {total_chars}")
        print(f"   Vocales totales: {total_vocales}")
        print(f"   Promedio chars/frase: {total_chars/contador_frases:.1f}")
    
    print("¡Saliendo del eco!")

def mostrar_banner():
    """Muestra el banner ASCII del arcade"""
    print("""
    ╔═══════════════════════════════════════════╗
    ║   __  __ ___ _   _ ___      _             ║
    ║  |  \/  |_ _| \ | |_ _|    / \            ║
    ║  | |\/| || ||  \| || |    / _ \           ║
    ║  | |  | || || |\  || |   / ___ \          ║
    ║  |_|  |_|___|_| \_|___| /_/   \_\         ║
    ║      _    ____   ____    _    ____        ║
    ║     / \  |  _ \ / ___|  / \  |  _ \       ║
    ║    / _ \ | |_) | |     / _ \ | | | |      ║
    ║   / ___ \|  _ <| |___ / ___ \| |_| |      ║
    ║   /_/   \_\_| \_\\____/_/   \_\____/       ║
    ║                                           ║
    ║     LABORATORIO DE JUEGOS RETRO           ║
    ║         DEL DAVISS - VERSION 1.0          ║
    ╚═══════════════════════════════════════════╝
    """)

def mostrar_records(records):
    """Muestra los mejores records guardados"""
    print("\n=== SALON DE LA FAMA ===")
    print(f"PPT - Victorias consecutivas: {records['ppt_victorias']}")
    print(f"Adivina - Mejor puntuacion: {records['adivina_mejor']}")
    print(f"Calculo - Mejor puntuacion: {records['calculo_mejor']}")
    if any(records.values()):
        print("Records guardados en records.txt")
    else:
        print("¡Se el primero en establecer un record!")
    input("\nPresiona ENTER para continuar...")

def main():
    """Funcion principal que controla el bucle del menu"""
    mostrar_banner()
    print("Bienvenido/a al Mini Arcade!")
    print("Tu mision: ¡Batir todos los records!")
    
    # Cargar records existentes
    records = cargar_records()
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1) Piedra, Papel o Tijera")
        print("2) Adivina el numero")
        print("3) Calculo mental expres")
        print("4) Juego del eco invertido")
        print("5) Ver records (Salon de la Fama)")
        print("0) Salir")
        
        opcion = pedir_opcion()
        if opcion == "1":
            juego_ppt(records)
        elif opcion == "2":
            juego_adivina(records)
        elif opcion == "3":
            juego_calculo_mental(records)
        elif opcion == "4":
            juego_eco_invertido()
        elif opcion == "5":
            mostrar_records(records)
        elif opcion == "0":
            print("\n¡Gracias por jugar en el Mini Arcade!")
            print("Tus records han sido guardados")
            print("¡Hasta la proxima, gamer!")
            break
        time.sleep(0.8)

if __name__ == "__main__":
    main()  