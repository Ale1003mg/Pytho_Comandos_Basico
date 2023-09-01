#Condicional Basica
print("Condicional simple")
numero=int(input("Digite un numero: "))

if 5==numero:
        print("Es numero 5")
else:
    print("No es el numero 5")


print("Condicional")

#Condicional multiple
print("Condicional multiple")
if 5==numero:
    print("El numero es 5")
elif 6==numero:
    print("El numero es 6")
elif 8==numero:
    print("El numero es 8")
else:
    print("El numero no es 5,6,8")
print("Condicional multiple")

#Condicional anidada
print("Condicional anidada")

if 5<=numero:
    if 5<numero:
        if 6== numero:
            print("El numero es 6")
        elif 6>numero:
            print("El numero es mayor que 6")
        else:
            print("El numero es mayor 6")
    else:
        print("El numero es 5")
else:
    print ("El numero es menor que 5")

print("fin")
