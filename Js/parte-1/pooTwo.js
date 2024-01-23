class Animal {
    constructor(especie, edad, color) {
        this.especie = especie
        this.edad = edad
        this.color = color
        this.info = `soy un ${this.especie} y tengo ${this.edad} años`
    }
    verInfo() {
        console.log(this.info)

    }
}

class Perro extends Animal {
    constructor(especie, edad, color, raza) {
        super(especie, edad, color)
        this.raza = 'bulldog'
        this.info+= ` y soy de raza ${this.raza}`
    }
    ladrar() {
        console.log('wow')
    }
    static comer() {
        console.log('Estoy comiendo')
    }
    set setRaza(newName) {
        this.raza = newName
    }
    get getRaza(){
        return this.raza
    }
}

const perrito = new Perro('perro', 5, 'negro', 'bulldog')

perrito.verInfo()
perrito.ladrar()
Perro.comer()

perrito.setRaza='doberman'
console.log(perrito.getRaza)