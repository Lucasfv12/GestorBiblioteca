from material import Material

class Libro(Material):
        def __init__(self,codigo,titulo,autor):
            super().__init__(codigo,titulo)
            self.__autor = autor

        def dias_de_prestamo(self):
            return 15