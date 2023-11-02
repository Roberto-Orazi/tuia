import React from "react"

export const GameBoard = ({ onSelectPlayer, board }) => {
    /* const [gameBoard, setGameBoard] = useState(initialGameBoard)

    const handleBoardSquare = (rowIndex, colIndex) => { setGameBoard((prevGameBoard) => { const updatedBoard =
        [...prevGameBoard.map(innerArray => [...innerArray])] updatedBoard[rowIndex][colIndex] = activePlayerSymbol
            return updatedBoard }) onSelectPlayer() }
 */
    return (
        <ol id="game-board">
            {board.map((row, rowIndex) => <li key={rowIndex}>
                <ol>
                    {row.map((playerSymbol, colIndex) =>
                        <li key={colIndex}>
                            <button onClick={() =>
                                onSelectPlayer(rowIndex, colIndex)}
                                disabled={playerSymbol !== null}>
                                {playerSymbol}
                            </button>
                        </li>)}
                </ol>
            </li>)}
        </ol>
    )
}