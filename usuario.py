class Usuario:

    def __init__ (self, nombre, apellido, nombreUsuario, psw, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.nombreUsuario = nombreUsuario
        self.psw = psw
        self.tipo = tipo


    def obtenerUsuarioComoListado(self):
        listadoUsuarios = {}
        listadoUsuarios["nombre"] = self.nombre
        listadoUsuarios["apellido"] = self.apellido
        listadoUsuarios["usuario"] = self.nombreUsuario
        listadoUsuarios["psw"] = self.psw 
        listadoUsuarios["tipo"] = self.tipo 
        return listadoUsuarios 

class ControlDeUsuarios:

    usuarios = []
    

    UsuarioMaestro = Usuario("Usuario","Maestro","admin","admin","Administrador")
    r2 = Usuario("uwu","uwu","zz","zz","Cliente")
    r3 = Usuario("J","L","aaa","777","Cliente")

    usuarios.append(r2)
    usuarios.append(r3)
    usuarios.append(UsuarioMaestro)



    def agregarUsuario(usuarioNuevo):
        for usuario in ControlDeUsuarios.usuarios:
            if(usuario.nombreUsuario == usuarioNuevo.nombreUsuario):
                return False
        ControlDeUsuarios.usuarios.append(usuarioNuevo)
        return True

    def removerUsuario(nombreUsuario):
        for usuario in ControlDeUsuarios.usuarios:
            if(usuario.nombreUsuario == nombreUsuario):
                ControlDeUsuarios.usuarios.remove(usuario)
                return


    def modificarUsuario(nuevonombre, nuevoapellido, nuevousuario, nuevapsw, nombreUsuarioPorModificar):
        for usuario in ControlDeUsuarios.usuarios:
            if(usuario.nombreUsuario == nombreUsuarioPorModificar):
                usuario.nombre = nuevonombre
                usuario.apellido = nuevoapellido
                usuario.nombreUsuario = nuevousuario
                usuario.psw = nuevapsw
                return
        


    def inicioSesion(nombreUsuario,psw):
        for usuario in ControlDeUsuarios.usuarios:
            if(usuario.nombreUsuario == nombreUsuario):
                if(usuario.psw == psw):
                    UsuarioAdmitido = usuario
                    return "admitido"
                else:
                    return "psw No Valida"
        return "no user"

    def verificacionUsuarioExistente(nombreUsuario):
        for usuario in ControlDeUsuarios.usuarios:
            if(usuario.nombreUsuario == nombreUsuario):
                return "Existe"                  
        return "No Existe"

    def lostpsw(nombreUsuario):
        for usuario in ControlDeUsuarios.usuarios:
            if(usuario.nombreUsuario == nombreUsuario):
                return usuario.psw    

    def obtenerUsuarioComoLista(nombreUsuario):
        for user in ControlDeUsuarios.usuarios:
            if(user.nombreUsuario == nombreUsuario):
                return {
                    "nombre" : user.nombre,
                    "apellido" : user.apellido,
                    "usuario" : user.nombreUsuario,
                    "psw" : user.psw,
                    "tipo" : user.tipo
                }
        return
        
    def obtenerDatosUsuario(nombreUsuario):
        for usuario in ControlDeUsuarios.usuarios:
            if(usuario.nombreUsuario == nombreUsuario):
                print(usuario.nombre)
                print(usuario.apellido)
                print(usuario.nombreUsuario)
                print(usuario.psw)
                return 

    def esValido(usuario):

        LetrasPosibles = ["y","z","a","b","c","d","e","f","g","h","i","j","k","l",
        "m","n","o","p","q","r","s","t","u","v","w","x"]
        stringUsuario = str(usuario)
        LetraInicial = stringUsuario[0].lower()

        for letra in LetrasPosibles:
            if(LetraInicial == letra):
                print("Si inicia con letras")
                return True
    
        print("No inicia con letras")
        return False

    def obtenerUsuariosComoListado():
        listado = {}
        i = 0
        for usuario in ControlDeUsuarios.usuarios:
            listado[i] = usuario.obtenerUsuarioComoListado()
            i = i + 1
        return listado
        