# MiniArcade.py - Version principiante
import random
import time

def cargar_records():
    """Carga los mejores records desde records.txt"""
    records = {"ppt_victorias": 0, "adivina_mejor": 0, "calculo_mejor": 0}
    try:
        archivo = open("records.txt", "r")
        lineas = archivo.readlines()
        for linea in lineas:
            if ":" in linea:
                partes = linea.strip().split(":")
                clave = partes[0]
                valor = int(partes[1])
                records[clave] = valor
        archivo.close()
    except:
        pass
    return records

def guardar_records(records):
    """Guarda los records en records.txt"""
    try:
        archivo = open("records.txt", "w")
        archivo.write("ppt_victorias:" + str(records["ppt_victorias"]) + "\n")
        archivo.write("adivina_mejor:" + str(records["adivina_mejor"]) + "\n")
        archivo.write("calculo_mejor:" + str(records["calculo_mejor"]) + "\n")
        archivo.close()
    except:
        print("No se pudieron guardar los records")

def pedir_opcion():
    """Pide y valida la opcion del menu"""
    op = input("Elige una opcion: ")
    while op != "0" and op != "1" and op != "2" and op != "3" and op != "4" and op != "5":
        print("Opcion no valida. Intenta de nuevo.")
        op = input("Elige una opcion: ")
    return op

def juego_ppt(records):
    """
    Piedra, Papel o Tijera contra el ordenador
    Juega multiples rondas y lleva la cuenta
    """
    print("\n=== PIEDRA, PAPEL O TIJERA ===")
    victorias = 0
    derrotas = 0
    empates = 0
    
    print("Record actual: " + str(records['ppt_victorias']) + " victorias consecutivas")
    
    jugando = True
    while jugando:
        jugador = input("\nElige (piedra/papel/tijera) o 'salir': ")
        jugador = jugador.lower()
        
        if jugador == "salir":
            jugando = False
        elif jugador == "piedra" or jugador == "papel" or jugador == "tijera":
            numero = random.randint(1, 3)
            if numero == 1:
                bot = "piedra"
            elif numero == 2:
                bot = "papel"
            else:
                bot = "tijera"
            
            print("Tu eliges: " + jugador)
            print("Bot elige: " + bot)
            
            if jugador == bot:
                print("¡Empate!")
                empates = empates + 1
            elif (jugador == "piedra" and bot == "tijera") or (jugador == "papel" and bot == "piedra") or (jugador == "tijera" and bot == "papel"):
                print("¡Ganaste!")
                victorias = victorias + 1
            else:
                print("¡Perdiste!")
                derrotas = derrotas + 1
            
            print("Marcador -> V:" + str(victorias) + " | D:" + str(derrotas) + " | E:" + str(empates))
        else:
            print("Opcion no valida")
    
    # Actualizar record si es mejor
    if victorias > records["ppt_victorias"]:
        print("¡NUEVO RECORD! " + str(victorias) + " victorias (anterior: " + str(records['ppt_victorias']) + ")")
        records["ppt_victorias"] = victorias
        guardar_records(records)
    
    print("\nResumen final: " + str(victorias) + "V - " + str(derrotas) + "D - " + str(empates) + "E")
    return victorias

def juego_adivina(records):
    """
    Adivina el numero con niveles de dificultad
    Mide tiempo y da pistas Mayor/Menor
    """
    print("\n=== ADIVINA EL NUMERO ===")
    print("Record actual: " + str(records['adivina_mejor']) + " puntos")
    print("\nElige dificultad:")
    print("1) Facil (1-20, 5 intentos)")
    print("2) Normal (1-50, 7 intentos)")
    print("3) Dificil (1-100, 10 intentos)")
    
    dif = input("Dificultad (1/2/3): ")
    while dif != "1" and dif != "2" and dif != "3":
        print("Opcion no valida")
        dif = input("Dificultad (1/2/3): ")
    
    if dif == "1":
        rango = 20
        intentos = 5
    elif dif == "2":
        rango = 50
        intentos = 7
    else:
        rango = 100
        intentos = 10
    
    numero = random.randint(1, rango)
    print("\nAdivina el numero entre 1 y " + str(rango))
    inicio = time.time()
    
    i = 0
    acertado = False
    while i < intentos and not acertado:
        try:
            texto = input("Intento " + str(i+1) + "/" + str(intentos) + ": ")
            guess = int(texto)
            
            if guess == numero:
                tiempo = time.time() - inicio
                puntos = (intentos - i) * 50
                if tiempo < 100:
                    puntos = puntos + (100 - int(tiempo))
                
                print("¡CORRECTO! Lo adivinaste en " + str(round(tiempo, 1)) + " segundos")
                print("Puntuacion: " + str(puntos) + " puntos")
                
                if puntos > records["adivina_mejor"]:
                    print("¡NUEVO RECORD! (anterior: " + str(records['adivina_mejor']) + ")")
                    records["adivina_mejor"] = puntos
                    guardar_records(records)
                
                acertado = True
                return puntos
            elif guess < numero:
                print("Mayor!")
            else:
                print("Menor!")
            
            i = i + 1
        except:
            print("Introduce un numero valido")
    
    if not acertado:
        print("Perdiste. El numero era " + str(numero))
    return 0

