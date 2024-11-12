from flask import Flask

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return '          Creacion simple'

# Iniciar el servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
