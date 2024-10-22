import os
import readchar
import random

obstacle_definition = """\
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
TTTTTTTTTTTTTTT\
"""

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

POST_X = 1
POST_Y = 0

MAP_HEIGH = len(obstacle_definition)
MAP_WIDTH = len(obstacle_definition[0])

NUM_OBJECTS = 5
MAP_OBJECTS = []

COACH_DEFEATED = 0

MY_POSITION = [5,1]

while len(MAP_OBJECTS) < NUM_OBJECTS:
    new_object = [random.randint(2, MAP_HEIGH - 2), random.randint(2, MAP_WIDTH - 2)]
    if obstacle_definition[new_object[POST_Y]][new_object[POST_X]] not in ["T", "*", "~",] and new_object not in MAP_OBJECTS:
        MAP_OBJECTS.append(new_object)


while True:
    print("+" + "-" * MAP_HEIGH * 3 + "+")

    for cordinate_x in range(MAP_WIDTH):
        print("|", end="")
        for cordinate_y in range(MAP_HEIGH):
            char_to_draw = " "

            if [cordinate_y, cordinate_x] == MY_POSITION:
                char_to_draw = "@" # Personaje
            elif obstacle_definition[cordinate_y][cordinate_x] == "T":
                char_to_draw = "T" # Arboles
            elif obstacle_definition[cordinate_y][cordinate_x] == "*":
                char_to_draw = "*" # Rocas
            elif obstacle_definition[cordinate_y][cordinate_x] == "~":
                char_to_draw = "~" # Agua
            elif [cordinate_y,cordinate_x] in MAP_OBJECTS:
                char_to_draw = "$" # entrenadores

            print(f" {char_to_draw} ", end="")
        print("|")

    print("+" + "-" * MAP_HEIGH * 3 + "+")
    print("Entrenadores derrotados: " + str(COACH_DEFEATED))

    #Movimiento de jugador
    POSICION_USUARIO = readchar.readchar().upper()
    if POSICION_USUARIO == "W" and obstacle_definition[MY_POSITION[POST_Y]][MY_POSITION[POST_X]- 1] not in ["T", "*", "~"]:
        MY_POSITION[POST_X] -= 1
    elif POSICION_USUARIO == "S" and obstacle_definition[MY_POSITION[POST_Y]][MY_POSITION[POST_X] + 1] not in ["T", "*", "~"]:
        MY_POSITION[POST_X] += 1
    elif POSICION_USUARIO == "A" and obstacle_definition[MY_POSITION[POST_Y] - 1][MY_POSITION[POST_X]] not in ["T", "*", "~"]:
        MY_POSITION[POST_Y] -= 1
    elif POSICION_USUARIO == "D" and obstacle_definition[MY_POSITION[POST_Y] + 1][MY_POSITION[POST_X]] not in ["T", "*", "~"]:
        MY_POSITION[POST_Y] += 1
    elif POSICION_USUARIO == "Q":
        break

    if MY_POSITION in MAP_OBJECTS:
        MAP_OBJECTS.remove(MY_POSITION)
        COACH_DEFEATED += 1

    os.system("cls")