#Numero mas alto

print("********************************************************************")
print("*                        Número más alto                           *")
print("********************************************************************")

numero1=input("Digite primer número: ")
numero2=input("Digite segundo número: ")
numero3=input("Digite tercero número: ")


if numero1>numero2 and numero1>numero3:
    print("El número "+ numero1+" es el mayor." )
else:
    if numero2>numero3:
        print("El número "+ numero2+" es el mayor." )
    else:
        print("El número "+ numero3+" es el mayor." )

    
        
