class Socio:
    def __init__(self, id_socio, nombre, apellido):
        self.__id_socio = id_socio
        self.__nombre = nombre
        self.__apellido = apellido
        self.__materiales_prestados = []

    def get_id(self):
        return self.__id_socio

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    def prestar_material(self, material):
        self.__materiales_prestados.append(material)

    def devolver_material(self, material):
        if material in self.__materiales_prestados:
            self.__materiales_prestados.remove(material)

    def listar_prestamos(self):
        return self.__materiales_prestados
