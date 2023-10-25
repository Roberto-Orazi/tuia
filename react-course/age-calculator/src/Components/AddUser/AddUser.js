import React, { useState } from "react";
import classes from './AddUser.module.css'

const initialValues = {
    'user-name': '',
    'age': 0,
}

export const AddUser = (props) => {
    const [userInput, setUserInput] = useState(initialValues)

    const submitHandler = (event) => {
        event.preventDefault();
        props.addUser(userInput);
        setUserInput(initialValues);
    };

    const changeHandler = (input, value) => {
        setUserInput((prevInput) => {
            return {
                ...prevInput,
                [input]: value,
            }
        })
    }

    return (
        <form onSubmit={submitHandler} className={classes.form}>
            <div className={classes['input-group']}>
                <p>
                    <label
                        htmlFor="user-name">UserName</label>
                    <input
                        onChange={(event) =>
                            changeHandler('user-name', event.target.value)}
                        value={userInput['user-name']}
                        type="text"
                        id="user-name" />
                </p>
                <p>
                    <label
                        htmlFor="age">Age (Years)</label>
                    <input onChange={(event) =>
                        changeHandler('age', event.target.value)
                    }
                        value={userInput['age']}
                        type="number"
                        id="age" />
                </p>
            </div>
            <p className={classes.actions}>
                <button type="submit" className={classes.button}>
                    Add User
                </button>
            </p>
        </form>
    )
}