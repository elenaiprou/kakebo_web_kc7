from kakebo import app
from flask import jsonify #crea un json con flask
import sqlite3


@app.route('/')
def index():
    conexion = sqlite3.connect("movimientos.db")
    cur = conexion.cursor()

    cur.execute("SELECT * FROM movimientos;") #importante poner el punto y coma(;)

    claves = cur.description
    #print('claves\n', claves)
    filas = cur.fetchall()
    #print('filas\n', filas)

    movimientos = []
    for fila in filas:
        d = {}
        for tclave, valor in zip(claves, fila): #zip sirve para enfrentar listas y crear una nueva (lista, tupla o diccionario)
            d[tclave[0]] = valor
        movimientos.append(d)

    conexion.close()

    return jsonify(movimientos) #imprime en oden alfabético