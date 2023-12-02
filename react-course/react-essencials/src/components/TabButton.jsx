import React, { useState } from "react"

export const TabButton = ({ children, isSelected, ...props}) => {
    return (
        <li>
            <button className={isSelected ? 'active' : undefined} {...props}>
                {children}
            </button>
        </li>
    )
}