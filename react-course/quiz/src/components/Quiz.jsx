import { useState, useCallback } from "react"

import QUESTIONS from '../questions'
import completeQuiz from '../assets/quiz-complete.png'
import QuestionTimer from "./QuestionTimer"


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
            <div id="summary">
                <img src={completeQuiz} alt="trophy icon" />
                <h2>
                    You have comlete the quiz!
                </h2>
            </div>
        )
    }
    const shuffleAnswers = [...QUESTIONS[activeQuestionIndex].answers]
    shuffleAnswers.sort(() => Math.random() - 0.5)
    return (
        <div id="quiz">
            <div id="question">
                <QuestionTimer
                key={activeQuestionIndex}
                    timeout={10000}
                    onTimeout={handleSkipAnswer} />
                <h2>
                    {QUESTIONS[activeQuestionIndex].text}
                </h2>
                <ul id="answers">
                    {shuffleAnswers.map((answer) => (
                        <li key={answer} className="answer">
                            <button onClick={() => handleSelectAnswer(answer)}>
                                {answer}
                            </button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    )
}