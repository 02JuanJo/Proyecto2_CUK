# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

from recetas import *
from usuario import *
import json

app = Flask(__name__)
CORS(app)

usuarioLogeado = "No hay"

##############################################BUSCAR RECETA############################################################

@app.route('/buscarReceta/', methods=['POST'])
def buscarReceta():
    datos = json.loads(request.data)

    titulo = datos['titulo']
    print(titulo)

    if not titulo:
        return jsonify({
            "Message": "Los datos ingresados son inválidos",
            "METHOD" : "POST"
        })
    else:
        palabraClave = titulo.lower()
        print(palabraClave)
        recetaEncontradas = ControlDeRecetas.buscadorReceta(palabraClave)
        print("En buscar recetaaaaaa")
        print(recetaEncontradas)
        if recetaEncontradas == None:
            return jsonify({
                "Message": "No se han encontrado recetas con esos datos.",
                "METHOD" : "POST",
                "Tipo" : "No encontrado"
            })
        else:
            return jsonify({
                "Message": "Se encontraron unas recetas",
                "METHOD" : "POST",
                "Tipo" : "Encontrado",
                "Listado": recetaEncontradas
            })

##############################################AGREGAR COMENTARIO##########################################################
@app.route('/agregarComentario/', methods=['POST'])
def agregarComentario():

    datos = json.loads(request.data)

    recetaAutor = datos['recetaAutor']
    recetaTitulo = datos['recetaTitulo']
    autorComentario = datos['autorComentario']
    contenido = datos['contenido']

    now = datetime.now()
    fecha = now.strftime("a las %H:%M:%S el %d-%m")

    receta = ControlDeRecetas.buscarReceta(recetaTitulo,recetaAutor)

    if receta != None:
        ControlDeRecetas.agregarComentario(receta, autorComentario,contenido,fecha)

        return jsonify({
            "Message": "Se está procesando la información..",
            "METHOD" : "POST",
            "Tipo" : "Listo",
            "Datos" : fecha
        })
    else:
        return jsonify({
            "Message": "La receta no existe.",
            "METHOD" : "POST",
            "Tipo" : "No Listo"

        })  
    

##############################################ENCONTRAR RECETA############################################################

@app.route('/encontrarReceta/', methods=['POST'])
def encontrarReceta():
    datos = json.loads(request.data)

    titulo = datos['titulo']
    autor = datos['autor']
    
    print(titulo)
    print(autor)

    #response = {}

    if not titulo or not autor:
        return jsonify({
            "Message": "Los datos ingresados son inválidos",
            "METHOD" : "POST"
        })
    else:
        recetaEncontrada = ControlDeRecetas.obtenerRecetaPorTitulo(titulo, autor)

        if recetaEncontrada == None:
            return jsonify({
                "Message": f"No se han encontrado recetas con esos datos.",
                "METHOD" : "POST",
                "Tipo" : "No encontrado"
            })
        else:
            return jsonify({
                "Message": "Receta a modificar Encontrada",
                "METHOD" : "POST",
                "Tipo" : "Encontrado",
                "Datos" : recetaEncontrada
            })

    #response = jsonify(response)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    #return response

##############################################MODIFICAR RECETA############################################################
@app.route('/modificarReceta/', methods=['POST'])
def modificacionRec():
    datos = json.loads(request.data)

    tituloPorModificar = datos['tituloPorModificar']
    autorPorModificar = datos['autorPorModificar']
    autor = datos['autor']
    titulo = datos['titulo']
    resumen = datos['resumen']
    ingredientes = datos['ingredientes']
    procedimiento = datos['procedimiento']
    tiempo = datos['tiempo']
    imagen = datos['imagen']

    #estadoModificarReceta = ControlDeRecetas.verificacionRecetaExistente(tituloPorModificar)

    ControlDeRecetas.modificarReceta(tituloPorModificar, autorPorModificar, autor, titulo, resumen, ingredientes, procedimiento, tiempo, imagen)

    return jsonify({
        "Message": "Modificado con exito.",
        "METHOD" : "POST",
        "Tipo" : "Modificado"
    })

##############################################AGREGAR RECETA############################################################
@app.route('/agregarReceta/', methods=['POST'])
def agregarReceta():

    datos = json.loads(request.data)

    #id_receta = datos['id']
    autor = datos['autor']
    titulo = datos['titulo']
    resumen = datos['resumen']
    ingredientes = datos['ingredientes']
    procedimiento = datos['procedimiento']
    tiempo = datos['tiempo']
    imagen = datos['imagen']
    reacciones = []
    comentarios = []

    print(datos)

    #MODIFICAR QUE TODOS LOS TITULOS SI SON ACEPTADOS Y REPETIDOS 
    estadoRegistro = ControlDeRecetas.verificacionRecetaExistente(titulo)

    if estadoRegistro == "No Existe":
        ControlDeRecetas.agregarRecetas(Receta(autor, titulo, resumen, ingredientes, procedimiento, tiempo, imagen, reacciones, comentarios))   
        
        return jsonify({
            "Message": f"Se ha registrado la Receta {titulo}, escrita por {autor}, correctamente",
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "Message": "Este título ya está registrado previamente para tu receta.",
            "METHOD" : "POST"
        })

