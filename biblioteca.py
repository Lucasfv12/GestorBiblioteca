class Biblioteca:

    __instancia = None

    def __init__(self):
        self.__materiales = []
        self.__socios = []
        self.__contador_material = 0
        self.__contador_socio = 0

    @classmethod
    def obtener_instancia(cls):
        if cls.__instancia is None:
            cls.__instancia = Biblioteca()
        return cls.__instancia

    # La biblioteca asigna identificadores únicos, así nunca se repiten
    def generar_codigo_material(self):
        self.__contador_material += 1
        return f"M{self.__contador_material:03d}"

    def generar_id_socio(self):
        self.__contador_socio += 1
        return f"S{self.__contador_socio:03d}"

    def registrar_material(self, material):
        self.__materiales.append(material)

    def registrar_socio(self, socio):
        self.__socios.append(socio)

    def prestar(self, codigo, id_socio):
        material = None
        socio = None
        for m in self.__materiales:
            if m.get_codigo() == codigo:
                material = m
        for s in self.__socios:
            if s.get_id() == id_socio:
                socio = s
        if material and socio and material.esta_disponible():
            material.marcar_prestado()
            socio.prestar_material(material)

    def devolver(self, codigo, id_socio):
        material = None
        socio = None
        for m in self.__materiales:
            if m.get_codigo() == codigo:
                material = m
        for s in self.__socios:
            if s.get_id() == id_socio:
                socio = s
        if material and socio:
            material.marcar_devuelto()
            socio.devolver_material(material)

    def materiales_disponibles(self):
        disponibles = []
        for material in self.__materiales:
            if material.esta_disponible():
                disponibles.append(material)
        return disponibles
