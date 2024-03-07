const express = require('express')

const app = express()

app.use('/',(res, req, next) => {
    console.log('hello')
    req.send('<h1>hello this is what i made</h1>')
    next()
})

app.use('/users',(res, req, next) => {
    console.log('hello this')
    req.send('<h1>hello this is what i made bye</h1>')
})

app.listen(3000)