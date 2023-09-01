#numero par o impar
print("********************************************************************")
print("*                        Número par o impar                        *")
print("********************************************************************")
Numero=int( input("Digite un numero: "))

resultado= Numero%2

if resultado==0:
    print("Es un numero par")
elif resultado==1:
    print("Es un numero impar")

print("Fin")
