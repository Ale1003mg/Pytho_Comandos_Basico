class Calculadora1:
    def __init__(self, numero):
        self.resultado=numero
    
    def sumar(self, numero):
        self.resultado+=+numero

    def  resta(self,numero):
        self.resultado-=numero
    
    def multiplicar(self, numero):
        self.resultado*=numero

    def division(self, numero):
        if numero !=0:
            self.resultado /=numero
        else:
            print("No se pudo dividir")
    
    def resultado(self):
        return self.resultado


Calculo=Calculadora1(0)
Calculo.sumar(10)
Calculo.multiplicar(4)
Calculo.resta(5)
Calculo.division(2)
resultado= Calculo.resultado
print(f"Resultado: ", resultado)
