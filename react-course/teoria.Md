## Why components?
- reusability
Dont repeat yourself

- separation of concerns
Dont do too many things in one and the same place

Split big chunks of code into multiple smaller functions

## How are they build

We mix html+css+js to create the ui.

## JSX
Es javascript+xml ya que html es xml al fin y al cabo

## How it works react
We have html inside js files so our html is desire target state

## COMPONENT TREE

->APP
     -> HEADER
     -> TASKS
             ->TASK
             ->TASK
             ->TASK

## Styled components
They are components created with style and they go in the end of the code.
1. Install package
```
npm install --save styled-components
```

2. For example we can create a new button:
```
import styled from 'styled-components'

const Button = styled.button`
estilos como en css
`
```
## How to read errors
1. check the file that has an error
2. See the line
3. See what type of error, usually especifies what error could be
4. see the fragment of the code that has an error

We can use breakpoints