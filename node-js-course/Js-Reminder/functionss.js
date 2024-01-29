const userName = 'Rovs'
let age = 26
let hasHobbies = true

console.log(userName, age, hasHobbies)

// Asi se hacian antes
const summarizeUser = function (userName, userAge, userHasHobbies) {
    return (
        `Hi im ${userName}, i have ${userAge} and my hobbies are ${userHasHobbies}`
    )
}

console.log(summarizeUser(userName, age, hasHobbies))

const summarizeUserNew = (userName, userAge, userHasHobbies) => {
    return (
        `Hi im ${userName}, i have ${userAge} and my hobbies are ${userHasHobbies}`
    )
}

const add = (a, b) => {
    return a + b
}

const addOne = a => a + 1

console.log(addOne(2))


