from flask.helpers import url_for
from kakebo import app
from flask import jsonify, render_template, request, redirect, flash
import sqlite3
from kakebo.forms import MovimientosForm #importar classe de movimientos de formulario para poder cargarlo

def consultaSQL(query, parametros = []):
    # Abrimos la conexion
    conexion = sqlite3.connect("movimientos.db")
    cur = conexion.cursor()
    # Ejecutamos la consulta
    cur.execute(query, parametros)
    # Obtenemos los datos de la consulta
    claves = cur.description
    filas = cur.fetchall()
    # Procesar los datos para devolver una lista de diccionarios. Un diccionario por fila
    resultado = []
    for fila in filas:
        d = {}
        for tclave, valor in zip(claves, fila):
            d[tclave[0]] = valor
        resultado.append(d)
    conexion.close()
    return resultado

def modificaTabletSQL(query, parametros= []):
    conexion = sqlite3.connect("movimientos.db")
    cur = conexion.cursor()

    cur.execute(query, parametros)

    conexion.commit()
    conexion.close()

@app.route('/')
def index():
    movimientos = consultaSQL("SELECT * FROM movimientos order by fecha;")
    saldo = 0
    for d in movimientos:
        if d['esGasto'] == 0:
            saldo = saldo + d['cantidad']
        else:
            saldo = saldo - d['cantidad']
        d['saldo'] = saldo
    return render_template('movimientos.html', datos = movimientos)


@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    formulario = MovimientosForm()
    
    if request.method == 'GET':
        return render_template('alta.html', form = formulario)
    else:
        if formulario.validate():
            query = "INSERT INTO movimientos (fecha, concepto, categoria, esGasto, cantidad) VALUES (?, ?, ?, ?, ?)"
            try:
                modificaTabletSQL(query, [formulario.fecha.data, formulario.concepto.data, formulario.categoria.data,
                                formulario.esGasto.data, formulario.cantidad.data])
            
            except sqlite3.Error as el_error:
                print("Error en SQL INSERT", el_error)
                flash("Se ha producido un error en la base de datos. Pruebe en unos minutos")
                return render_template('alta.html', form=formulario)

            return redirect(url_for("index"))
            
            #Redirect a la ruta /
        else:
            return render_template('alta.html', form = formulario)

@app.route('/borrar/<int:id>', methods = ['GET', 'POST'])
def borrar(id):
    filas = consultaSQL("SELEC * FROM movimientos WHERE id =?", [id])
    if len(filas) == 0:
        flash("El registro no existe")
        return render_template('borrar.html')
    
    return render_template('borrar.html', movimiento = filas[0])

