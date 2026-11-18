class Anuncio:
    def __init__(self, num=0, pre=0.1):
        self.__numero =num
        self.__precio= pre
    def getPrecio(self):
        return self.__precio
    
class Artista:
    def __init__(self, nom, car, anios):
        self.__nombre=nom
        self.__ci =car
        self.__aniosExp= anios
    def getNombre(self):
        return self.__nombre
    def getAnios(self):
        return self.__aniosExp

class Obra:
    def __init__(self, titulo, material, nom1, car1, anio1, nom2, car2, anio2):
        self.__titulo = titulo 
        self.__material= material
        self.__artista1 =Artista(nom1, car1, anio1)
        self.__artista2 =Artista(nom2, car2, anio2)
        self.__anuncio=None
    def agregarAnuncio(self, anun):
        self.__anuncio =anun
    def getArt1(self):
        return self.__artista1
    def getArt2(self):
        return self.__artista2
    def getAnuncio(self):
        return self.__anuncio

class Pintura(Obra):
    def __init__(self, titulo:str, material:str, nom1, car1, anio1, nom2, car2, anio2, gen):
        super().__init__(titulo, material, nom1, car1, anio1, nom2, car2, anio2)
        self.__genero=gen

if __name__ == "__main__":
    a1 = Anuncio(1, 150.0)   
    p1 = Pintura("Paisaje", "Oleo", "Juan", 123, 5, "Pedro", 321, 2, "Realismo")
    p2 = Pintura("Retrato", "Oleo", "Lizeth", 456, 15, "Ana", 654, 8, "Abstracto")   
    p2.agregarAnuncio(a1)
    artistas =[p1.getArt1(), p1.getArt2(), p2.getArt1(), p2.getArt2()]
    max_exp =-1
    nom_max= ""
    for art in artistas:
        if art.getAnios() > max_exp:
            max_exp=art.getAnios()
            nom_max= art.getNombre()
    print(nom_max)
    a2 =Anuncio(2, 250.0)
    p1.agregarAnuncio(a2)
    total =p1.getAnuncio().getPrecio() + p2.getAnuncio().getPrecio()
    print(total)