from Dto import Dto_Usuario
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
    for per in personas:
        print(per)
    cursor.close()
    return personas