#Encapsulamiento
class encap:
    def __init__(self):
        self.numero=0
       # self.__numero al tener dos "__" son varables staticas 
    def operacion(self):
        print(self.numero+20)

    def resultado(self):
        return self.numero
    
ejemplo= encap()
ejemplo.operacion()
ejemplo.numero=100
print(ejemplo.resultado())