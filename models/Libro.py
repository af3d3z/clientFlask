class Libro:
    def __init__(self, id, precio, isbn, titulo, numpag, tematica, id_editorial):
        self.id = id
        self.precio = precio
        self.isbn = isbn
        self.titulo = titulo
        self.numpag = numpag
        self.tematica = tematica
        self.id_editorial = id_editorial

    def __str__(self):
        return (f"ID: {self.id}\nPrecio: {self.precio}€\nTitulo: {self.titulo}\nNº Páginas: {self.numpag}\nTemática: {self.tematica}\n"
                f"ID Editorial: {self.id_editorial}\n")

    def serialize(self):
        return {"id": self.id, "precio": self.precio, "isbn": self.isbn, "titulo": self.titulo, "numpag": self.numpag, "tematica": self.tematica, "id_editorial": self.id_editorial}