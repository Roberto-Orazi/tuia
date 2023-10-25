import React from "react"
import classes from './UsersList.module.css'

export const UsersList = (props) => {
  const filteredUsers = props.data.filter(user => user['user-name'] !== '');

  return (
    <table className={classes.users}>
      <tbody>
        {filteredUsers.map(userData => (
          <tr key={userData['user-name']}>
            <td>{userData['user-name']}</td>
            <td>{userData['age']}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
