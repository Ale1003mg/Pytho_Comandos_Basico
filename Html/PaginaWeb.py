import cgi

header="Content-type: text/html\n\n"

# Define el cuerpo de la página HTML
body = """
<!DOCTYPE html>
<html>
<head>
    <title>Mi Página HTML generada con Python</title>
</head>
<body>
    <h1>Hola, mundo!</h1>
    <p>Esta página fue generada con Python.</p>
</body>
</html>
"""

# Imprime la cabecera y el cuerpo de la página
print(header + body)


#python PaginaWeb.py > PaginaWeb.html para covertirlo en html