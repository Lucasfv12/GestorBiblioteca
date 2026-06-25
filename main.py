from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from socio import Socio

# Obtenemos la única biblioteca (patrón Singleton)
biblioteca = Biblioteca.obtener_instancia()

# Referencias locales para buscar/mostrar desde el menú
materiales = {}   # codigo -> objeto Material
socios = {}       # id_socio -> objeto Socio


def pregunta_si(texto):
    return input(texto + " (s/n): ").strip().lower() == "s"


def tipo_material(material):
    return "Libro" if isinstance(material, Libro) else "Revista"


def registrar_libro():
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    if not titulo:
        print("✗ El título no puede estar vacío.\n")
        return
    codigo = biblioteca.generar_codigo_material()   # el sistema asigna el código
    libro = Libro(codigo, titulo, autor)
    biblioteca.registrar_material(libro)
    materiales[codigo] = libro
    print(f"✓ Libro '{titulo}' registrado con código {codigo}.\n")


def registrar_revista():
    titulo = input("Título: ").strip()
    edicion = input("Número de edición: ").strip()
    if not titulo:
        print("✗ El título no puede estar vacío.\n")
        return
    codigo = biblioteca.generar_codigo_material()
    revista = Revista(codigo, titulo, edicion)
    biblioteca.registrar_material(revista)
    materiales[codigo] = revista
    print(f"✓ Revista '{titulo}' registrada con código {codigo}.\n")


def registrar_socio():
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    if not nombre or not apellido:
        print("✗ Nombre y apellido son obligatorios.\n")
        return
    id_socio = biblioteca.generar_id_socio()   # el sistema asigna el ID
    socio = Socio(id_socio, nombre, apellido)
    biblioteca.registrar_socio(socio)
    socios[id_socio] = socio
    print(f"✓ Socio '{socio.get_nombre_completo()}' registrado con ID {id_socio}.\n")


def listar_disponibles():
    disponibles = biblioteca.materiales_disponibles()
    print("--- Materiales disponibles ---")
    if not disponibles:
        print("(no hay materiales disponibles)")
    for m in disponibles:
        print(f" [{m.get_codigo()}] {m.get_titulo()} - {tipo_material(m)} ({m.dias_de_prestamo()} días)")
    print()


def listar_socios():
    print("--- Socios registrados ---")
    if not socios:
        print("(no hay socios registrados)")
    for s in socios.values():
        print(f" [{s.get_id()}] {s.get_nombre_completo()}")
    print()


def prestar():
    if pregunta_si("¿Querés ver los materiales disponibles?"):
        listar_disponibles()
    codigo = input("Código del material a prestar: ").strip()

    material = materiales.get(codigo)
    if material is None:
        print("✗ No existe un material con ese código.\n")
        return
    if not material.esta_disponible():
        print("✗ Ese material ya está prestado.\n")
        return

    if pregunta_si("¿Querés ver la lista de socios?"):
        listar_socios()
    id_socio = input("ID del socio: ").strip()
    if id_socio not in socios:
        print("✗ No existe un socio con ese ID.\n")
        return

    biblioteca.prestar(codigo, id_socio)
    print(f"✓ '{material.get_titulo()}' prestado a {socios[id_socio].get_nombre_completo()}.\n")


def devolver():
    if pregunta_si("¿Querés ver la lista de socios?"):
        listar_socios()
    id_socio = input("ID del socio: ").strip()
    socio = socios.get(id_socio)
    if socio is None:
        print("✗ No existe un socio con ese ID.\n")
        return

    prestamos = socio.listar_prestamos()
    if not prestamos:
        print("Ese socio no tiene materiales prestados.\n")
        return
    print(f"--- Préstamos de {socio.get_nombre_completo()} ---")
    for m in prestamos:
        print(f" [{m.get_codigo()}] {m.get_titulo()}")

    codigo = input("Código del material a devolver: ").strip()
    material = materiales.get(codigo)
    if material is None or material not in prestamos:
        print("✗ Ese material no figura entre los préstamos de este socio.\n")
        return

    biblioteca.devolver(codigo, id_socio)
    print(f"✓ '{material.get_titulo()}' devuelto.\n")


def ver_prestamos():
    if pregunta_si("¿Querés ver la lista de socios?"):
        listar_socios()
    id_socio = input("ID del socio: ").strip()
    socio = socios.get(id_socio)
    if socio is None:
        print("✗ No existe un socio con ese ID.\n")
        return

    prestamos = socio.listar_prestamos()
    print(f"--- Préstamos de {socio.get_nombre_completo()} ---")
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
    print("5. Listar socios")
    print("6. Prestar material")
    print("7. Devolver material")
    print("8. Ver préstamos de un socio")
    print("0. Salir")


def main():
    opciones = {
        "1": registrar_libro,
        "2": registrar_revista,
        "3": registrar_socio,
        "4": listar_disponibles,
        "5": listar_socios,
        "6": prestar,
        "7": devolver,
        "8": ver_prestamos,
    }
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()
        print()
        if opcion == "0":
            print("¡Hasta luego!")
            break
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("✗ Opción inválida.\n")


if __name__ == "__main__":
    main()
