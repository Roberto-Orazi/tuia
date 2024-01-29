const person = {
    name: 'roberto',
    age: 29,
    greet() {
        console.log(`Hi im ${this.name}`)
    }
}

console.log(person)
person.greet()
console.log(person.name)
console.log(person.age)

const copyPerson = { ...person }

const hobbies = ['tennis', 'mechanical keyboards']
for (let hobby of hobbies) {
    console.log(hobby)
}

console.log(hobbies.map(hobby => {
    return `Hobbie: ${hobby}`
}))
console.log(`old array: ${hobbies}`)

hobbies.push('Programming')

const copyArraySlice = hobbies.slice()
const copyArray = [...hobbies]

const toArray = (arg1, arg2, arg3) => {
    return [arg1, arg2, arg3]
}
console.log(toArray(1, 2, 3))

const toArrayMultiple = (...args) => {
    return args
}
console.log(toArrayMultiple(1, 2, 3, 4, 5))