from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola mundo! ruta raiz'

@app.route('/hola')
def hola():
    return 'Hola mundo! ruta /hola'

@app.route('/user/<string:user>')
def user(user):
    return f"Hola {user}"

@app.route('/numero/<int:numero>')
def numero(numero):
    return 'Numero: {}'.format(numero)

@app.route('/user/<string:user>/<int:id>')
def user_id(user, id):
    return f'Usuario: {user}, ID: {id}'

@app.route('/suma/<float:num1>/<float:num2>')
def suma(num1, num2):
    return 'La suma es {}'.format(num1 + num2)

@app.route('/default')
@app.route('/default/<string:nom>')
def func(nom='Sergio'):
    return 'Hola {}'.format(nom)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
