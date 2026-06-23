from material import Material

class Revista (Material):
        def __init__(self,codigo,titulo,numero_edicion):
            super().__init__(codigo,titulo)
            self.__numero_edicion = numero_edicion
    
        def dias_de_prestamo(self):
            return 7