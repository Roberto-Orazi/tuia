import React, { useState } from 'react';
import { AddUser } from './Components/AddUser/AddUser';
import { UsersList } from './Components/UsersList/UsersList';
import { Modal } from './Components/ErrorModal/ErrorModal';

function App() {
  const [userData, setUserData] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const calculateHandler = (userInput) => {
    if (userInput['user-name'] === '' || userInput['age'] === 0) {
      console.log('Modal debe abrirse');
      setIsModalOpen(true);
    } else {
      setUserData((prevData) => [...prevData, userInput]);
    }
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <div>
      <AddUser addUser={calculateHandler} />
      {userData.length === 0 && <p style={{ textAlign: 'center' }}>No Users Added!</p>}
      {userData.length > 0 && <UsersList data={userData} />}
      <Modal isOpen={isModalOpen} close={closeModal} message="Por favor, completa todos los campos." />
    </div>
  );
}

export default App;