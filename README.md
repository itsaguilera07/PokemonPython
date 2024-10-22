# Juego de Entrenadores - Python Console Game

Este es un sencillo juego de consola en Python en el que debes moverte en un mapa esquivando obstáculos y derrotando entrenadores representados como símbolos `$`. El personaje del jugador es representado por el símbolo `@`.

## Requisitos

- Python 3.x
- Librería `readchar` (puedes instalarla ejecutando `pip install readchar`)

## Cómo jugar

1. Ejecuta el archivo Python.
2. Usa las teclas de dirección `W`, `A`, `S`, `D` para moverte en el mapa:
   - `W`: Moverse hacia arriba.
   - `S`: Moverse hacia abajo.
   - `A`: Moverse hacia la izquierda.
   - `D`: Moverse hacia la derecha.
   - `Q`: Salir del juego.
3. Esquiva los obstáculos:
   - `T`: Árboles.
   - `*`: Rocas.
   - `~`: Agua.
4. Derrota a los entrenadores (`$`) al moverte sobre ellos.
5. El número de entrenadores derrotados se mostrará en la parte inferior de la pantalla.

## Objetivo

El objetivo del juego es derrotar a todos los entrenadores moviéndote estratégicamente por el mapa sin chocar con los obstáculos.

## Estructura del mapa

El mapa es definido por una matriz de caracteres. El código crea una representación visual del mismo y coloca al azar un número de entrenadores en posiciones aleatorias.

```text
TTTTTTTTTTTTTTT
T     *       T
T  TTTTTT     T
T     ~~~     T
T             T
T  T          T
T     *       T
T  TTTTTTTT   T
T             T
T             T
T  TTTTTTTTTT T
T             T
T             T
T  TTTTTTTT   T
T             T
TTTTTTTTTTTTTTT
