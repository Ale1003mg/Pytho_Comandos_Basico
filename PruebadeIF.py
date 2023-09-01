#Ejercicio
#Consultar Dias de Trabajo a coider a los datos ingresados

print("********************************************************************")
print("*                        Días de Vacaciones                        *")
print("********************************************************************")

Nombre=str(input("Digite su nombre: "))
Clave=int(input("Digite su Clave de apartamento: "))
Ano=int(input("Digite la fecha que entro: "))

Anos=2023-Ano

if Clave==1:
    if Anos>=7:
        print(Nombre+" tiene 20 días de vacaciones")
    elif Anos>=2:
        print(Nombre+" tiene 14 dias de vacaciones")
    elif Anos==1:
        print(Nombre+" tiene 6 días de vacaciones")
    else:
        print(Nombre+" No tiene días de vacaciones")

elif Clave==2:
    if Anos>=7:
        print(Nombre+" tiene 22 días de vacaciones")
    elif Anos>=2:
        print(Nombre+" tiene 15 dias de vacaciones")
    elif Anos==1:
        print(Nombre+" tiene 7 días de vacaciones")
    else:
        print(Nombre+" No tiene días de vacaciones")
    
elif Clave==3:
    if Anos>=7:
        print(Nombre+" tiene 30 días de vacaciones")
    elif Anos>=2:
        print(Nombre+" tiene 20 dias de vacaciones")
    elif Anos==1:
        print(Nombre+" tiene 10 días de vacaciones")
    else:
        print(Nombre+" No tiene días de vacaciones")

else:
    print(Nombre+" No digito la clave de su apartamento")
