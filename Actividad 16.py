class Libro:
    def __init__(self, titulo, autor, año_Publicacion, Codigo):
        self.Codigo = Codigo
        self.titulo = titulo
        self.autor = autor
        self.año_Publicacion = año_Publicacion


    def mostrar_libro(self):
        return f"Codigo: {self.Codigo} - titulo: {self.titulo} - autor: {self.autor} - año Publicación: {self.año_Publicacion}"

class manipulacion:
    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        try:
            Codigo = int(input("Ingrese código de la libro: "))
            titulo = input("Ingrese titulo de la libro: ")
            autor = input("Ingrese autor de la libro: ")
            publicacion = input("Ingrese el año de la publicación: ")
            self.libros.append(Libro(titulo, autor, Codigo))
            print("Libros agregados\n")
        except ValueError:
            print("Error: el código debe ser números")

    def mostrar(self):
        if not self.libros:
            print("No hay libros registrados")
        else:
            print("\Listado de libros")
            for i, datos in enumerate(self.libros, start=1):
                print(f"{i}. {datos.mostrar_libro()}")