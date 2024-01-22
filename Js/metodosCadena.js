let cadenaConcat='Cadena de prueba'

resultadoConcat = cadenaConcat.concat(' concatenada') // Concatena los strings

console.log(resultadoConcat)


let cadenaStartsWith='Cadena de prueba'
let inicioCadena = 'Cadena'

resultadoStartsWith = cadenaStartsWith.startsWith(inicioCadena) // verifica si la cadena empieza con el string que le pasemos como parametro

console.log(resultadoStartsWith)

let cadenaEndsWith='Cadena de prueba'
let finCadena = 'de prueba'

resultadoEndsWith = cadenaEndsWith.endsWith(finCadena) // verifica si la cadena termina con el string que le pasemos como parametro

console.log(resultadoEndsWith)

let cadenaIncludes='Cadena de prueba'
let incluyeCadena = 'de'

resultadoIncludes = cadenaIncludes.includes(incluyeCadena) // verifica el parametro que le pasamos esta en nuestra cadena

console.log(resultadoIncludes)

let cadenaPosition='Cadena de prueba'
let posicionCadena = 'de'

resultadoPosition = cadenaPosition.indexOf(posicionCadena) // Nos dice en que posicion esta la cadena, si devuelve -1 es porque no esta

console.log(resultadoPosition)

let cadenaLastPosition='Cadena de prueba de de de de de de de de de de de de de de de'
let ultimaPosicionCadena = 'de'

resultadoLastPosition = cadenaLastPosition.lastIndexOf(ultimaPosicionCadena) // Nos dice en que posicion esta la ultima cadena, si devuelve -1 es porque no esta

console.log(resultadoLastPosition)
