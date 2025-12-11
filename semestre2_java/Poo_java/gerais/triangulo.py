class triangulo:
    def __init__(self,base,altura: int):
        self.__base = base
        self.__altura = altura

    def calcular_a_area(self) -> float:
        area = (self.__base * self.__altura) / 2
        return area
    
    def get_base(self):
        return self.__base
    
    def get_altura(self):
        return self.__altura
    
    def set_altura(self,nova_altura:float):
        self.__altura = nova_altura


    
tri_um = triangulo(9,15)

tri_dois = triangulo(10,1.9)

tri_tres = triangulo(20,50) 

tri_um.set_altura(55)

print("base e altura do t1: ",tri_um.get_base(),tri_um.get_altura())

print(tri_dois.calcular_a_area())

