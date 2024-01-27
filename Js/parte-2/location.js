const href = window.location.href // Localizacion/ruta de mi archivo

console.log(href)

const hostname = window.location.hostname // Nos devuelve el dominio del servidor web

console.log(hostname)

const pathname = window.location.pathname // Nos devuelve la ruta del dominio en la que estamos parados

console.log(pathname)

const protocol = window.location.protocol // Nos devuelve el protocolo, si es http https etc

console.log(protocol)

const assign = window.location.assign('https://youtube.com') // Carga un nuevo documento

/*
https://   youtube.com  /channel/asd098asased334-asd
protocol + hostname  +  pathname = href
*/