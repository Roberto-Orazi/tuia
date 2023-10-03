# ALPHAFOLD
## Que son las proteinas?
1. Aminoacido(Una molecula)
```
Tiene 3 grupos
Amino
Acido
R: Da 20 aminoacidos
```
2. Secuencias de aminoacidos Las proteinas son secuencias de aminoacidos Yo tengo 20 combinaciones de aminoacidos por
cada aminoacido Por lo tanto si tengo 2 aminoacidos tengo: AxA=20x20

3. Proteinas Hay 4 estructuras Primaria:
- Lineal Secundaria:
- Helices Alfa (Helicoideal)
- Laminas Beta (Lamina plegada) Terciaria(Monomero):
- Es un conjunto de helices alfa y laminas beta
- Se puede unir por afinidad Cuaternaria:
- Conjunto de Estructuras terciarias
- Conjunto de proteinas funcionales(Dimero)
- Adentro de los dimeros estan los homogeneos(Homodimeros: son de 1 sola proteina) y heterogeneos(Heterodimeros:
  Distintas proteinas)

### Problema de alphafold adentro de las proteinas
El problema viene para crear los homo dimeros cuando son iguales

4. Funcion de alphafold en las proteinas


## RAYOS X / El problema del plegado(CAPS)/ Base de Datos
1. Rayos x
- Se le hacen rayos x a las proteinas
- Se usa para descubrir la estructura 3d de las proteinas
- Para hacerle los rayos x:
    1. Se purifican las proteinas
    2. Se cristalizan las proteinas

- Se cristalizan las proteinas para usar los rayos x, hay algunas proteinas que no se pueden cristalizar ya que estan
  constantemente en movimiento
- Proteinas intrinsecamente desordenadas


2. CASP
- Surge por el alto costo de los rayos X
- Da soluciones para sacar las estructuras 3d segun las secuencias que le ingresamos
- Busca secuencias que no esten en las base de datos
- En fin es una base de datos donde estan todas las estructuras 3d de todas las proteinas no publicadas y se usa para
  ver que algoritmo de todos los hechos se asemeja mas al real
### Como funciona el casp
De 10 secuencias hasta 2018 acertaba 5 proteinas En 2020 con alphafold llego hasta un 92.4% de gdt que seria la
distancia entre la estructura del cristal con la predicha De una secuencia generan una imagen


1. Base de datos
- Se crea PDB Protein Data Bank
- PDB TIENE:
    1. La secuencia
    2. La estructura 3d

- Tenes resonador magnetico
- Rayos x
- Cryo-en

4. CASP Alphafold
    1. Se ingresa la matriz con las distancias entre los aminoacidos(PAE)
    2. De los datos de la matriz creamos la imagen que tenes un color para valores iguales a 0 y una tonalidad de
       colores para valores distintos a 0
    3. Ahi entra alphafold y de la primera imagen crea otra imagen con una estructura de colores para que lo entienda a
       la hora de hacer la estructura
    4. De la imagen generada se hace la estructura 3d de la proteina
### Training de alpha fold
1. secuencia
2. estructura 3d
3. matriz de distancias

## ALPHAFOLD: Como resuelve los problemas

## Lo negativo de ALPHAFOLD