def juego_calculo_mental(records):
    """
    Calculo mental con limite de tiempo
    Puntuacion por velocidad y aciertos
    """
    preguntas = 8
    tiempo_total = 35
    
    print("\n=== CALCULO MENTAL EXPRES ===")
    print("Record actual: " + str(records['calculo_mejor']) + " puntos")
    print("Tienes " + str(tiempo_total) + " segundos para " + str(preguntas) + " operaciones")
    print("¡Cuanto mas rapido respondas, mas puntos!")
    
    input("Presiona ENTER cuando estes listo...")
    print("3... 2... 1... ¡YA!")
    time.sleep(0.5)
    
    aciertos = 0
    puntos_totales = 0
    inicio = time.time()
    
    i = 0
    while i < preguntas:
        tiempo_ahora = time.time() - inicio
        if tiempo_ahora >= tiempo_total:
            print("\n¡TIEMPO AGOTADO!")
            break
        
        if i < 3:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        else:
            a = random.randint(1, 20)
            b = random.randint(1, 15)
        
        numero_op = random.randint(1, 3)
        if numero_op == 1:
            op = "+"
            resultado = a + b
        elif numero_op == 2:
            op = "-"
            if a < b:
                temp = a
                a = b
                b = temp
            resultado = a - b
        else:
            op = "*"
            resultado = a * b
        
        tiempo_restante = tiempo_total - tiempo_ahora
        progreso = ""
        j = 0
        while j < i + 1:
            progreso = progreso + "#"
            j = j + 1
        j = 0
        while j < preguntas - i - 1:
            progreso = progreso + "-"
            j = j + 1
        
        print("\n[" + progreso + "] " + str(i+1) + "/" + str(preguntas) + " | Tiempo: " + str(round(tiempo_restante, 1)) + "s")
        
        tiempo_pregunta = time.time()
        try:
            texto = input(str(a) + " " + op + " " + str(b) + " = ")
            respuesta = int(texto)
            
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
                
                puntos_totales = puntos_totales + puntos_pregunta
                print("¡Correcto! +" + str(puntos_pregunta) + " puntos (" + str(round(tiempo_usado, 1)) + "s)")
                aciertos = aciertos + 1
            else:
                print("Incorrecto. Era " + str(resultado))
        except:
            print("Respuesta no valida")
        
        i = i + 1
    
    if aciertos == preguntas:
        bonus = 200
        puntos_totales = puntos_totales + bonus
        print("¡PERFECTO! Bonus: +" + str(bonus) + " puntos")
    
    print("\n=== RESULTADOS ===")
    print("Aciertos: " + str(aciertos) + "/" + str(preguntas))
    print("Puntuacion total: " + str(puntos_totales) + " puntos")
    
    if puntos_totales > records["calculo_mejor"]:
        print("¡NUEVO RECORD! (anterior: " + str(records['calculo_mejor']) + ")")
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
    
    jugando = True
    while jugando:
        texto = input("\nTu frase: ")
        if texto == "":
            jugando = False
        else:
            contador_frases = contador_frases + 1
            
            # Invertir texto
            invertida = ""
            i = len(texto) - 1
            while i >= 0:
                invertida = invertida + texto[i]
                i = i - 1
            
            num_chars = len(texto)
            
            # Contar vocales
            num_vocales = 0
            vocales = "aeiouAEIOU"
            i = 0
            while i < len(texto):
                if texto[i] in vocales:
                    num_vocales = num_vocales + 1
                i = i + 1
            
            # Contar consonantes
            consonantes = 0
            i = 0
            while i < len(texto):
                letra = texto[i]
                if (letra >= 'a' and letra <= 'z') or (letra >= 'A' and letra <= 'Z'):
                    if letra not in vocales:
                        consonantes = consonantes + 1
                i = i + 1
            
            # Contar espacios
            espacios = 0
            i = 0
            while i < len(texto):
                if texto[i] == ' ':
                    espacios = espacios + 1
                i = i + 1
            
            total_chars = total_chars + num_chars
            total_vocales = total_vocales + num_vocales
            
            print("Invertida: '" + invertida + "'")
            print("Longitud: " + str(num_chars) + " caracteres")
            print("Vocales: " + str(num_vocales) + " | Consonantes: " + str(consonantes) + " | Espacios: " + str(espacios))
            
            if texto.lower() == invertida.lower():
                print("¡Es un PALINDROMO!")
            if num_vocales > consonantes:
                print("Frase muy vocalica")
            elif consonantes > num_vocales * 2:
                print("Frase muy consonantica")
    
    if contador_frases > 0:
        print("\nESTADISTICAS FINALES:")
        print("   Frases procesadas: " + str(contador_frases))
        print("   Caracteres totales: " + str(total_chars))
        print("   Vocales totales: " + str(total_vocales))
        promedio = total_chars / contador_frases
        print("   Promedio chars/frase: " + str(round(promedio, 1)))
    
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
    print("PPT - Victorias consecutivas: " + str(records['ppt_victorias']))
    print("Adivina - Mejor puntuacion: " + str(records['adivina_mejor']))
    print("Calculo - Mejor puntuacion: " + str(records['calculo_mejor']))
    
    hay_records = False
    if records['ppt_victorias'] > 0 or records['adivina_mejor'] > 0 or records['calculo_mejor'] > 0:
        hay_records = True
    
    if hay_records:
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
    
    jugando = True
    while jugando:
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
            jugando = False
        
        time.sleep(0.8)

# Programa principal
main()