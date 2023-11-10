#

## Computadoras Vs Computacion

### Algoritmo
El conect
pto intuitivo de algoritmo lo tenemos practicamente todos.
Es una serie finita de pasos para resolver un problema.
Tiene 3 caracteriticas:
1. Exacto Ya que si se corre multiples veces con los mismos datos debe dar el mismo resultado
2. Finito: Ya que debe terminar en algun momento.
3. Preciso: Ya que va corriendo paso a paso hasta terminar de recorrer el algoritmo

Caracteristicas:
1. Entrada: Definir que necesita el algoritmo
2. Saluda: Definir lo que produce
3. No ambiguo: Explicito siempre sabe que comando ejecutar
4. Finito: Tiene numero finito de pasos
5. Correcto: Hace lo que se supone que debe hacer, la solucion es correcta
6. Efectividad: Cada instruccion se completa en tiempo finito. Y debe ser suficientemente basica como para ser ejecutada por cualquier persona usando papel y lapiz
7. General: Debe ser Lo suficientemente general como para contemplar todos los casos de entrada.

### Algoritmo Vs Problemas Vs Programas
- Un algoritmo es un metodo o proceso seguido para resolver un problema
- Un problema es una funcion o asociacion de entradas con salidas.
- Un programa es una instanciacion de una lgoritmo en un programa de programacion

### Resolucion de problemas
La fase de resolucion de problemas tiene 3 etapas:
1. Analisis de alternativas y seleccion de la solucion
2. Especificacion detallada del procedimiento solucion
3. Adopcion o utilizacion de una herramienta para su implementacion si es que es necesaria.

## Divide y venceras
Muchos algoritmos son recursivos, osea que se llaman asi mismo para resolver subproblemas mas pequeños
La tecnica dive y venceras, nos dice que tenemosq ue generar algoritmos recursivos para resolver una amplia variedad de problemas.
Como:
1. Agarro el problema y lo divido
2. Busco una solucion para cada pedazo de problema
3. y luego uno toda la solucion


Necesitamos identificar:
1. Funcion Caso base que verifique si estamos en caso base
2. funcion resolver que le de la solucion al caso base
3. Funcion dividir que nos divida el problema

Para aplicar la estrategia necesitamos 3 condiciones:
1. Cuales son nuestros casos base cuando resolvemos el problema sin necesidad de dividir.
2. Tiene que ser posible el caso en subcasos y recomponer las solcuiones parciales de forma eficiente.
3. Los subcasos deben ser aproximadamente del mismo tamaño

## Algoritmo voraces
Algortimos avidos o voraces(Greedy Algorithms) son algoritmos que toman decisiones de corto alcance,
basadas en informacion inmediatamente disponible, sin importar consecuencias futuras.

Suelen ser simples y se suelen emplear para problemas de optimizacion.
- Conjunto o lista de candidatos
- COnjunto de decisiones ya tomadas
- Una funcion que determina si los candidatos son o no solucion al problema
- Una funcion si determina que es la solucion optima

