import React from "react"

export const TabContent = ({ title, description, code }) => {
    return (
        <>
            <h3>
                {title}
            </h3>
            <p>
                {description}
            </p>
            <pre>
                <code>
                    {code}
                </code>
            </pre>
        </>
    )
}