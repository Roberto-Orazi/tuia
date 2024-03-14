import { Children, createContext, useState } from "react";

const UserProgressContext = createContext({
    Progress:'',
    showCart:()=>{},
    hideCart:()=>{},
    showCheckout:()=>{},
    hideCheckout:()=>{},
})

export function UserProgressContextProvider({Children}){
    const [userProgress,setUserProgress]=useState()
    
    function showCart(){}
    function hideCart(){}
    function showCheckout(){}
    function hideCheckout(){}

    return(
        <UserProgressContext.Provider>
            {Children}
        </UserProgressContext.Provider>
    )
}
export default UserProgressContext;