const person = {
    userName: 'roberto',
    age: 26,
    greet() {
        console.log(`Hi im ${this.name}`)
    }
}
const printName = ({ userName }) => {
    console.log(userName)
}

printName(person)

const { userName, age } = person

console.log(userName, age)