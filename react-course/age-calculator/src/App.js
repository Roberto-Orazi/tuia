import { useState } from 'react';
import { AddUser } from './Components/AddUser/AddUser';
import { UsersList } from './Components/UsersList/UsersList';

function App() {
  const [userInput, setUserInput] = useState(null)

  const calculateHandler = (userInput) => {
    setUserInput(userInput)
  };
  const userData = [];
  if (userInput) {
  }
  return (
    <div>
      <AddUser onCalculate={calculateHandler} />
      {!userInput && <p style={{textAlign: 'center'}}>No Users Added!</p>}
      {userInput && <UsersList data={userData} initialInvestment={userInput['current-savings']} />}

    </div>
  );
}

export default App;
