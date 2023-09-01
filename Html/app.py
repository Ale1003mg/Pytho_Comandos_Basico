from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Aquí puedes generar contenido dinámico para tu página HTML si es necesario
    # Por ahora, simplemente renderizaremos una página HTML estática
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
