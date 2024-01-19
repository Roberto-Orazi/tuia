class animal {
    constructor(especie, edad, color) {
        this.especie = especie
        this.edad = edad
        this.color = color
        this.informacion = `soy ${this.especie}, tengo ${this.edad} años`
    }
    verInformacion() {
        console.log(this.informacion)
    }
}

let perro = new animal('perro', 2, 'atigrado')
let gato = new animal('gato', 3, 'naranja')
let tortuga = new animal('tortuga', 20, 'marron')
console.log(perro)
console.log(perro.color)
console.log(perro.informacion)
console.log(gato.informacion)
console.log(tortuga.informacion)

perro.verInformacion()
tortuga.verInformacion()
gato.verInformacion()