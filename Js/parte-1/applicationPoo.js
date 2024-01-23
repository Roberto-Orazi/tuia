class App {
    constructor(descargas,puntuacion,peso){
        this.descargas=descargas
        this.puntuacion=puntuacion
        this.peso=peso
        this.iniciada=false
        this.instalada=false
    }
    abrir(){
        if (this.iniciada==false && this.instalada==true){
            this.iniciada=true
            console.log('app abierta')
        }
        else if(this.instalada==false){
            console.log('la app no esta instalada')
        }
        else{
            console.log('la app ya esta abierta')
        }
    }
    cerrar(){
        if (this.iniciada==true && this.instalada==true){
            this.iniciada=false
            console.log('app cerrada')
        }
        else if(this.instalada==false){
            console.log('la app no esta instalada')
        }
        else{
            console.log('la app no esta abierta')
        }
    }
    instalar(){
        if(this.instalada==false){
            this.instalada=true
            console.log('se instalo la app')
        }
        else{
            console.log('app ya instalada')
        }
    }
    desinstalar(){
        if(this.instalada==true && this.instalada==true){
            this.instalada=false
            console.log('se desinstalo la app')
        }
        else{
            console.log('La app no esta instalada')
        }
    }
    appInfo(){
        console.log(
            `
            Descargas totales: ${this.descargas}
            Puntuacion: ${this.puntuacion}
            Peso: ${this.peso}
            `
        )
    }
}

app = new App('16.000','5 estrellas', '900mb')

app.instalar()
app.desinstalar()
app.abrir()

app.appInfo()