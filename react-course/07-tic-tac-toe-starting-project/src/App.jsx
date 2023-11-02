import { useState } from "react"

import { GameBoard } from "./components/GameBoard"
import { Player } from "./components/Player"
import { Log } from "./components/Log"
import WINNING_COMBINATIONS from './winning-combination.js'

const deriveActivePlayer = (gameTurns) => {
  let currentPlayer = 'X'
  if (gameTurns.length > 0 && gameTurns[0].player === 'X') {
    currentPlayer = 'O'
  }
  return currentPlayer
}

function App() {
  const [gameTurns, setGameTurns] = useState([])
  /* const [activePlayer, setActivePlayer] = useState('X') */

  const activePlayer = deriveActivePlayer(gameTurns)

  const handleSelectPlayer = (rowIndex, colIndex) => {
    //setActivePlayer((curActivePlayer) => curActivePlayer === 'X' ? 'O' : 'X')
    setGameTurns(prevTurns => {
      const currentPlayer = deriveActivePlayer(prevTurns)

      const updatedTurns = [
        { square: { row: rowIndex, col: colIndex }, player: currentPlayer }
        , ...prevTurns,
      ]
      return updatedTurns
    })
  }

  return (
    <main>
      <div id="game-container">
        <ol id="players" className="highlight-player">
          <Player initialName='Player 1' symbol='X' isActive={activePlayer === 'X'} />
          <Player initialName='Player 2' symbol='O' isActive={activePlayer === 'O'} />
        </ol>
        <GameBoard
          onSelectPlayer={handleSelectPlayer}
          turns={gameTurns}
        />
      </div>
      <Log turns={gameTurns} />
    </main>
  )
}

export default App
