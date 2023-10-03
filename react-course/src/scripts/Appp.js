//import apiKey from "./util.js"
//import * as util from "./util.js"
import { apiKey as asl, abc as content } from "./util.js"
import { Greet } from './Function.js'

const user = {
    name: "Roberto",
    age: 26,
    greet() {
        return "hello"
    }
}
class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greeet() {
        console.log('hi')
    }
}
const hobbies = ['uno', 'dos']
hobbies.push("tres") //agrega el string al final del array
const index = hobbies.findIndex((item) => {
    return item === 'uno'
})
console.log(index) //va a devolver el indice de el string uno osea el indice 0
const editedhob = hobbies.map((item) => ({ text: item }))
console.log(editedhob)
const editedhobb = hobbies.map((item) => item + '!')
console.log(editedhobb)
const user1 = new User("rob", 23)
export const Appp = () => {
    return (
        <div>
            <>{console.log(content, asl)}</>
            <h1>
                {content}
            </h1>
            {Greet('roberto')}
            <br />
            {Greet('juan', 'Hola, como estas')}
            <h2>{user.greet()}</h2>
            <h2>{console.log(user1)}</h2>
            <h3>{hobbies[0]}</h3>
            <h3>{hobbies[1]}</h3>
        </div>
    )
}
const [firstName, lastName] = ['Roberto', 'Orazi']
console.log(firstName, lastName)

const user2 = {
    name: 'robertito',
    age: 26
}
console.log(user2)
const { name: userName, age } = {
    name: 'robvi',
    age: 0
}
console.log(userName, age)

const hobbies2 = ['keyboards', 'cars']
const user4 = {
    name: 'robert',
    age: 20
}

const newHobbies = ['computer']

const mergedHobbies = [...hobbies2, ...newHobbies] //LOS 3 PUNTOS SON PARA SACAR LOS VALORES DE LOS ARREGLOS
console.log(mergedHobbies)

const extendedUser = {
    isAdmin: true,
    ...user4
}

console.log(extendedUser)

const password = prompt('Your password')

console.log(password)

if (password === 'Hello') {
    console.log('Hello works')
} else if (password === 'hello') {
    console.log('hello works')
} else {
    console.log('Access not granted')
}

const keyboards = ['savage65', 'hyperx tkl']

for (const keyboard of keyboards) {
    console.log(keyboard)
}

const list = document.querySelector('ul')
list.remove()
function handleTimeout() {
    console.log('Timed out!')
}
const handleTimeout2 = () => {
    console.log('Timed out ... again!')
}
setTimeout(handleTimeout, 2000) // SI LLAMO A LA FUNCION handleTimeout() CON LOS PARENTESIS SE EJECUTA ENSEGUIDA
setTimeout(handleTimeout2, 3000)

function greeter(greetFn) {
    greetFn()
}
greeter(() => console.log('hi'))

function init() {
    function greet() {
        console.log('hi!!!')
    }
    greet()
}

init()

let userMessage = 'Hello!'
userMessage=userMessage.concat('!!!!')
console.log(userMessage)

const hobbies3=['sports','cooking']
hobbies3.push('working')

