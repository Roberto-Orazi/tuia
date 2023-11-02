import { useState } from "react"

import { GameBoard } from "./components/GameBoard"
import { Player } from "./components/Player"

function App() {
  const [activePlayer, setActivePlayer] = useState('X')

  const handleSelectPlayer(){
    setActivePlayer((curActivePlayer) => curActivePlayer === 'X' ? 'O' : 'X')
  }

  return (
    <main>
      <div id="game-container">
        <ol id="players">
          <Player initialName='Player 1' symbol='X' />
          <Player initialName='Player 2' symbol='O' />
        </ol>
        <GameBoard />
      </div>
      Log
    </main>
  )
}

export default App
