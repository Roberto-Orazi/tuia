console.log('METODO POP')

let nombresPop = ['Roberto', 'Delfina', 'Athena']

console.log(`Array completo: ${nombresPop}`)

let resultadoPop = nombresPop.pop() // Pop elimina el ultimo del array

console.log(`Elemento eliminado: ${resultadoPop}`)

console.log(`Array despues del metodo: ${nombresPop}`)


console.log('METODO SHIFT')


let nombresShift = ['Roberto', 'Delfina', 'Athena']

console.log(`Array completo: ${nombresShift}`)

let resultadoShift = nombresShift.shift() // Shift elimina el primero del array

console.log(`Elemento eliminado: ${resultadoShift}`)

console.log(`Array despues del metodo: ${nombresShift}`)

console.log('METODO PUSH')
let nombresPush = ['Roberto', 'Delfina', 'Athena']

console.log(`Array completo: ${nombresPush}`)

let resultadoPush = nombresPush.push('Wendy') // Push Agrega un elemnto al final del array

console.log(`Cantidad de elementos que tiene: ${resultadoPush}`) // Marca la cantidad total de elementos

console.log(`Array despues del metodo: ${nombresPush}`)


console.log('METODO REVERSE')
let nombresReverse = ['Roberto', 'Delfina', 'Athena']

console.log(`Array completo: ${nombresReverse}`)

let resultadoReverse = nombresReverse.reverse() // Reverse, nos da vuelta el orden del array

console.log(`Luego de modificarlo: ${resultadoReverse}`) // Nos da vuetla todo el array pero sobre el original.

console.log(`Array despues del metodo: ${nombresReverse}`)

console.log('METODO UNSHIFT')

let nombresUnshift = ['Roberto', 'Delfina', 'Athena']

console.log(`Array completo: ${nombresUnshift}`)

let resultadoUnshift = nombresUnshift.unshift('Wendy') // Unshift, nos agrega el elemento al principio del array

console.log(`Cantidad de elementos que tiene: ${resultadoUnshift}`) // Marca la cantidad total de elementos

console.log(`Array despues del metodo: ${nombresUnshift}`)

console.log('METODO SORT')

let nombresSort = ['Roberto', 'Delfina', 'Athena']

console.log(`Array completo: ${nombresSort}`)

let resultadoSort = nombresSort.sort() // Sort, ordena de menor a mayor o alfabeticamente de manera standar.

console.log(`Elementos ordenados en mi nuevo array ${resultadoSort}`) //Son los elementos del nuevo array ordenados

console.log(`Array despues del metodo: ${nombresSort}`) // Este metodo al igual que el reverse nos modifica el array original


console.log('METODO SPLICE')

let nombresSplice = ['Roberto', 'Delfina', 'Athena']

console.log(`Array completo: ${nombresSplice}`)

let resultadoSplice = nombresSplice.splice(1, 2) // Splice, le damos 2 parametros y borra los elementos entre las posiciones dadas

console.log(`Elementos eliminados por splice: ${resultadoSplice}`)

console.log(`Elemento cortado: ${nombresSplice}`)



console.log('METODO AGREGAR SPLICE')

let nombresAgregarSplice = ['Roberto', 'Delfina', 'Athena']

console.log(`Array completo: ${nombresAgregarSplice}`)

let agregarConSplice = nombresAgregarSplice.splice(0, 1, 'Robertito') // Splice, le damos 2 parametros y borra los elementos entre las posiciones dadas

console.log(`Elemento eliminado por splice: ${agregarConSplice}`)

console.log(`Elemento cortado: ${nombresAgregarSplice}`)

