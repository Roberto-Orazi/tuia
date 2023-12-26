import { useState, useCallback } from "react"

import QUESTIONS from '../questions'

import Question from "./Question"
import Summary from "./Summary"


export default function Quiz() {
    const [userAnswers, setUserAnswer] = useState([])
    const activeQuestionIndex = userAnswers.length
    const quizIsComplete = activeQuestionIndex === QUESTIONS.length

    const handleSelectAnswer = useCallback(function handleSelectAnswer(selectedAnswer) {
        setUserAnswer((prevUserAnswer) => {
            return [...prevUserAnswer, selectedAnswer]
        })
    }, [])

    const handleSkipAnswer = useCallback(() => handleSelectAnswer(null), [handleSelectAnswer])

    if (quizIsComplete) {
        return (
            <Summary userAnswers={userAnswers}/>
        )
    }
    return (
        <div id="quiz">
            <Question
                key={activeQuestionIndex}
                index={activeQuestionIndex}
                onSelectAnswer={handleSelectAnswer}
                onSkipAnswer={handleSkipAnswer}
            />
        </div>
    )
}