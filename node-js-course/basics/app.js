// http module
const http = require('http')

// function rqListener(req, res) {} Se hace la funcion en el mismo createServer
//http.createServer(function (req, res) { })

const server = http.createServer((req, res) => {
    console.log(req.url, req.method, req.headers)
    //process.exit()
    res.setHeader('Content-Type', 'text/html')
    res.write('<html>')
    res.write('<head><title>My first page</title></head>')
    res.write('<body><h1>Hello from my nodejs</h1></body>')
    res.write('</html>')
    res.end()
})

server.listen(3000)