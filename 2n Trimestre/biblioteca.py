class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        pass
    def mostrar_info(self):
        print(f"el título es {self.titulo} y el autor es {self.autor}")

mi_libro = Libro("Luna de pluton", "Dross")

mi_libro.mostrar_info()

class Usuario:
    def __init__(self,nombre):
        self.nombre = nombre
        pass
    def mostrar_usuario(self):
        print(f"El usuario es {self.nombre}")

user1 = Usuario("duma")
user1.mostrar_usuario()

class Biblioteca:
    def __init__(self):
        self.libros = []
        pass
    def agregar_libro(self,libro):
        self.libros.append(libro.titulo)
    def mostrar_libros(self):
        print(f"estos son los libros que hay: {self.libros}")

mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_libro(mi_libro)  

mi_biblioteca.mostrar_libros()