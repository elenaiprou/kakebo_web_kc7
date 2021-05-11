from flask import Flask #importamos la clase Flask

app = Flask(__name__) #crea una instancia de Flask. Flask es la clase que es la aplicación

@app.route('/') #decorador: dentro fask hay metodo route que rodea la funcion de cosas. Asocia el contenido a la ruta del servidor web 
def index():
    return 'Hola, mundo!'

@app.route('/adios')
def bye():
    return 'Hsta luego, cocodrilo'

#crearemos variable de entorno para poder lanzar la web con los saludos. 
    #set FLASK_APP=hello.py
    #flask run