# DOCKER

## repositorio de contenedores:
            - Privados
            - Publicos:
                    - docker hub:
                            - nodejs
                            - postgres
                            - python
                            - golang
                            - mysql
                            - etc

### Con contenedores:
- descargamos una imagen basada en linux
- podemos usar un solo comando para multiples versioens a la vez

#### Imagen
- Runtime Docker

Que es una imagen?

- Es lo que contiene las dependencias, el codigo y es lo que se comparte.
- Son capas tras capas de imagenes
- la primer imagen suele ser el so por ej: Alpine que es la mas liviana de linux

### Sin contenedores:
Tenemos el codigo

Tenemos que actualizar las dependencias

adentro de eso tenemos los archivos de configuracion

Puede pasar que tengamos distintas versiones de dependencias y problemas de comunicacion

vm: virtual machine

Harware -> [Kernel -> aplicaciones] muchos gbs

Docker se encarga de usar el kernel del so que estamos utilizando

Adentro de la virtualizacion existen 3:

- Paravirtualizacion: existe host y guest. Host es el so anfitrion en nuestro caso ubuntu, y el guest es la maquina
  virtual que vamos a instalar

Ubuntu -> Anfitrion

Ubuntu Debian suse -> Cliente

- Virtualizacion parcial: Algunos componentes del hardware se virtualizan para el so cliente.
- Virtualizacion completa: Todos los componetnes del hardware que se utilizan por el so cliente se virtualizan

docker: Los contenedores de docker tiene muy bien rendimiento en las virtualizaciones.

Docker desktop:

Es una vm, se encuentra optimizada y corre linux.

- Permite ejecutar containers.
- Permite acceder al distema de archivos
- Docker compose, CLI(comman line interface) y otras herramientas
- corre nativo en windows con wsl 2 win subs for linux

COMANDOS

docker images

Muestra esto:

REPOSITORY  TAG       IMAGE ID       CREATED      SIZE

ubuntu      20.04     14be0685b768   2 weeks ago   72.8MB

instalar en nuestro caso la imagen de ubuntu

sudo docker pull ubuntu:20.04

Para crear la imagen

docker create ubuntu

nos devuelve un id: b4286782d3e46ba23ba1103907ad9d12cdf6a99f4edb5583a3564346bf33e7c0

en nuestro caso eso

ahora ingresamos

docker start b4286782d3e46ba23ba1103907ad9d12cdf6a99f4edb5583a3564346bf33e7c0

nos devuelve nuestro id: b4286782d3e46ba23ba1103907ad9d12cdf6a99f4edb5583a3564346bf33e7c0

En docker hub podemos encontrar muchas imagenes

Por ej para node podemos tirar
```bash
docker run node
```
y va a hacer el pull solo en este caso porque no esta descargado

Con este comando vamos a ejecutarlo con una consola interactiva, por ej si hacemos una suma o demas va a resolverlo node
```bash
docker run -it node
```
ej
```bash
docker run -it node
Welcome to Node.js v23.6.0.
Type ".help" for more information.
> 1+1
2
>
```

Para ver los contenedores
```bash
docker ps -a

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES # Muestra esto
```

