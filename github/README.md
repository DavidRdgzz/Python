# 🕹️ Mini-Arcade - Laboratorio de Juegos Retro

Mini-Arcade en consola con 4 juegos diferentes usando Python.

## 🎮 Juegos incluidos

### 1. Piedra, Papel o Tijera
- Juega contra el ordenador
- El bot elige aleatoriamente
- Puedes jugar varias rondas
- Escribe 'salir' para volver al menú

### 2. Adivina el número
- Adivina un número entre 1 y 20
- Tienes 5 intentos
- Recibe pistas: "Mayor!" o "Menor!"
- Mide tu tiempo de resolución

### 3. Cálculo mental exprés
- 8 operaciones de suma, resta o multiplicación
- 35 segundos de tiempo total
- Números entre 1 y 20
- Muestra tu puntuación final

### 4. Juego del eco invertido
- Escribe frases y te las devuelve invertidas
- Cuenta caracteres totales
- Cuenta vocales
- Línea vacía para salir

## 🚀 Cómo ejecutar

```powershell
python miniarcade.py
```

O desde el directorio:
```powershell
python "c:\Users\david\Desktop\Clase\PROG\LAB\Python\miniarcade.py"
```

## 📋 Requisitos técnicos cumplidos

✅ Estructura con `main()` y funciones separadas  
✅ Bloque protector `if __name__ == "__main__"`  
✅ Validación de entrada con bucle while  
✅ Uso de `random` (PPT, adivina, cálculo mental)  
✅ Uso de `time` (cronómetro, time.sleep, tiempo límite)  
✅ Mensajes claros y UX básica  
✅ Manejo de entradas inválidas con try/except  

## 🎯 Extras implementados

- Tiempo límite en cálculo mental
- Cronómetro en adivina el número
- Modo multi-ronda en PPT
- Contador de vocales en eco invertido

## 📝 Notas

- Solo usa librerías estándar (random, time)
- Código comentado con docstrings
- Sin librerías externas
- Validación robusta de entradas
