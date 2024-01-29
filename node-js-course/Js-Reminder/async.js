const fetchData = () => {
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Done')
        }, 1100)
    })
    return promise
}

setTimeout(() => {
    console.log('one second')
}, 1000)
setTimeout(() => {
    console.log('two seconds')
    console.log('Timer is done')
    fetchData()
        .then(text => {
            console.log(text)
            return fetchData()
        })
        .then(text2 => {
            console.log(text2)
        })
}, 2000)
// Se llama asincrono porque no se ejecuta ni finaliza de inmediato.

console.log('Hola, esto esto es codigo sincronico y los otros son asincronicos')