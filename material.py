from abc import ABC, abstractmethod

class Material(ABC):
     
     def __init__(self,codigo,titulo):
          self.__codigo = codigo
          self.__titulo = titulo
          self.__disponible = True
     
     def get_codigo(self):
          return self.__codigo
               
     def get_titulo(self):
          return self.__titulo

     def esta_disponible(self):
          return self.__disponible

     def marcar_prestado(self): 
          self.__disponible = False

     def marcar_devuelto(self):
          self.__disponible = True

     @abstractmethod
     def dias_de_prestamo(self):
          pass