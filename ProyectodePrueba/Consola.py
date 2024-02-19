import Dao_Usuario 
print("*******************************************************************************************************************************")
print("******************************************Mantenimiento de Usuarios************************************************************")
print("*******************************************************************************************************************************")

#from es de la carpeta de donde lo va a llamar el importa la clase o el dao

#datos = Getall()


#u_id, u_nombre, u_apellidos,  u_cedula, u_telefono, u_correo, u_dirreccion, u_sexo, u_estado, u_contrasena,u_accion
print (f"{Dao_Usuario.Mantenimiento(26,'Alejandro','Marin','113412588','87598462','amg1004@hotmail.com','curridabat',1,True,'12345',2)}")

print( f"{Dao_Usuario.Getall()}")