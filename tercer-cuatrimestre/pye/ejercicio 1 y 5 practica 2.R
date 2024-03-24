datos <- read.csv("~/Downloads/Datos U2 - ej 1.csv")

colnames(datos) <- c('etapas','frecuencia', 'relativa')

datos <- read.csv("~/Downloads/Datos U2 - ej 5.csv", dec=',')
hist(datos$Duracion.1,
     breaks=8,
     main="Histograma de frecuencias",
     col='red')
