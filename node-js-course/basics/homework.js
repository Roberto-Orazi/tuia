const http = require('http')

const server = http.createServer((req, res) => {
    const url = req.url
    const method = req.method

    if (url === '/') {
        res.write('<html>')
        res.write('<head><title>Homework 1</title></head>')
        res.write('<body><h1>Hi how are you?</h1><form action="/create-user" method="POST"><input type="text" name="username"/><button type="submit">create user</button></form></body>')
        res.write('</html>')
        return res.end()
    }
    if (url === '/users') {
        res.write('<html>')
        res.write('<head><title>Homework 1</title></head>')
        res.write('<body><ul><li>user1</li><li>user2</li></ul></body>')
        res.write('</html>')
        return res.end()
    }
    if (url === '/create-user' && method === 'POST') {
        const body = []
        req.on('data', (chunk) => {
            body.push(chunk)
        })
        req.on('end', () => {
            const parsedBody = Buffer.concat(body).toString()
            console.log(parsedBody.split('=')[1])
        })
        res.statusCode = 302
        res.setHeader('Location', '/')
        return res.end()
    }
})

server.listen(3000)