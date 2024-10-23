# Juego de Entrenadores - Python Console Game

Este es un sencillo juego de consola en Python donde los jugadores pueden explorar un mapa, esquivar obstáculos y derrotar entrenadores representados como símbolos `$`. Además, los jugadores pueden enfrentarse en combates de Pokémon, utilizando estrategias para vencer a los oponentes.

## Requisitos

- Python 3.x
- Librería `readchar` (puedes instalarla ejecutando `pip install readchar`)

## Cómo jugar

1. **Ejecuta el archivo Python**: Inicia el juego ejecutando el archivo principal.
2. **Control del personaje**:
   - Usa las teclas de dirección `W`, `A`, `S`, `D` para moverte en el mapa:
     - `W`: Moverse hacia arriba.
     - `S`: Moverse hacia abajo.
     - `A`: Moverse hacia la izquierda.
     - `D`: Moverse hacia la derecha.
     - `Q`: Salir del juego.
3. **Esquiva los obstáculos**:
   - `T`: Árboles.
   - `*`: Rocas.
   - `~`: Agua.
4. **Derrota a los entrenadores**: 
   - Al moverte sobre un entrenador (símbolo `$`), inicias un combate.
5. **Combate de Pokémon**: 
   - Utiliza diferentes ataques y habilidades de tu Pokémon para vencer al Pokémon del entrenador. Los ataques tienen diferentes efectos sobre los puntos de vida (PS).
6. **Objetivo del juego**:
   - El objetivo es derrotar a todos los entrenadores moviéndote estratégicamente por el mapa sin chocar con los obstáculos.

## Estructura del mapa

El mapa es definido por una matriz de caracteres que se utiliza para crear una representación visual. Los entrenadores se colocan en posiciones aleatorias. Aquí hay un ejemplo del mapa:

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
