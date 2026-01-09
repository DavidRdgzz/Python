class Jugador:
    def __init__(self, dor, nom, eq):
        self.dorsal = dor
        self.nombre = nom
        self.equipo = eq
    def mostrar(self):
        print(f"{self.dorsal}. {self.nombre}: {self.equipo.nombre_equipo}")

class equipo:
    def __init__(self, nom_eq):
        self.nombre_equipo = nom_eq

equipo1 = equipo("Los Angeles Lakers")
equipo2 = equipo("Ducati")

jugador1 = Jugador(16, "Pau Gasol", equipo1)
jugador2 = Jugador(47, "Marc Marquez", equipo2)

jugador1.mostrar()
jugador2.mostrar()