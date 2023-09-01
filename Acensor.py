print("***********************************************************************************************************************")
print("****************************************              Acensor                ******************************************")
print("***********************************************************************************************************************")

entrada_usuario = input("Ingrese los datos: ")
try:
    entrada_usuario=float(entrada_usuario)
    print("Input "+ str(entrada_usuario))
    print("Output: "+ str(entrada_usuario))
except:
    lista_numeros = eval("[" + entrada_usuario + "]")
    #lista_numeros=[[1.1],[2]]
    resultado=0
    valor=0
    valor2=len(lista_numeros)
    while valor<valor2:
        resultado=resultado+int(lista_numeros[valor][0])
        valor=valor+1
    print("Input "+ str(resultado))
    print("Output: "+ str(resultado))