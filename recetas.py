class Receta:

    def __init__ (self, autor, titulo, resumen, ingredientes, procedimiento, tiempo, imagen, comentarios, reacciones):
        #self.id_receta = id_receta
        self.autor = autor
        self.titulo = titulo
        self.resumen = resumen
        self.ingredientes = ingredientes
        self.procedimiento = procedimiento
        self.tiempo = tiempo
        self.imagen = imagen
        self.reacciones = reacciones
        self.comentarios = comentarios

    def obtenerRecetaComoListado(self):
        listadoRecetas = {}
        listadoRecetas["autor"] = self.autor
        listadoRecetas["titulo"] = self.titulo
        listadoRecetas["resumen"] = self.resumen
        listadoRecetas["ingredientes"] = self.ingredientes 
        listadoRecetas["procedimiento"] = self.procedimiento 
        listadoRecetas["tiempo"] = self.tiempo
        listadoRecetas["imagen"] = self.imagen
        listadoRecetas["reacciones"] = self.reacciones
        listadoRecetas["comentarios"] = self.comentarios
        return listadoRecetas 



class ControlDeRecetas:

    recetas = []
    
    #TODO BORRAR A LA RECONTRA VRGA

    receta1= Receta("Administrador","Lasaña","¿A quién no le gusta la lasaña? Este clásico plato de la cocina italiana hace las delicias de los más pequeños y triunfa entre los no tan pequeños. Es perfecto, además, para preparar en cantidades, congelar y llevar al trabajo o al cole. El relleno puede ser de casi cualquier cosa pero, nosotros, no hemos decantado por la clásica lasaña de carne. Una receta fácil y deliciosa para tomar en familia.",
    "0.75 l de Leche \n 40 g de Mantequilla\n40 g de Harina\n1 pizca de Nuez moscada molida\nSal","1.En una sartén, sofreír en un poco de aceite de oliva la cebolla y la zanahoria peladas y cortadas en dados bien pequeños.\n2.Pelar el tomate y cortarlo en dados pequeños. Añadirlo a la sartén. Salpimentar y dejar unos 20 minutos a fuego medio-bajo, hasta que esté en su punto.\n3.Incorporamos los champiñones laminados y los salteamos con la carne.","1 hora","https://th.bing.com/th/id/OIP.rSF_epgUbdjkLMui98fKNAHaE8?w=278&h=185&c=7&o=5&pid=1.7",[{"autor":"JJ","contenido":"Buena receta!","fecha":"a las 2:33:26 el 02-10"}],[])
    receta2= Receta("Administrador","Ensalada","¿A quién no le gusta la ensalada? Y si la ensalada César tiene fama mundial, la ensalada Waldorf no se queda atrás. Fácil y riquísima con el toque de la manzana o, como en este caso, de la pera. La receta completa podéis verla pinchando aquí,
    "1 lechuga \n 40 g de pimeinta\n40 g de sal\n1 pizca de Nuez moscada molida\nSal","1.Se deben cortar todos los ingredientes al gusto \n2.Condimenta al gusto con lo necesario en la cocina.\n3.Se agregan acompañamientos y a disfrutar","45 minutos","https://th.bing.com/th/id/OIP.chnEAkI4xogn108YLrpDegHaGF?pid=Api&rs=1",[{"autor":"Iván","contenido":"Niceee receta!","fecha":"a las 10:20:11 el 09-06"}],[])

    recetas.append(receta1)
    recetas.append(receta2)

    #YA NO BORRAR A LA RECONTRA VRGA

    def agregarRecetas(receta):
        ControlDeRecetas.recetas.append(receta)

    def removerReceta(titulo, autor):
        for receta in ControlDeRecetas.recetas:
            if (receta.titulo == titulo):
                if(receta.autor == autor):
                    ControlDeRecetas.recetas.remove(receta)

    def buscadorReceta(PalabraClave):
        recetasEncontradas = {} 
        i = 0
        for receta in ControlDeRecetas.recetas:
            if ((PalabraClave in receta.titulo.lower())or(PalabraClave == receta.titulo.lower())):
                recetasEncontradas[i] = receta.obtenerRecetaComoListado()
                print(recetasEncontradas)
                i = i + 1
        return recetasEncontradas
       


    def obtenerRecetaPorTitulo(titulo, autor):
        for receta in ControlDeRecetas.recetas:
            if (receta.titulo == titulo):
                if(receta.autor == autor):
                    return {
                        "autor" : receta.autor,
                        "titulo" : receta.titulo,
                        "resumen" : receta.resumen,
                        "ingredientes" : receta.ingredientes,
                        "procedimiento" : receta.procedimiento,
                        "tiempo" : receta.tiempo,
                        "imagen" : receta.imagen,
                        "reacciones" : receta.reacciones,
                        "comentarios" : receta.comentarios
                    }
        return None

    def buscarReceta(titulo, autor):
        for receta in ControlDeRecetas.recetas:
            if (receta.titulo == titulo):
                if(receta.autor == autor):
                    return receta
        return None

    


    def obtenerRecetasComoListado():
        listado = {}
        i = 0
        for receta in ControlDeRecetas.recetas:
            listado[i] = receta.obtenerRecetaComoListado()
            i = i + 1
        return listado

###########################################################################################
    def verificacionRecetaExistente(titulo):
        for receta in ControlDeRecetas.recetas:
            if(receta.titulo == titulo):
                return "Existe"                  
        return "No Existe"

    def modificarReceta(tituloPorModificar, autorPorModificar, autor, titulo, resumen, ingredientes, procedimiento, tiempo, imagen):
        for receta in ControlDeRecetas.recetas:
            if(receta.titulo == tituloPorModificar):
                if(receta.autor == autorPorModificar):
                    receta.autor = autor
                    receta.titulo = titulo
                    receta.resumen = resumen
                    receta.ingredientes = ingredientes
                    receta.procedimiento = procedimiento
                    receta.tiempo = tiempo
                    receta.imagen = imagen
                    return


    def agregarComentario(receta, autor, contenido, fecha):
      
        receta.comentarios.append({
            "autor":autor,
            "contenido":contenido,
            "fecha":fecha
        })
        