import numpy as np

class Pila2:
    __dimension: int = None
    __tope: int = None
    __tipo: type = None
    __arreglo: np.ndarray = None

    def __init__(self, tipo:type=int, dimension:int=20) -> None:
        assert isinstance(dimension, int), "La dimension de la pila debe ser un entero"
        self.__dimension = dimension
        self.__tope = 0
        self.__tipo = tipo
        self.__arreglo = np.empty(self.__dimension, dtype=self.__tipo)
    
    def vacia(self) -> bool:
        return self.__tope == 0
    
    def llena(self) -> bool:
        return self.__dimension == self.__tope
    
    def apilar(self, elemento):
        assert isinstance(elemento, self.__tipo), "Solo se pueden apilar datos del tipo {0}, no {1}".format(self.__tipo, type(elemento))
        if self.llena():
            raise OverflowError
        self.__arreglo[self.__tope] = elemento
        self.__tope += 1
        return elemento
    
    def desapilar(self):
        if self.vacia():
            raise Exception("No hay mas elementos")
        self.__tope -= 1
        elemento = self.__arreglo[self.__tope]
        return elemento
    
    
    def getDimension(self) -> int:
        return self.__dimension
    
    def getCantidad(self) -> int:
        return self.__tope