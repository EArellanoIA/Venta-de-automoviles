from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app = Flask(__name__,template_folder='templates')


db_config = {
    'host': 'localhost',  
    'user': 'root',
    'password': '',
    'database': 'ventas', 
}

conn = mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
     return render_template('contacto.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    direccion = request.form['direccion']

    cursor = conn.cursor()
    cursor.execute('INSERT INTO cliente (nombre, apellido, telefono, direccion ) VALUES (%s, %s, %s,%s )', (nombre, apellido, telefono, direccion ))
    conn.commit()

    cursor.close()
    
    return redirect(url_for('contacto'))


@app.route('/promocion')
def promocion():
     return render_template('promocion.html')

@app.route('/vehiculos')
def vehiculos():
     return render_template('vehiculos.html')


if __name__ == '__main__':
    app.run(debug=True)

