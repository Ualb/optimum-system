## Script de optimización de objetivos vs alternativas

El algoritmo da una puntuación a las alternativas para el cumplimiento de una 
serie de objetivos, mejor dicho, este se encarga de valuar las mejores opciones
de entre las alternativas disponibles.

Muy útil para ocasiones cuando se tienen muchas alternativas y estas suelen ser muy
similares o cuando simplemente existen muchas alternativas.

Se debe considerar que se han seleccionado como variables categoricas de puntuación
al valor de K, el costo de la alternativa y al impacto que esta pueda tener.

En el caso de k y el costo de la alternativa, está fácilmente descrita en la
matriz de optimización de objetivos y alternativas, sin embargo, para la variable
de impacto se aconseja seguir el siguiente método: Valuar el impacto según
las consecuencias positivas de la alternativa menos las consecuencias negativas.

Existen ocasiones donde se daría mayor valor al costo y al impacto más que al
valor de K, en esos casos sólo basta con modificar las variables `wieght_cost`,
`wieght_impact` o `wieght_k` definidas previamente como: 2, 1, 1 correspondientemente.

Para hacer andar el script se necesita que se agrege un `data.json` el cual debe 
albergar todas las alternativas con su detalle totalmente numérico, siendo este:

- id
- k
- impact
- cost