class Receta:

    def __init__ (self, autor, titulo, resumen, ingredientes, procedimiento, tiempo, imagen):
        self.autor = autor
        self.titulo = titulo
        self.resumen = resumen
        self.ingredientes = ingredientes
        self.procedimiento = procedimiento
        self.tiempo = tiempo
        self.imagen = imagen

    def obtenerRecetaComoListado(self):
        listadoRecetas = {}
        listadoRecetas["autor"] = self.autor
        listadoRecetas["titulo"] = self.titulo
        listadoRecetas["resumen"] = self.resumen
        listadoRecetas["ingredientes"] = self.ingredientes
        listadoRecetas["procedimiento"] = self.procedimiento
        listadoRecetas["tiempo"] = self.tiempo   
        listadoRecetas["imagen"] = self.imagen     
        return listadoRecetas 

class ControlDeRecetas:

    recetas = []
    
    #TODO BORRAR A LA RECONTRA VRGA

    r1 = Receta("Autor1","Titulo1","Res1","1ingr1,1ingr2","proced1","tiempo1","imagen1")
    r2 = Receta("Autor2","Titulo2","Res2","2ingr1,2ingr2","proced2","tiempo2","imagen2")
    r3 = Receta("Autor3","Titulo3","Res3","3ingr1,3ingr2","proced3","tiempo3","imagen3")

    recetas.append(r1)
    recetas.append(r2)
    recetas.append(r3)

    #YA NO BORRAR A LA RECONTRA VRGA

    def agregarRecetas(receta):
        ControlDeRecetas.recetas.append(receta)

    def removerReceta(titulo):
        for receta in RecetasHandler.recetas:
            if (receta.titulo == titulo):
                ControlDeRecetas.recetas.remove(receta)

    def buscarReceta(PalabraClave):
        recetasEncontradas = [] 
        for receta in ControlDeRecetas.recetas:
            if (PalabraClave in receta.titulo):
                recetasEncontradas.append(receta)
        return recetasEncontradas


    def obtenerRecetaPorTitulo(titulo):
        for receta in ControlDeRecetas.recetas:
            if (receta.titulo == titulo):
                return ControlDeRecetas.receta

    def obtenerRecetasComoListado(recetas):
        listado = {}
        i = 0
        for receta in recetas:
            listado[i] = receta.obtenerRecetaComoListado()
            i = i + 1
        return listado


###########################################################################################

