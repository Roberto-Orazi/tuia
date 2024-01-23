function saludar() {
    return (
        console.log('Hola')
    )
}

saludar()

function suma(numUno, numDos) {
    return numUno + numDos
}

resultado=suma(1,2)
console.log(resultado)

const saludarNombreFunction = function(nombre){
    let frase=`Hola, ${nombre} como estas?`
    console.log(frase)
}

saludarNombreFunction('roberto')


const saludarNombre = (nombre) =>{
    let frase=`Hola, ${nombre} como estas?`
    console.log(frase)
}

saludarNombre('roberto sin function')