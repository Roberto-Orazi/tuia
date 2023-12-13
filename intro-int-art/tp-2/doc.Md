# Trabajo practico Introduccion a la inteligencia artificial
#### Orazi, Roberto
# Generador de voz

## Dataset
### Eleccion de cancion
Comencé seleccionando la voz que quería que mi modelo entrenara; en mi caso, elegí a Bryant Myers. Para ello, descargué una de sus canciones desde YouTube.

### Separacion de las voces de los intrumentos
Utilicé el colab proporcionado para separar la voz de mi artista. El proceso tardó menos de 2 minutos en total para 7 canciones. Aunque no quedaron perfectas, logró separar bastante bien la voz de los instrumentos.

### Curacion de datos
No realicé una curación exhaustiva de datos debido a que la separación de instrumentos no fue tan mala y tampoco disponía de mucho tiempo para dedicarle.

## Entrenamiento
### Largo de dataset
Entrené el modelo con 7 canciones de Bryant Myers, alrededor de 20 minutos de voz:

    1. Bryant myers
    2. En que pais
    3. Pa pasar el rato
    4. Un ratito mas
    5. Vamos a vernos
    6. Viejos tiempos
    7. Volvamos a hablar

La cancion que canto bryant myers es una cancion de emilia mernes mas especificamente [iconic](https://www.youtube.com/watch?v=cYOdk3SSslQ) del album mp3.


### Tiempo de entrenamiento
El entrenamiento llevó 54 minutos con los siguientes parámetros:

Frecuencia de guardado: 20
Cantidad de épocas: 300

## Inferencia
Realicé la inferencia una sola vez, ya que consideré que los resultados eran bastante aceptables, aunque no perfectos. La operación no tomó más de 2-3 minutos. La mezcla final la realicé en Audacity.

## Conclusiones sobre el modelo
En mi evaluación personal del modelo que desarrollé, identifico la necesidad de un conjunto de datos más limpio para mejorar la calidad de la generación de voces. Tanto el conjunto de datos como la pista utilizada para la inferencia presentaban cierta reverberación, lo que afectó la precisión del modelo. A pesar de seleccionar canciones con autotune, lo que complica la separación de instrumentos y efectos respecto a la voz real de la artista, considero que el rendimiento fue bastante aceptable.

Uno de los aspectos notables es que las notas de voz generadas por mi modelo tienden a ser más graves en comparación con las de Emilia. Esto podría ser una área de mejora para futuras iteraciones del modelo, ya que la fidelidad en la reproducción de la entonación es fundamental para lograr una mayor autenticidad en la generación de voces.

En resumen, a pesar de las limitaciones detectadas, estoy satisfecho con los resultados obtenidos hasta el momento. Continuaré explorando mejoras en el conjunto de datos y ajustes en los parámetros del modelo para perfeccionar aún más la calidad de la generación vocal.

## Eticas y legales

### Consideraciones Éticas:
1. Suplantacion de identidad:

Imitando voces y estilos, podemos dar lugar a la suplantación de identidad.

2. Confianza en la informacion que vemos en internet:

Hay mucha gente que se cree todo lo que ve en internet, entonces estamos difuminando la línea entre lo auténtico y lo artificial.

3. Pocos requisitos para la creacion

Es muy accesible para todos y es muy fácil de usar.

### Consideraciones legales:
1. Derechos de autor

Por lo general, la mayoría de las canciones tienen derechos de autor, por lo cual el uso sin pago de derechos puede terminar en problemas legales.

2. Fraudes

Hubo muchos fraudes y ventas de contenido como contenido original y creado naturalmente que realmente fue creado por IA.

### Conclusion
La mezcla de IA y música trae problemas serios que hay que considerar antes de crear y difundir. Todavía es algo que está muy verde pero que con el tiempo mejorará en términos de regulación de uso.

## Link del drive con los datos + el dataset

[Carpeta de project main + dataset con pistas](https://drive.google.com/drive/folders/17T53Dy_wZd0y06_9VuQv1aqD8SdAPvVj?usp=drive_link)

