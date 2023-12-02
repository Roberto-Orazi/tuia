import React from "react"

export const CoreConcept = ({image, title,description}) => {
    return (
        <li>
            <img src={image}/>
            <h3>{title}</h3>
            <p>{description}</p>
        </li>
    )
}