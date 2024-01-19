// while nunca ejecuta el codigo hasta que sea true
let numero = 0;
while (numero < 6) {
    console.log('El numero es menor')
    numero++
}

// do while la diferencia es que la primera vez siempre entra, despues verifica si cumple la condicion
do {
    console.log('El numero es menor')
    numero++
}
while (numero <= 6)

// Break en el while
while (numero < 1000) {
    console.log('El numero es menor')
    numero++
    if (numero == 10) {
        break // nos saca afuera del bucle
    }
}

// for
/*
1. Declaracion y Inicializacion
2. Condicion
3. Incremento o decremento
*/
for (let i = 0; i < 100; i++) {
    console.log(i)
    if (i == 12) {
        continue // esto lo que hace es saltear el 12 en este caso, osea que termina la iteracion en la cual esta el bucle
    }
}

let animales = ['gato', 'perro', 'dinosaurio']

for (animal in animales) {
    console.log(animal) // esto nos va a mostrar la posicion de cada elemento del array osea 0,1,2
    console.log(animales[animal])//Esto nos mostraria el elemento de cada elemento del array osea 'gato', 'perro', 'dinosaurio'
}

for (animal of animales) {
    console.log(animal) // Nos va a devolver el elemento de cada elemento del array osea 'gato', 'perro', 'dinosaurio'
}