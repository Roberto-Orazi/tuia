import {render, screen, waitFor} from '@testing-library/react'
import user from '@testing-library/user-event'
import UserForm from './UserForm'

test('it shows two inputs and a button', () => {
    // render the component
    render(<UserForm/>)

    // manipulate the component or find an element in it
    const inputs = screen.getAllByRole('textbox')
    const button = screen.getByRole('button')

    // Assertion - Make sure that the component is doing what we expect it to do
    expect(inputs).toHaveLength(2)
    expect(button).toBeInTheDocument()

})

test('it calls onUserAdd when the form is submited', async () => {
    // Not the best implementation
    const mock = jest.fn()

    // Try to render my component
    render(<UserForm  onUserAdd={mock}/>)

    // Find the two inputs
    const nameInput = screen.getByRole('textbox', {
        name: /name/i
    })
    const emailInput = screen.getByRole('textbox', {
        name: /email/i
    })
    
    // Simulate typing a name
    await user.click(nameInput)
    await user.keyboard('test')
    // await userEvent.type(nameInput, 'test') se resume mas facil

    // Simulate typing a email
    await user.click(emailInput)
    await user.keyboard('typingtestemail@gmail.com')

    // Find the button
    const button = screen.getByRole('button')

    // Simulate clicking the button
    await user.click(button)

    // Assertion to make sure 'onUserAdd' gets call with email/name
    await waitFor(() => {
        expect(mock).toHaveBeenCalled()
        expect(mock).toHaveBeenCalledWith({name: 'test', email: 'typingtestemail@gmail.com'})
    })

})