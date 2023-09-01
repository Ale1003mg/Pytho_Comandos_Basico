mensaje="Hola"
mensaje+=" "
mensaje+="Mundo"
print(mensaje)

Nombre="Alejandro"
Apellido1=" Marin "
Apellido2="Guzman"
print(Nombre+Apellido1+Apellido2)

numero_uno=6
numero_dos=4
resultado=numero_uno+numero_dos
resultado= str(resultado)
print("La suma de las dos variables es: "+resultado)

mensaje= "Alejandro Marin Guzman"
buscar=mensaje.find("Marin")
print(buscar)

mensaje= "Alejandro Marin Guzman"
buscar=mensaje[0:9]
print(buscar)

mensaje1= "Alejandro Marin Guzman"
mensaje2= "Alejandro Marin Guzman"
print("igual datos "+mensaje1==mensaje2)

mensaje1= "Alejandro Marin Guzman"
mensaje2= "Alejandro Marín Guzmán"
print("diferente "+mensaje1==mensaje2)
