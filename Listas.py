#Vector
Lista=["Ale",1,"prueba"]

for prueba in Lista:
    print(prueba)
print("Fin")
print(Lista[0])
print("******************************************************************")

"""--------------------------------------------------------------------"""
#Modificar
Lista[1]=20
#Incertar
Lista.insert(0,"Katty")
#Agregar
Lista.append("Prueba2")
for prueba in Lista:
    print(prueba)
print("Fin 2")
print("******************************************************************")

Lista.append("Prueba3")
Lista.append("Prueba4")


for prueba in Lista:
    print(prueba)
print("Fin 3")
print("******************************************************************")

#Eliminar
Lista.pop(0)
for prueba in Lista:
    print(prueba)
print("Fin 4")
print("******************************************************************")
