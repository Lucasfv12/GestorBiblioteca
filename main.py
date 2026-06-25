from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from socio import Socio

#Obtenemos la única biblioteca (Utilizando Singleton)

biblioteca = Biblioteca.obtener_instancia()

#Creamos materiales y un socio

libro1 = Libro("L001","Principito","Antoine de Saint-Exupéry")
revista1 = Revista("R001","Caras",100)
socio1 = Socio("S001","Lucas")

#Los registramos en la biblioteca

biblioteca.registrar_material(libro1)
biblioteca.registrar_material(revista1)
biblioteca.registrar_socio(socio1)

print("---ESTADO INICIAL---")
print("Materiales disponibles:")
for material in biblioteca.materiales_disponibles():
    print(" -", material.get_titulo())

#El socio pide prestado un libro

print(\n--- El socio retira el Principito)
biblioteca.prestar("L001","S001")

print("Prestamos del socio: ")
for material in socio1.listar_prestamos():
    print(material.get_titulo())

print("Materiales disponibles: ")
for material in biblioteca.materiales_disponibles():
    print(" -", material.get_titulo())

#El socio devuelve el libro

print("\--- El socio devuelve el Principito ---")
biblioteca.devolver("L001","S001")

print("Prestamos del socio:")
prestamos = socio1.listar_prestamos()
if prestamos:
    for material in prestamos:
        print(" -", material.get_titulo())
else:
    print("(sin prestamos")

print("Materiales disponibles:")
for material in biblioteca.materiales_disponibles():
    print(" -", material.get_titulo())
