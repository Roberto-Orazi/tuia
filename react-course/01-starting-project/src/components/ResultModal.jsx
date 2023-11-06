import { forwardRef, useImperativeHandle, useRef } from "react"

export const ResultModal = forwardRef(function ResultModal({ result, targetTime, remainingTime, onReset }, ref) {
    const dialog = useRef()
    const formmattedRemainingTime = (remainingTime / 1000).toFixed(2)
    const userLost = remainingTime <= 0
    const score = Math.round((1 - remainingTime / (targetTime * 1000)) * 100)
    useImperativeHandle(ref, () => {
        return {
            open() {
                dialog.current.showModal()
            }
        }
    })

    return (
        <dialog ref={dialog} className="result-modal" onClose={onReset}>
            {userLost && <h2>You Lost</h2>}
            {!userLost && <h2>Your score: {score}</h2>}
            <p>
                The target time was <strong>{targetTime} seconds.</strong>
            </p>
            <p>
                You stopped the timer with <strong>{formmattedRemainingTime} seconds left.</strong>
            </p>
            <form method="dialog" onSubmit={onReset}>
                <button>Close</button>
            </form>
        </dialog>
    );
})