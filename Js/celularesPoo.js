class Celular {
    constructor(color, peso, rdp, rdc, ram) {
        this.color = color;
        this.peso = peso;
        this.rdp = rdp;
        this.rdc = rdc;
        this.ram = ram;
        this.encendido = false;
    }

    prender() {
        if (this.encendido == false) {
            console.log('Celular prendiendo')
            this.encendido = true
        }
        else {
            console.log('el celular ya esta encendido')
        }
    }

    apagar() {
        if (this.encendido == true) {
            console.log('Celular apagandose')
            this.encendido = false
        }
        else {
            console.log('el celular ya esta apagado')
        }
    }

    reiniciar() {
        if (this.encendido == true) {
            console.log('Celular reiniciandose')
        }
        else {
            console.log('el celular esta apagado')
        }
    }

    tomarFotos() {
        console.log(`Foto tomada en una resolucion de ${this.rdc}`)
    }

    grabarVideo() {
        console.log(`Video grabado en una resolucion de ${this.rdc}`)
    }
    mostrarInfo() {
        console.log(`
        Color: ${this.color}
        Peso: ${this.peso}
        Resolucion de pantalla: ${this.rdp}
        Ram: ${this.ram}
        Resolucion de camara: ${this.rdc}
        `)
    }
}

celularSamsung = new Celular('gris', '130g', '5" ', 'full hd', '3GB')
celularIphone = new Celular('rose gold', '110g', '4.9" ', '2k', '4GB')

celularSamsung.prender()
celularSamsung.tomarFotos()
celularSamsung.reiniciar()
celularSamsung.grabarVideo()
celularSamsung.apagar()

celularIphone.mostrarInfo()
celularSamsung.mostrarInfo()

class CelularAltaGama extends Celular {
    constructor(color, peso, rdp, rdc, ram, rdce) {
        super(color, peso, rdp, rdc, ram)
        this.rdce = rdce
    }
    grabarEnCamaraLenta() {
        console.log(`Video en camara lenta en resolucion ${this.rdce}`)
    }
    reconocimientoFacial() {
        console.log('Estamos haciendo el reconocimiento facial')
    }
    infoAltaGama(){
        this.mostrarInfo() + `resolucion de camara trasera: ${this.rdce}`
    }
}

celularIphoneProMax = new CelularAltaGama('oro', '130g', '5.7" ', '4k', '7GB', '2k')

celularIphoneProMax.grabarEnCamaraLenta()
celularIphoneProMax.infoAltaGama()