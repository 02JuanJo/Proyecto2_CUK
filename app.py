# app.py
from flask import Flask, request, jsonify, render_template
from recetas import *
from usuario import *

app = Flask(__name__)

@app.route('/encontrarReceta/', methods=['GET'])
def receta():
    titulo = request.args.get("titulo", None)

    print(f"got name {titulo}")

    response = {}

    if not titulo:
        response["ERROR"] = "No ha ingreso un titulo de receta a buscar"
    else:
        recetasEncontradas = ControlDeRecetas.buscarReceta(titulo)

        if len(recetasEncontradas) == 0:
            response["MESSAGE"] = "No se encontraror recetas con ese nombre"
        else:
            comoListado = ControlDeRecetas.obtenerRecetasComoListado(recetasEncontradas)
            print(jsonify(comoListado))
            response["MESSAGE"] = comoListado

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/modificarReceta/', methods=['GET'])
def modificarReceta():
    titulo = request.args.get("titulo", None)

    print(f"got name {titulo}")

    response = {}

    if not titulo:
        response["ERROR"] = "No ha ingreso un titulo de receta a buscar"
    else:
        recetasEncontradas = ControlDeRecetas.buscarReceta(titulo)

        if len(recetasEncontradas) == 0:
            response["MESSAGE"] = "No se encontraror recetas con ese nombre"
        else:
            comoListado = ControlDeRecetas.obtenerRecetasComoListado(recetasEncontradas)
            print(jsonify(comoListado))
            response["MESSAGE"] = comoListado

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


###############################################################################################################
@app.route('/post/', methods=['POST'])
def post_something():
    parametro = request.form.get('Juanito')
    print(param)

    if param:
        return jsonify({
            "Message": f"El usuario leído es {parametro} , Bienvenido!",
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "No funciona :c"
        })

@app.route('/login/', methods=['POST'])
def login():
    nombreUsuario = request.args.get('nombreUsuario')
    psw = request.args.get('psw')
    print(nombreUsuario)    
    print(psw)

    if nombreUsuario and psw:
        estadoLogin = ControlDeUsuarios.inicioSesion(nombreUsuario, psw)
        if estadoLogin == "admitido":
            return jsonify({
                "Message": f"Se ha iniciado sesión con el usuario: {nombreUsuario} , Bienvenido!",
                "METHOD" : "POST"
            })
        elif estadoLogin == "psw No Valida":
            return jsonify({
                "Message": "Las credenciales son incorrectas.",
                "METHOD" : "POST"
            })
        else:
            return jsonify({
                "Message": "El usuario no existe.",
                "METHOD" : "POST"
            })
    else:
        return jsonify({
            "Message": "No ha brindado todos los datos",
            "METHOD" : "POST"
        })

@app.route('/registrarse/', methods=['POST'])
def registrarse():
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    nombreUsuario = request.args.get('nombreUsuario')
    psw = request.args.get('psw')
    print(nombre)
    print(apellido)
    print(nombreUsuario)    
    print(psw)

    estadoRegistro = ControlDeUsuarios.verificacionUsuarioExistente(nombreUsuario)

    if estadoRegistro == "No Existe":
        ControlDeUsuarios.agregarUsuario(Usuario(nombre, apellido, nombreUsuario, psw))
        return jsonify({
            "Message": f"Se ha registrado {nombreUsuario}  correctamente, Bienvenido!",
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "Message": "Este usuario ya está registrado.",
            "METHOD" : "POST"
        })

@app.route('/lostpsw/', methods=['POST'])
def lostpsw():
    nombreUsuario = request.args.get('nombreUsuario')
    print(nombreUsuario)    

    estadoLostpsw = ControlDeUsuarios.verificacionUsuarioExistente(nombreUsuario)

    if estadoLostpsw == "Existe":
        pswRecuperar = ControlDeUsuarios.lostpsw(nombreUsuario)
        return jsonify({
            "Message": f"La contraseña del Usuario: {nombreUsuario}  es {pswRecuperar}, Recuperado exitosamente!",
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "Message": "El usuario no existe, no se puede realizar esta acción.",
            "METHOD" : "POST"
        })


@app.route('/modificarUsuario/', methods=['POST'])
def modificacion():

    nombreUsuarioPorModificar = request.args.get('nombreUsuarioPorModificar')
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    nombreUsuarioNuevo = request.args.get('nombreUsuarioNuevo')
    psw = request.args.get('psw')
    print(nombreUsuarioPorModificar)
    print(nombre) 
    print(apellido)
    print(nombreUsuarioNuevo)
    print(psw)

    estadoModificarUsuario = ControlDeUsuarios.verificacionUsuarioExistente(nombreUsuarioPorModificar)

    if estadoModificarUsuario == "Existe":

        estadoUsuarioNuevo = ControlDeUsuarios.verificacionUsuarioExistente(nombreUsuarioNuevo)
        
        if estadoUsuarioNuevo == "No Existe":

            ControlDeUsuarios.modificarUsuario(nombre, apellido, nombreUsuarioNuevo, psw, nombreUsuarioPorModificar)
            return jsonify({
                "Message": "Modificado con exito.",
                "METHOD" : "POST"
            })
        else:
            return jsonify({
                "Message": "El usuario ya está registrado, no se puede completar esta acción.",
                "METHOD" : "POST"
            })
     
    else:
        return jsonify({
            "Message": "El usuario no existe, no se puede completar esta acción.",
            "METHOD" : "POST"
        })
     

@app.route('/')

def index():
    return "OLA K ASE"

if __name__ == '__main__':

    app.run(threaded=True, port=5000)
