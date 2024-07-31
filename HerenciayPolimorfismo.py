class vehiculo:
    def __init__(self, marca,modelo):
        self.marca=marca
        self.modelo=modelo
    #clase padre
    def arracar(self):
        return f"{self.marca} {self.modelo} esta arrancando"
    
#clase hijo
#son herencias
class coche(vehiculo):
    def  acelerar(self):
        return f"{self.marca} {self.modelo} esta acelerando"

#clase hijo
#clase hijo
#son herencias
class motocicleta(vehiculo):
    def caballito(self):
        return f"{self.marca} {self.modelo} esta haciendo un caballito"
    
#herencia
cochee= coche("toyota","camry")
moto= motocicleta("Harley","sports")

print(f"Coche marca y modelo:{cochee.marca}, {cochee.modelo}")
print(f"Motocicleta marca y modelo: {moto.marca}, {moto.modelo}")


print(cochee.acelerar())
print(moto.caballito())

#polimorfismo
print(cochee.arracar())
print(moto.arracar())
    






    
