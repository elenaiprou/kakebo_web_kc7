from flask import Flask

app = Flask(__name__) #cremos la aplicación. Flask clase por eso ha de ir en mayusculas. 

from kakebo import views #seria lo mismo decir import kakebo.views

