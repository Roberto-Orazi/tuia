import React from "react"
import reactImg from '../../assets/react-core-concepts.png'
import './Header.css'
const words = ['Fundamental', 'Crucial', 'Core']
function genRandomInt(max) {
  return Math.floor(Math.random() * (max + 1))
}
export const Header = () => {
  const initialWord = words[genRandomInt(2)]
  return (
    <header>
      <img src={reactImg} alt="Stylized atom" />
      <h1>React Essentials</h1>
      <p>
        {initialWord} React concepts you will need for almost any app you are
        going to build!
      </p>
    </header>
  )
}