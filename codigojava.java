class Anuncio {
    private int numero;
    private double precio;
    public Anuncio() {
        this.numero =0;
        this.precio =0.1;
    }
    public Anuncio(int num, double pre) {
        this.numero =num;
        this.precio =pre;
    }
}

class Artista {
    private String nombre;
    private int ci;
    private int aniosExp;
    public Artista(String nom, int car, int anios) {
        this.nombre =nom;
        this.ci= car;
        this.aniosExp= anios;
    }
    public int getAnios() {
        return this.aniosExp;
    }
}

class Obra {
    private String titulo;
    private String material;
    private Artista artista1;
    private Artista artista2;
    private Anuncio anuncio;
    public Obra(String titulo, String material, String nom1, int car1, int anio1, String nom2, int car2, int anio2) {
        this.titulo =titulo;
        this.material= material;
        this.artista1 =new Artista(nom1, car1, anio1);
        this.artista2 = new Artista(nom2, car2, anio2);
        this.anuncio= null;
    }
    public void agregarAnuncio(Anuncio anun) {
        this.anuncio = anun;
    }
    public Artista getArt1() {
        return this.artista1;
    }
}

class Pintura extends Obra {
    private String genero;
    public Pintura(String titulo, String material, String nom1, int car1, int anio1, String nom2, int car2, int anio2, String gen) {
        super(titulo, material, nom1, car1, anio1, nom2, car2, anio2);
        this.genero=gen;
    }
}

public class Main {
    public static void main(String[] args) {
        Anuncio a1 =new Anuncio();
        Anuncio a2= new Anuncio(2, 2.3);
        Pintura p1=new Pintura("monalisa", "oleo", "davinci", 123, 20, "joel", 321, 1, "intriga");
        Pintura p2 =new Pintura("monalisa", "oleo", "davinci", 123, 20, "adrian", 444, 4, "cuatro");
        p2.agregarAnuncio(a1);
    }
}