##############################################PUBLICAR RECETAS############################################################
@app.route('/eliminarRecetas/', methods=['POST'])
def eliminarRecetas():

    datos = json.loads(request.data)

    titulo = datos['titulo']
    autor = datos['autor']
    
    print(titulo)
    print(autor)

    recetaEncontrada = ControlDeRecetas.obtenerRecetaPorTitulo(titulo, autor)

    if recetaEncontrada == None:
        return jsonify({
            "Message": "No se han encontrado recetas con esos datos.",
            "METHOD" : "POST"
        })
    else:
        ControlDeRecetas.removerReceta(titulo, autor)
        return jsonify({
            "Message": "Eliminado",
            "METHOD" : "POST"
        })

##############################################PUBLICAR RECETAS############################################################
@app.route('/publicarRecetas/', methods=['POST'])
def publicarRecetas():

        return jsonify({
            "Listado": ControlDeRecetas.obtenerRecetasComoListado(),
            "METHOD" : "POST"
        })

##############################################PUBLICAR RECETAS############################################################
@app.route('/usuariosRegistrados/', methods=['POST'])
def usuariosRegistrados():

        return jsonify({
            "Listado": ControlDeUsuarios.obtenerUsuariosComoListado(),
            "METHOD" : "POST"
        })



#USUARIOSS
###############################################################################################################

@app.route('/login/', methods=['POST'])
def login():

    datos = json.loads(request.data)
    print(datos)

    nombreUsuario = datos['nombreUsuario']
    psw = datos['psw']
    

    print(datos)

    if nombreUsuario and psw:
        estadoLogin = ControlDeUsuarios.inicioSesion(nombreUsuario, psw)
        if estadoLogin == "admitido":
            global usuarioLogeado 
            usuarioLogeado = nombreUsuario
            print(usuarioLogeado)
            return jsonify({
                "Message": f"Bienvenido! {nombreUsuario}",
                "METHOD" : "POST",
                "Tipo" : "Admitido"
                
            })
        elif estadoLogin == "psw No Valida":
            return jsonify({
                "Message": "Las credenciales son incorrectas.",
                "METHOD" : "POST",
                "Tipo" : "No admitido, error 1"
            })
        else:
            return jsonify({
                "Message": "El usuario no existe.",
                "METHOD" : "POST",
                "Tipo" : "No admitido, error 2"
            })
    else:
        return jsonify({
            "Message": "No ha brindado todos los datos suficientes para Iniciar Sesión.",
            "METHOD" : "POST",
            "Tipo" : "No admitido, error 3"
        })

##############################################SESION INICIADA###########################################################
@app.route('/sesionIniciada/', methods=['POST'])
def sesionIniciada():

    elUsuario = ""
    print("segunda vez")
    print(usuarioLogeado)
    if usuarioLogeado != None:
        elUsuario = usuarioLogeado
        print("el usuario")
        print(elUsuario)

    return jsonify({
        "usuario": elUsuario,
        "METHOD" : "POST",
        "Datos" : ControlDeUsuarios.obtenerUsuarioComoLista(elUsuario)
    })

    ##############################################SESION TERMINADA###########################################################
@app.route('/sesionTerminada/', methods=['POST'])
def sesionTerminada():

    global usuarioLogeado
    usuarioLogeado = "No hay"

    if usuarioLogeado != "No hay":
        elUsuario = usuarioLogeado

    return jsonify({
        "usuario": elUsuario,
        "METHOD" : "POST",
    })

############################################ REGISTRARSE ##################################################################
@app.route('/registrarse/', methods=['POST'])
def registrarse():

    datos = json.loads(request.data)

    nombre = datos['nombre']
    apellido = datos['apellido']
    nombreUsuario = datos['nombreUsuario']
    psw = datos['psw']
    tipo = datos['tipo']

    print(datos)

    estructura = ControlDeUsuarios.esValido(nombreUsuario)

    estadoRegistro = ControlDeUsuarios.verificacionUsuarioExistente(nombreUsuario)

    if estructura :

        if estadoRegistro == "No Existe":
            ControlDeUsuarios.agregarUsuario(Usuario(nombre, apellido, nombreUsuario, psw, tipo))
            
            return jsonify({
                "Message": f"Se ha registrado {nombreUsuario}  correctamente, Bienvenido! ",
                "METHOD" : "POST",
                "Tipo" : "Admitido"
            })
        else:
            return jsonify({
                "Message": "Este usuario ya está registrado.",
                "METHOD" : "POST",
                "Tipo" : "No Admitido"
            })

    else:
        return jsonify({
            "Message": "El usuario debe iniciar con una letra.",
            "METHOD" : "POST",
            "Tipo" : "Letra Inicial"
        })



