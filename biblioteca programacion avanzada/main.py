from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from socio import Socio

biblioteca = Biblioteca.obtener_instancia()

libro1 = Libro("L001","Principito","Antoine de Saint-Exupéry")
revista1 = Revista("R001","Caras",100)

socio1 = Socio("S001","Lucas")

biblioteca.registrar_material(libro1)
biblioteca.registrar_material(revista1)

biblioteca.registrar_socio(socio1)

biblioteca.prestar("L001","S001")

print("Prestamos del socio: ")

for material in socio1.listar_prestamos():
    print(material.get_titulo())

print("Materiales disponibles: ")

for material in biblioteca.materiales_disponibles():
    print(material.get_titulo())