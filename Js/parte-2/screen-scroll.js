const screen = window.screen
const screenLeft = window.screenLeft
const screenTop = window.screenTop

console.log(screen) // Esto es un objeto
console.log(screen.width) // Asique con el . accedemos a todas las propiedades del objeto

const scrollX = window.scrollX // Esto es el desplazamiento horizontal
const scrollY = window.scrollY // Estoy es el dezplazamiento vertical

const scroll = window.scroll(0, 100) // Esto nos scrolea hasta donde le demos, pero es absoluto. para relativo tenemos moveBy()

const ventana = window.open('https://robertoorazi.com.ar')

ventana.resizeBy(200, 400) // Esto lo que nos hace es nos cambia el tamaño al especificado
ventana.resizeTo(200, 400) // Esto nos redimenciona la ventana
ventana.moveBy(100, 200) // Esto nos scrolea 100 en x y 200 en y lo podemos usar varias veces y nos va a mover
ventana.moveTo(100, 200) // Esto es lo mismo que window.scroll()

