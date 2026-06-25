from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from socio import Socio

# Obtenemos la única biblioteca (patrón Singleton)
biblioteca = Biblioteca.obtener_instancia()

# Guardamos referencias locales solo para poder mostrar/buscar
# materiales y socios desde el menú (la biblioteca los administra de verdad).
materiales = {}   # codigo -> objeto Material
socios = {}       # id_socio -> objeto Socio


def registrar_libro():
    codigo = input("Código del libro: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    libro = Libro(codigo, titulo, autor)
    biblioteca.registrar_material(libro)
    materiales[codigo] = libro
    print(f"✓ Libro '{titulo}' registrado.\n")


def registrar_revista():
    codigo = input("Código de la revista: ")
    titulo = input("Título: ")
    edicion = input("Número de edición: ")
    revista = Revista(codigo, titulo, edicion)
    biblioteca.registrar_material(revista)
    materiales[codigo] = revista
    print(f"✓ Revista '{titulo}' registrada.\n")


def registrar_socio():
    id_socio = input("ID del socio: ")
    nombre = input("Nombre: ")
    socio = Socio(id_socio, nombre)
    biblioteca.registrar_socio(socio)
    socios[id_socio] = socio
    print(f"✓ Socio '{nombre}' registrado.\n")


def listar_disponibles():
    disponibles = biblioteca.materiales_disponibles()
    print("--- Materiales disponibles ---")
    if not disponibles:
        print("(no hay materiales disponibles)")
    for m in disponibles:
        print(f" [{m.get_codigo()}] {m.get_titulo()} - {m.dias_de_prestamo()} días")
    print()


def prestar():
    codigo = input("Código del material a prestar: ")
    id_socio = input("ID del socio: ")

    material = materiales.get(codigo)
    if material is None:
        print("✗ No existe un material con ese código.\n")
        return
    if id_socio not in socios:
        print("✗ No existe un socio con ese ID.\n")
        return
    if not material.esta_disponible():
        print("✗ Ese material ya está prestado.\n")
        return

    biblioteca.prestar(codigo, id_socio)
    print(f"✓ '{material.get_titulo()}' prestado al socio {id_socio}.\n")


def devolver():
    codigo = input("Código del material a devolver: ")
    id_socio = input("ID del socio: ")

    material = materiales.get(codigo)
    if material is None:
        print("✗ No existe un material con ese código.\n")
        return
    if id_socio not in socios:
        print("✗ No existe un socio con ese ID.\n")
        return

    biblioteca.devolver(codigo, id_socio)
    print(f"✓ '{material.get_titulo()}' devuelto.\n")


def ver_prestamos():
    id_socio = input("ID del socio: ")
    socio = socios.get(id_socio)
    if socio is None:
        print("✗ No existe un socio con ese ID.\n")
        return

    prestamos = socio.listar_prestamos()
    print(f"--- Préstamos del socio {id_socio} ---")
    if not prestamos:
        print("(sin préstamos)")
    for m in prestamos:
        print(f" [{m.get_codigo()}] {m.get_titulo()}")
    print()


def mostrar_menu():
    print("=" * 32)
    print("   SISTEMA DE BIBLIOTECA")
    print("=" * 32)
    print("1. Registrar libro")
    print("2. Registrar revista")
    print("3. Registrar socio")
    print("4. Listar materiales disponibles")
    print("5. Prestar material")
    print("6. Devolver material")
    print("7. Ver préstamos de un socio")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")
        print()

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            registrar_revista()
        elif opcion == "3":
            registrar_socio()
        elif opcion == "4":
            listar_disponibles()
        elif opcion == "5":
            prestar()
        elif opcion == "6":
            devolver()
        elif opcion == "7":
            ver_prestamos()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("✗ Opción inválida.\n")


if __name__ == "__main__":
    main()
