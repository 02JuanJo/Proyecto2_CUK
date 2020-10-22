class Usuario:

    def __init__ (self, nombre, apellido, nombreUsuario, psw):
        self.nombre = nombre
        self.apellido = apellido
        self.nombreUsuario = nombreUsuario
        self.psw = psw


    def obtenerUsuarioComoListado(self):
        listadoUsuarios = {}
        listadoUsuarios["nombre"] = self.nombre
        listadoUsuarios["apellido"] = self.apellido
        listadoUsuarios["usuario"] = self.nombreUsuario
        listadoUsuarios["psw"] = self.psw  
        return listadoUsuarios 

class ControlDeUsuarios:

    usuarios = []
    

    UsuarioMaestro = Usuario("Usuario","Maestro","admin","admin")
    r2 = Usuario("Matusaurio","Puto amo","123","456")

    usuarios.append(r2)
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


    def modificarUsuario(nuevonombre, nuevoapellido, nuevousuario, nuevapsw, usuarioPorModificar):
        for usuario in ControlDeUsuarios.usuarios:
            if(usuario.nombreUsuario == usuarioPorModificar):

                if(nuevonombre != None):
                    usuario.nombreUsuario == nuevonombre

                if(nuevoapellido != None):
                    usuario.apellido == nuevoapellido

                if(nuevousuario != None):
                    usuario.nombreUsuario == nuevousuario

                if(nuevapsw != None):
                    usuario.psw == nuevapsw

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
      