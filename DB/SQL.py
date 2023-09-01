import pyodbc
#se tiene que instalar pyodbc para que ejecute los comandos 
   
server='localhost,14333'
db='PruebasConfi'
soporte='sa'
contrasena='AdminServer1234'

try:
    conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+db+';UID='+soporte+';PWD='+contrasena)
    print("Conexion exitosa")
except :
    print("Error al intentar conectarse")



#Consultar select
def Getall():
    cursor= conexion.cursor()
    #cursor.execute("select * from Getall_Usuario();")
    cursor.execute("select * from Usuarios_Prueba;")
    #cosnulta linea por linea
    #persona=cursor.fetchone()
    #while persona:
    #    print(persona)
    #    persona:cursor.fetchone()
    personas= cursor.fetchall()
    for per in personas:
        print(per)
        #print(per[1])
    cursor.close()



#Insertar datos
def insertar():
    Cursorinsert= conexion.cursor()
    cunsulta = "insert into Usuarios_Prueba (U_Nombre,U_Apellidos,U_Telefono,U_Direccion,U_Contrasena,U_Estado,Correo) values (?,?,?,?,?,?,?)"
    Cursorinsert.execute(cunsulta,'Natalia2','Mendez','25588555','prueba1','prueba',1,'prueba@prueba1.com')
    Cursorinsert.execute(cunsulta,'Natalia3','Mendez','25588555','prueba2','prueba',1,'prueba@prueba2.com')
    Cursorinsert.execute(cunsulta,'Natalia4','Mendez','25588555','prueba3','prueba',1,'prueba@prueba3.com')
    Cursorinsert.commit()
    Cursorinsert.close()
    Getall()

#Update
def update():
    cursoupdate=conexion.cursor()
    consulta=" update Usuarios_Prueba set   U_Nombre=?  where U_ID=?"
    cursoupdate.execute(consulta,'Katty2',51)
    cursoupdate.commit()
    cursoupdate.close()
    Getall()

#Delete
def Delete():
    CursosEliminar=conexion.cursor()
    consulta="delete Usuarios_Prueba where U_ID=? "
    CursosEliminar.execute(consulta,51)
    CursosEliminar.commit()
    CursosEliminar.close()
    Getall()
#conexion.close()
Getall()
#insertar()
#update()
#Delete()