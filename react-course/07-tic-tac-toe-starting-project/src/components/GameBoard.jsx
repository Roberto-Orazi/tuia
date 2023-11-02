import React, { useState } from "react"

const initialGameBoard = [
    [null, null, null],
    [null, null, null],
    [null, null, null]
]
export const GameBoard = (onSelectPlayer) => {
    const [gameBoard, setGameBoard] = useState(initialGameBoard)

    const handleBoardSquare = (rowIndex, colIndex) => {
        setGameBoard((prevGameBoard) => {
            const updatedBoard = [...prevGameBoard.map(innerArray => [...innerArray])]
            updatedBoard[rowIndex][colIndex] = 'X'
            return updatedBoard
        })
    }

    onSelectPlayer()
    return (
        <ol id="game-board">
            {gameBoard.map((row, rowIndex) => <li key={rowIndex}>
                <ol>
                    {row.map((playerSimbol, colIndex) =>
                        <li key={colIndex}>
                            <button onClick={() => handleBoardSquare(rowIndex, colIndex)}>
                                {playerSimbol}
                            </button>
                        </li>)}
                </ol>
            </li>)}
        </ol>
    )
}