import { useContext } from "react";
import Modal from "./UI/Modal";
import CartContext from '../store/CartContext'
import { currencyFormatter } from '../util/formatting'
import Button from "./UI/Button";

export default function Cart(){
    const cartCtx=useContext(CartContext)

    const cartTotal = cartCtx.item.reduce((totalPrice,item)=>{
        totalNumberOfItems+(item.quantity*item.price) ,0
    })
    return(
        <Modal className="cart" >
            <h2>Your cart</h2>
            <ul>
        {cartCtx.items.map((item)=><li key={item.id}>{item.name - item.quantity}</li>)}
            </ul>
            <p className="cart-total">{currencyFormatter.format(cartTotal)}</p>
            <p className="modal-actions">
                <Button textOnly>Close</Button>
                <Button>Go to checkout</Button>
            </p>
        </Modal>
    )
}