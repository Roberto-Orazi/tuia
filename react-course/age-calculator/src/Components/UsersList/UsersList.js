import React from "react"
import classes from './UsersList.module.css'

export const UsersList = (props) => {
  return (
    <table className={classes.users}>
      <tbody>
        {props.data.map(userData => (
          <tr key={userData.userName}>
            <td>{userData.userName}</td>
            <td>{userData.age}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
