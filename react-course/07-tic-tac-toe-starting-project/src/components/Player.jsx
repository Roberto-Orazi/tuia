import React, { useState } from "react"

export const Player = ({ initialName, symbol, isActive }) => {
    const [playerName, setPlayerName] = useState(initialName)
    const [isEditing, setIsEditing] = useState(false)

    const editHandler = () => {
        setIsEditing((editing) => !editing);
    }
    const handleChange = (event) => {
        setPlayerName(event.target.value);
    }
    let editableName = <span className="player-name">{playerName}</span>
    //let editButton = 'edit'
    if (isEditing) {
        editableName = <input type="text" required value={playerName} onChange={handleChange} />
        //editButton = 'save'
    }
    return (
        <li className={isActive ? 'active' : undefined}>
            <span className="player">
                {editableName}
                <span className="player-symbol">
                    {symbol}
                </span>
            </span>
            <button onClick={editHandler}>{isEditing ? 'Save' : 'Edit'}</button>
        </li>
    )
}
