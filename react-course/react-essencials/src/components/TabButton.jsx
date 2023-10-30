import React, { useState } from "react"

export const TabButton = ({ children, onSelect, isSelected}) => {
    return (
        <li>
            <button onClick={onSelect} className={isSelected ? 'active' : undefined}>
                {children}
            </button>
        </li>
    )
}