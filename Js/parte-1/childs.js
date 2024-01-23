const contenedor = document.querySelector('.contenedor')

const primerHijo = contenedor.firstChild

console.log(primerHijo) // Si hay espacios va a aparecer texto


const ultimoHijo = contenedor.lastChild

console.log(ultimoHijo)

const primerElementoHijo = contenedor.firstElementChild

console.log(primerElementoHijo)

const ultimoElementoHijo = contenedor.lastElementChild

console.log(ultimoElementoHijo)

const listaNodosHijos = contenedor.childNodes // Me da todos los hijos del contenedor

console.log(listaNodosHijos)

for (hijo in listaNodosHijos) {
    console.log(hijo)
}
