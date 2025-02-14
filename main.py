from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    grupo = "IDGS803"
    lista = ['Sergio','Esteban','Erick','Juan']
    return render_template('index.html',grupo = grupo, lista = lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route("/ejemplo2")
def ejemplo2():
    return render_template('ejemplo2.html') 

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

@app.route('/OperasBas')
def OperasBas():
    return render_template('OperasBas.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacion = request.form['operacion']
    
    resultado = 0
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        resultado = num1 / num2
    
    return render_template('OperasBas.html', resultado=resultado)

def calcular_descuento(cantidad_boletas):
    if cantidad_boletas > 5:
        return 0.15  
    elif 3 <= cantidad_boletas <= 5:
        return 0.10  
    else:
        return 0 

@app.route('/cine', methods=['GET', 'POST'])
def cine():
    valor_a_pagar = None
    nombre = None
    cantidad_boletas = None
    error = None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        cantidad_compradores = int(request.form.get('cantidadCompradores', 0))
        tarjeta_cineco = request.form.get('tarjetaCineco') == 'tarjetaCineco'
        cantidad_boletas = int(request.form.get('cantidadBoletas', 0))
        
        max_boletos_permitidos = cantidad_compradores * 7
        if cantidad_boletas > max_boletos_permitidos:
            error = f'Máximo {max_boletos_permitidos} boletas permitidas para {cantidad_compradores} compradores'
        else:
            precio_base = 12.00* cantidad_boletas
            descuento_cantidad = calcular_descuento(cantidad_boletas)
            precio_con_descuento = precio_base * (1 - descuento_cantidad)
            
            if tarjeta_cineco:
                precio_final = precio_con_descuento * 0.90
            else:
                precio_final = precio_con_descuento
                
            valor_a_pagar = round(precio_final)
    
    return render_template('cine.html', 
                         valor_a_pagar=valor_a_pagar,
                         nombre=nombre,
                         cantidad_boletas=cantidad_boletas,
                         error=error)

@app.route("/form1")
def form1():
    return '''
    <form>
        <label>Nombre:</label>
        <input type="text" name="nombre" placeholder="Nombre">
        <br>
        <label>Apellido:</label>
        <input type="text" name="apellido" placeholder="Apellido">
        <br>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=3000)