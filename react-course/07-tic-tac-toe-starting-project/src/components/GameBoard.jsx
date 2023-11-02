import React from "react"

const initialGameBoard = [
    [null, null, null],
    [null, null, null],
    [null, null, null]
]
export const GameBoard = ({ onSelectPlayer, turns }) => {
    let gameBoard = initialGameBoard

    for (const turn of turns) {
        const { square, player } = turn
        const { row, col } = square

        gameBoard[row][col] = player
    }
    /* const [gameBoard, setGameBoard] = useState(initialGameBoard)

    const handleBoardSquare = (rowIndex, colIndex) => { setGameBoard((prevGameBoard) => { const updatedBoard =
        [...prevGameBoard.map(innerArray => [...innerArray])] updatedBoard[rowIndex][colIndex] = activePlayerSimbol
            return updatedBoard }) onSelectPlayer() }
 */
    return (
        <ol id="game-board">
            {gameBoard.map((row, rowIndex) => <li key={rowIndex}>
                <ol>
                    {row.map((playerSimbol, colIndex) =>
                        <li key={colIndex}>
                            <button onClick={() =>
                                onSelectPlayer(rowIndex, colIndex)}
                                disabled={playerSimbol !== null}>
                                {playerSimbol}
                            </button>
                        </li>)}
                </ol>
            </li>)}
        </ol>
    )
}