############################################ LOST PSW ##################################################################
@app.route('/lostpsw/', methods=['POST'])
def lostpsw():

    datos = json.loads(request.data)

    nombreUsuario = datos['nombreUsuario']
    print(datos)  
    print("Datos ingresados ahoritititita")  

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


######################################### MODIFICAR USUARIO ##################################################################
@app.route('/modificarUsuario/', methods=['POST'])
def modificacionUsu():
    datos = json.loads(request.data)

    nombreUsuarioPorModificar = datos['nombreUsuarioPorModificar']
    nombre = datos['nombre']
    apellido = datos['apellido']
    nombreUsuario = datos['nombreUsuario']
    psw = datos['psw']

    estructura = ControlDeUsuarios.esValido(nombreUsuario)

    estadoRegistro = ControlDeUsuarios.verificacionUsuarioExistente(nombreUsuarioPorModificar)



    if estructura : 

        if nombreUsuarioPorModificar == nombreUsuario:

            if estadoRegistro == "Existe":

                ControlDeUsuarios.modificarUsuario(nombre, apellido, nombreUsuario, psw, nombreUsuarioPorModificar)

                return jsonify({
                    "Message": "Modificado con exito.",
                    "METHOD" : "POST",
                    "Tipo" : "Modificado"
                })
            else:
                return jsonify({
                    "Message": "El usuario no existe, no se puede completar esta acción.",
                    "METHOD" : "POST",
                    "Tipo" : "Sin Usuario"
                })
        
        else:

            estadoUsuarioNuevo = ControlDeUsuarios.verificacionUsuarioExistente(nombreUsuario)
            
            if estadoUsuarioNuevo == "No Existe":

                ControlDeUsuarios.modificarUsuario(nombre, apellido, nombreUsuario, psw, nombreUsuarioPorModificar)

                return jsonify({
                    "Message": "Modificado con exito.",
                    "METHOD" : "POST",
                    "Tipo" : "Modificado"
                })
            else:
                return jsonify({
                    "Message": "El usuario ya está registrado, no se puede completar esta acción.",
                    "METHOD" : "POST",
                    "Tipo" : "No Modificado"
                })

    else:
        return jsonify({
            "Message": "El usuario debe iniciar con una letra.",
            "METHOD" : "POST",
            "Tipo" : "Letra Inicial"
        })
     
############################################ Modificar Admin ##################################################################

@app.route('/encontrarUsuario/', methods=['POST'])
def encontrarUsu():
    datos = json.loads(request.data)

    usuario = datos['usuario']

    estructura = ControlDeUsuarios.esValido(usuario)

    estadoExistente = ControlDeUsuarios.verificacionUsuarioExistente(usuario)

    if estructura :

        if estadoExistente == "Existe":
            return jsonify({
                "Message": f"Se encontró al usuario {usuario}",
                "METHOD" : "POST",
                "Tipo" : "Encontrado",
                "Datos" : ControlDeUsuarios.obtenerUsuarioComoLista(usuario)
            })
            
        else:
            return jsonify({
                "Message": "El usuario no existe, no se puede completar esta acción.",
                "METHOD" : "POST",
                "Tipo" : "No encontrado"
            })

    else:
        return jsonify({
            "Message": "El usuario debe iniciar con una letra.",
            "METHOD" : "POST",
            "Tipo" : "Letra Inicial"
        })



############################################ Registrar Usuario Admin #########################################

@app.route('/registrarUsuario/', methods=['POST'])
def registrarUsuario():

    datos = json.loads(request.data)

    nombre = datos['nombre']
    apellido = datos['apellido']
    nombreUsuario = datos['nombreUsuario']
    psw = datos['psw']
    tipo = datos['tipo']

    print(datos)

    estructura = ControlDeUsuarios.esValido(nombreUsuario)

    estadoRegistro = ControlDeUsuarios.verificacionUsuarioExistente(nombreUsuario)

    if estructura :

        if estadoRegistro == "No Existe":
            ControlDeUsuarios.agregarUsuario(Usuario(nombre, apellido, nombreUsuario, psw, tipo))
            
            return jsonify({
                "Message": f"Se ha registrado {nombreUsuario}  correctamente, Bienvenido! ",
                "METHOD" : "POST",
                "Tipo" : "Admitido"
            })
        else:
            return jsonify({
                "Message": "Este usuario ya está registrado.",
                "METHOD" : "POST",
                "Tipo" : "No Admitido"
            })

    else:
        return jsonify({
            "Message": "El usuario debe iniciar con una letra.",
            "METHOD" : "POST",
            "Tipo" : "Letra Inicial"
        })


############################################ PRINCIPAL ##################################################################

@app.route('/')

def index():

    return jsonify({
                "Message":"BACKEND PROYECTO CUK",
                "METHOD" : "POST"
            })

if __name__ == '__main__':

    app.run(threaded=True, port=5000)
