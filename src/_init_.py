from flask import Flask, render_template

app = Flask(__name__)
app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Promocion 2024')
def captura():
     return render_template('promocion 2024.html')

@app.route('/vehiculos')
def inventario():
     return render_template('vehiculos.html')
   


if __name__ == '__main__':
    app.run(debug=True)
