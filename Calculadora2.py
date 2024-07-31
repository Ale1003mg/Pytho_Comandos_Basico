class Calculadora:
    def suma(self,numero1, numero2):
        return numero1+numero2
    def resta(self,numero1, numero2):
        return numero1-numero2
    def multiplicar(self,numero1, numero2):
        return numero1*numero2
    def Dividir(self,numero1, numero2):
        if numero2!=0:
                return numero1/numero2
   
    
Numero1= float(input("Inserte primer Numero: "))
Numero2= float(input("Inserte Segundo Numero: "))


result=Calculadora()
Suma=result.suma(Numero1,Numero2)
Resta=result.resta(Numero1,Numero2)
Multiplicacion=result.multiplicar(Numero1,Numero2)
Divicion=result.Dividir(Numero1,Numero2)

print("Suma: ",Suma)
print("Resta: ", Resta)
print("Multiplicacion: ",Multiplicacion)
print("Divicion: ", Divicion)


