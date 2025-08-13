class Libro:
    def __init__(self, titulo, autor, año_Publicacion, Codigo):
        self.Codigo = Codigo
        self.titulo = titulo
        self.autor = autor
        self.año_Publicacion = año_Publicacion


    def mostrar_libro(self):
        return f"Codigo: {self.Codigo} - titulo: {self.titulo} - autor: {self.autor} - año Publicación: {self.año_Publicacion}"