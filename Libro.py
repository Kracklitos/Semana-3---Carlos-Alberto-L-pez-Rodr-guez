class Libro:
    def __init__(self, titulo:str, autor:str, paginas:int):
        self.titulo=titulo
        self.autor= autor
        self.paginas= paginas
    
    def datos(self):
        print("El título del libro es : ", self.titulo, ", lo escribió : ",self.autor," y tiene ",self.paginas, " páginas")

libro = Libro("Edad de Oro","José Martí", 234)
libro.datos()