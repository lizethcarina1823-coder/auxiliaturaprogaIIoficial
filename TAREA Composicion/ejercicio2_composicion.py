class Pantalla:
    def __init__(self,tipo,alto,ancho):
        self._tipo=tipo
        self._alto=alto
        self._ancho=ancho
    def get_ancho(self):
        return self._ancho
    def __str__(self):
        return "Pantalla: "+self._tipo+", Alto: "+str(self._alto)+", Ancho: "+str(self._ancho)

class Aplicacion:
    def __init__(self,nombre,tamanio):
        self._nombre=nombre
        self._tamanio=tamanio
    def get_nombre(self):
        return self._nombre
    def get_tamanio(self):
        return self._tamanio
    def __str__(self):
        return "App: "+self._nombre+", Tamaño: "+str(self._tamanio)

class Laptop:
    def __init__(self,modelo,tipo,alto,ancho):
        self._modelo=modelo
        self._cantApp=0
        self._apps=[]
        self._pantalla=Pantalla(tipo,alto,ancho)
    def agregaApp(self,app):
        self._apps.append(app)
        self._cantApp=self._cantApp+1
    def get_cantApp(self):
        return self._cantApp
    def get_modelo(self):
        return self._modelo
    def get_apps(self):
        return self._apps
    def get_pantalla(self):
        return self._pantalla
    def __str__(self):
        return "Laptop modelo: "+self._modelo+", Cantidad de apps: "+str(self._cantApp)+", "+str(self._pantalla)

if __name__=="__main__":
    vec=[]
    n=int(input("Ingrese la cantidad de laptops: "))
    for i in range(n):
        modelo=input("Ingrese el modelo de la laptop: ")
        tipo=input("Ingrese el tipo de pantalla: ")
        alto=int(input("Ingrese el alto de la pantalla: "))
        ancho=int(input("Ingrese el ancho de la pantalla: "))
        lap=Laptop(modelo,tipo,alto,ancho)
        vec.append(lap)

    if len(vec)>0:
        may=vec[0].get_cantApp()
        for l in vec:
            if l.get_cantApp()>may:
                may=l.get_cantApp()
        print("Laptop(s) con más aplicaciones:")
        for l in vec:
            if l.get_cantApp()==may:
                print(l)

    x=input("Ingrese el modelo X para agregar una aplicación: ")
    for l in vec:
        if l.get_modelo()==x:
            nom=input("Ingrese el nombre de la aplicación: ")
            tam=int(input("Ingrese el tamaño de la aplicación: "))
            appnueva=Aplicacion(nom,tam)
            l.agregaApp(appnueva)

    y=int(input("Ingrese el ancho Y de la pantalla para eliminar apps: "))
    for l in vec:
        if l.get_pantalla().get_ancho()==y:
            l.get_apps().clear()
            l._cantApp=0

    for l in vec:
        apps=l.get_apps()
        t=len(apps)
        for i in range(t-1):
            for j in range(t-1-i):
                a1=apps[j]
                a2=apps[j+1]
                cambiar=False
                if a1.get_tamanio()<a2.get_tamanio():
                    cambiar=True
                else:
                    if a1.get_tamanio()==a2.get_tamanio():
                        if a1.get_nombre()>a2.get_nombre():
                            cambiar=True
                if cambiar==True:
                    aux=apps[j]
                    apps[j]=apps[j+1]
                    apps[j+1]=aux

    print("Estado final:")
    for l in vec:
        print(l)
        apps=l.get_apps()
        for a in apps:
            print(a)