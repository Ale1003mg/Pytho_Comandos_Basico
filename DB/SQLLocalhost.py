
import pyodbc

server='localhost,14333'
db='BD_Pruebas_Microservicios'
soporte='sa'
contrasena='AdminServer1234'

#Data Source=.;Initial Catalog=BD_Pruebas_Microservicios;Integrated Security=True
try:
   # Conexion:pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+db+';UID='+Usuario+';PWD='+pwd)
    #Conexion:pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER=.;DATABASE=BD_Pruebas_Microservicios;Trusted_Connection=yes')
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


Getall()