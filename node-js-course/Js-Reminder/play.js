var userName = 'Rovs'
var age = 26
var hasHobbies = true

console.log(userName, age, hasHobbies)

function summarizeUser(userName, userAge, userHasHobbies) {
    return (
        `Hi im ${userName}, i have ${userAge} and my hobbies are ${userHasHobbies}`
    )
}

console.log(summarizeUser(userName, age, hasHobbies))

// Se usa let, var no se usa mas, excepto que seas trolaso

let userName = 'Rovs'
let age = 26
let hasHobbies = true

console.log(userName, age, hasHobbies)

function summarizeUser(userName, userAge, userHasHobbies) {
    return (
        `Hi im ${userName}, i have ${userAge} and my hobbies are ${userHasHobbies}`
    )
}

console.log(summarizeUser(userName, age, hasHobbies))

// const ya que por lo general no cambiamos de nombre, de hobbie si, pero bueno saludos.
const userName = 'Rovs'
let age = 26
const hasHobbies = true
age = 27 // Cumpli años
console.log(userName, age, hasHobbies)

function summarizeUser(userName, userAge, userHasHobbies) {
    return (
        `Hi im ${userName}, i have ${userAge} and my hobbies are ${userHasHobbies}`
    )
}

console.log(summarizeUser(userName, age, hasHobbies))