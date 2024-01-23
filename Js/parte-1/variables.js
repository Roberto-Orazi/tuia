// Declaracion de variables
var variableVar = 'Tiene alcance global'
let variableLet = 'Nos limita el scope al bloque en el que estamos'
const variableConst = 'Es una variable constante si tiene el valor 3 el valor no va a cambiar y si la queremos cambiar va a tirar error'

// Tipos de dato
string = 'Cadena de texto'
number = 1
booleano = true

// Casos especiales
/*
Undefined: Es cuando esta declarada una variable pero no inicializada
const variableVacia
console.log(variableVacia) esto printea undefined

Null: Es un valor sin valor
let numero = null esto esta declarado y inicializado

Nan:(Not a number) Esto puede pasar cuando hacemos operaciones de por ej multiplicacion de texto y numero
*/

// Scope
let numero; // Existe en nuestro programa
numero = 29; // Inicializamos la variable
// Usamos siempre let en vez de var porque limitamos el uso en el programa

// Prompt

prompt('Hola este es un prompt osea un input por console.log')

nombre=prompt('Hola escribi tu nombre')
