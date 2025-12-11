class retangular:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.altura* self.base
retango_primario = retangular(12,15)
print(retango_primario.base)
print(retango_primario.altura)

calc = retango_primario.calcular_area()
print("Area: ",calc)

rangulo_secundario = retangular(9,12)

calculal = rangulo_secundario.calcular_area()
print("Area: ",calculal)