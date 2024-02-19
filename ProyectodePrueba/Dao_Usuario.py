#from Dto import Dto_Usuario
import pyodbc

server='localhost,14333'
db='BD_Pruebas_Microservicios'
soporte='sa'
contrasena='AdminServer1234'


try:
    conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+db+';UID='+soporte+';PWD='+contrasena)
    print("Conexion Exitosa")
except:
    print("Error de conexion")

def Getall():
    cursor= conexion.cursor()
    cursor.execute("SELECT *   FROM FC_Get_Usuarios()")
    personas=cursor.fetchall()
    #for per in personas:
        #print(per)
    cursor.close()
    return personas


def Mantenimiento(u_id, u_nombre, u_apellidos,  u_cedula, u_telefono, u_correo, u_dirreccion, u_sexo, u_estado, u_contrasena,u_accion):
   try:
        cursor=conexion.cursor()
        consulta=f"PA_Mantenimiento_Usuarios @u_id='{u_id}',@u_nombre='{u_nombre}',@u_apellidos='{u_apellidos}',@u_cedula='{u_cedula}',@u_telefono='{u_telefono}',@u_correo='{u_correo}',@u_contrasena='{u_contrasena}',@u_dirreccion='{u_dirreccion}',@u_sexo='{u_sexo}',@u_estado='{u_estado}',@u_accion='{u_accion}'"
        #print (f"{consulta}")
        cursor.execute(consulta)
        cursor.commit()
        cursor.close()
        return 'true'
   except:
       return 'false'

#Getall()