import React, { useState } from "react"

export const TabButton = ({ children, onSelect}) => {
    return (
        <li>
            <button onClick={onSelect}>
                {children}
            </button>
        </li>
    )
}