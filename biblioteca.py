class Biblioteca:

        __instacia = None

        def __init__(self,materiales,socios):
                self.materiales = [] 
                self.socios = [] 
        @classmethod
        def obtener_instancia(cls):
                if cls.__instacia is None:
                        cls.__instacia = Biblioteca
                        return cls.__instancia

        def registrar_material(self,material):
                self.__socios.appernd(material)

        def registrar_socio(self, socio):
                self.__socios.append(socio)

        def prestar(self, codigo, id_socio):

                material = None
                socio = None
                
                for m in self.__materiales:
                        if m.get_codigo() == codigo:
                                material = m
                for s in self.__materiales:
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
                for s in self.__materiales:
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