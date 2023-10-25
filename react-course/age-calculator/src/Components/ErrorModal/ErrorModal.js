import React from 'react';
import classes from './ErrorModal.module.css';

export const Modal = ({ isOpen, close, message }) => {
  return (
    isOpen && (
      <div className={classes.modal}>
        <div className={classes['modal-content']}>
          <span className={classes.close} onClick={() => {
            console.log('Cerrando el modal');
            close();
          }}>
            &times;
          </span>
          <p>{message}</p>
        </div>
      </div>
    )
  );
};