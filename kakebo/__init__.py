from flask import Flask

app = Flask(__name__, instance_relative_config= True) #cremos la aplicación. Flask clase por eso ha de ir en mayusculas. 
app.config.from_object('config')

from kakebo import views #seria lo mismo decir import kakebo.views

