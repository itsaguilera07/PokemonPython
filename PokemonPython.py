import os
import time
from fileinput import close

import readchar
import random

# Definición del mapa de obstáculos utilizando un string multilínea
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

# Convertir el mapa de obstáculos a una lista de listas para facilitar el acceso a las posiciones
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

# Posiciones en la lista para coordenadas
POST_X = 1
POST_Y = 0

# Longitudes del mapa basado en la definición de obstáculos
MAP_HEIGH = len(obstacle_definition)
MAP_WIDTH = len(obstacle_definition[0])

# Número total de objetos (entrenadores) a crear
NUM_OBJECTS = 5

# Lista para almacenar las posiciones de los objetos creados
MAP_OBJECTS = []

# Contador de entrenadores derrotados
COACH_DEFEATED = 0

# Posición inicial del usuario en el mapa
MY_POSITION = [5, 1]

# Lista de tipos de entrenadores que se pueden crear
TIPO_ENTRENADOR = ["Agua", "Fuego", "Tierra", "Planta", "Fantasma"]

# Inicialización de la vida de los Pokémon
Arceus_inicial_vida = 80
Greninja_inicial_vida = 80
Charizard_inicial_vida = 80
Torterra_inicial_vida = 80
Venusaur_inicial_vida = 80
Gengar_inicial_vida = 80

# Variables que guardan la vida actual de los Pokémon
Arceus_vida = Arceus_inicial_vida
Greninja_vida = Greninja_inicial_vida
Charizard_vida = Charizard_inicial_vida
Torterra_vida = Torterra_inicial_vida
Venusaur_vida = Venusaur_inicial_vida
Gengar_vida = Gengar_inicial_vida

# Tamaño de la barra de vida para visualización
Tam_barra_vida = 20

# Bucle para crear objetos (entrenadores) en el mapa
while len(MAP_OBJECTS) < NUM_OBJECTS:
    # Genera posiciones aleatorias dentro de los límites del mapa
    new_object = [random.randint(2, MAP_HEIGH - 2), random.randint(2, MAP_WIDTH - 2)]

    # Verifica que la posición generada no esté ocupada por obstáculos o entrenadores
    if obstacle_definition[new_object[POST_Y]][new_object[POST_X]] not in ["T", "*", "~"] and new_object not in [entrenador["pos"] for entrenador in MAP_OBJECTS]:
        # Selecciona aleatoriamente un tipo de entrenador
        tipos_entrenadores = random.choice(TIPO_ENTRENADOR)
        # Asegura que el tipo de entrenador no se repita
        if tipos_entrenadores not in [entrenador["tipo"] for entrenador in MAP_OBJECTS]:
            # Agrega el nuevo entrenador al mapa
            MAP_OBJECTS.append({"pos": new_object, "tipo": tipos_entrenadores})

while True:
    # Mensaje al vencer a todos los entrenadores
    if COACH_DEFEATED == 5:
        os.system('cls')
        print("-" * 60)
        print("Lograstes vencer a todos los entrenadores")
        print("-" * 60)
        break


    # Dibuja el mapa en la consola
    print("+" + "-" * MAP_HEIGH * 3 + "+")
    for cordinate_x in range(MAP_WIDTH):
        print("|", end="")
        for cordinate_y in range(MAP_HEIGH):
            char_to_draw = " "

            # Dibuja el personaje, obstáculos y entrenadores
            if [cordinate_y, cordinate_x] == MY_POSITION:
                char_to_draw = "@"  # Personaje
            elif obstacle_definition[cordinate_y][cordinate_x] == "T":
                char_to_draw = "T"  # Árboles
            elif obstacle_definition[cordinate_y][cordinate_x] == "*":
                char_to_draw = "*"  # Rocas
            elif obstacle_definition[cordinate_y][cordinate_x] == "~":
                char_to_draw = "~"  # Agua
            elif [cordinate_y, cordinate_x] in [entrenador["pos"] for entrenador in MAP_OBJECTS]:
                char_to_draw = "$"  # Entrenadores

            print(f" {char_to_draw} ", end="")
        print("|")

    print("+" + "-" * MAP_HEIGH * 3 + "+")
    print("Entrenadores derrotados: " + str(COACH_DEFEATED))
    barra_de_vida_Arceus = int(Arceus_vida * Tam_barra_vida / Arceus_inicial_vida)
    print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus, " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida, Arceus_inicial_vida))
    print("\n")

    # Movimiento del jugador basado en la entrada del teclado
    POSICION_USUARIO = readchar.readchar().upper()
    if POSICION_USUARIO == "W" and obstacle_definition[MY_POSITION[POST_Y]][MY_POSITION[POST_X] - 1] not in ["T", "*", "~"]:
        MY_POSITION[POST_X] -= 1  # Mover hacia arriba
    elif POSICION_USUARIO == "S" and obstacle_definition[MY_POSITION[POST_Y]][MY_POSITION[POST_X] + 1] not in ["T", "*", "~"]:
        MY_POSITION[POST_X] += 1  # Mover hacia abajo
    elif POSICION_USUARIO == "A" and obstacle_definition[MY_POSITION[POST_Y] - 1][MY_POSITION[POST_X]] not in ["T", "*", "~"]:
        MY_POSITION[POST_Y] -= 1  # Mover hacia la izquierda
    elif POSICION_USUARIO == "D" and obstacle_definition[MY_POSITION[POST_Y] + 1][MY_POSITION[POST_X]] not in ["T", "*", "~"]:
        MY_POSITION[POST_Y] += 1  # Mover hacia la derecha
    elif POSICION_USUARIO == "Q":
        break  # Salir del juego


    for entrenador in MAP_OBJECTS:
        if MY_POSITION == entrenador["pos"]:
            TIPO_ENTRENADOR = entrenador["tipo"]

            # Verifica si el tipo de entrenador es "Agua"
            if TIPO_ENTRENADOR == "Agua":

                # -----------------------------------------
                # Entrenador tipo Agua
                # -----------------------------------------

                print("\n" + "-" * 60)
                print("Te has encontrado con el entrenador de tipo Agua")

                # Ciclo de batalla entre Arceus y Greninja
                while Arceus_vida > 0 and Greninja_vida > 0:

                    os.system("cls")  # Limpia la consola
                    ataque_pokemon = random.randint(1, 4)  # Selección aleatoria de ataque de Greninja

                    print("-" * 60)
                    print("Es el turno de atacar de Greninja")
                    barra_de_vida_Greninja = int(Greninja_vida * Tam_barra_vida / Greninja_inicial_vida)
                    print("Greninja: [{}{}][{}/{}]".format("-" * barra_de_vida_Greninja,
                                                           " " * (Tam_barra_vida - barra_de_vida_Greninja),
                                                           Greninja_vida, Greninja_inicial_vida))
                    print("-" * 60)

                    # Determina el ataque que usará Greninja y reduce la vida de Arceus
                    if ataque_pokemon == 1:
                        print("El Pokémon atacó con: Hidrobomba - (PS - 30)\n")
                        Arceus_vida -= 30
                    elif ataque_pokemon == 2:
                        print("El Pokémon atacó con: Surf - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 3:
                        print("El Pokémon atacó con: Pulso Umbrío - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 4:
                        print("El Pokémon atacó con: Tijera X - (PS - 20)\n")
                        Arceus_vida -= 20

                    # Verifica si Arceus ha sido derrotado
                    if Arceus_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Greninja ganó la partida")
                        print("-" * 60)
                        Arceus_vida = 0
                        print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                             " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                             Arceus_inicial_vida))
                        print("-" * 60)
                        exit()  # Termina el juego

                    Arceus_ataque = None  # Reinicia la variable del ataque de Arceus

                    print("-" * 60)
                    print("Es el turno de atacar de Arceus")
                    barra_de_vida_Arceus = int(Arceus_vida * Tam_barra_vida / Arceus_inicial_vida)
                    print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                         " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                         Arceus_inicial_vida))
                    print("-" * 60)

                    # Muestra las opciones de ataque de Arceus
                    print("Opción A - Corte Fuego")
                    print("Opción B - Puño Trueno")
                    print("Opción C - Bola Sombra")
                    print("Opción D - Poder divino(?)")

                    # Ciclo para seleccionar el ataque de Arceus
                    while Arceus_ataque not in ["A", "B", "C", "D"]:
                        Arceus_ataque = input("¿Qué ataque debe hacer Arceus? ").upper()
                        if Arceus_ataque == "A":
                            print("El Pokémon atacó con: Corte Fuego - (PS - 80)\n")
                            Greninja_vida -= 40
                            time.sleep(3)
                        elif Arceus_ataque == "B":
                            print("El Pokémon atacó con: Puño Trueno - (PS - 20)\n")
                            Greninja_vida -= 20
                            time.sleep(3)
                        elif Arceus_ataque == "C":
                            print("El Pokémon atacó con: Bola Sombra - (PS - 20)\n")
                            Greninja_vida -= 25
                            time.sleep(3)
                        elif Arceus_ataque == "D":
                            print("El Pokémon atacó con: Poder divino - (PS - ?)")
                            poder_divino = int(random.randint(1, 3))  # Selección aleatoria del efecto de Poder divino
                            if poder_divino == 1:
                                print("Poder divino: Furia de los caídos - (PS - 50)\n")
                                Greninja_vida -= 50
                                time.sleep(3)
                            elif poder_divino == 2:
                                print("Poder divino: Mismo destino - (Resta a tu vida - 40 PS)\n")
                                Arceus_vida -= 40
                                time.sleep(3)
                            elif poder_divino == 3:
                                print("Poder divino: Castigo de los dioses - (PS - 80)\n")
                                Greninja_vida -= 80
                                time.sleep(3)

                    # Verifica si Greninja ha sido derrotado
                    if Greninja_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Arceus ganó la partida")
                        print("Arceus Utilizo cura sagrada")
                        print("Arceus recupero toda la vida")
                        Arceus_vida = 80  # Restablece la vida de Arceus
                        print("-" * 60)
                        Greninja_vida = 0
                        print("Greninja: [{}{}][{}/{}]".format("-" * barra_de_vida_Greninja,
                                                               " " * (Tam_barra_vida - barra_de_vida_Greninja),
                                                               Greninja_vida, Greninja_inicial_vida))
                        print("-" * 60)
                        MAP_OBJECTS.remove(entrenador)  # Elimina el entrenador derrotado de la lista
                        COACH_DEFEATED += 1  # Incrementa el contador de entrenadores derrotados
                        time.sleep(4)
                        break  # Termina el bucle de batalla

                    os.system("cls")  # Limpia la consola para la siguiente ronda de batalla



            # Verifica si el tipo de entrenador es "Fuego"
            elif TIPO_ENTRENADOR == "Fuego":

                # -----------------------------------------

                # Entrenador tipo Fuego

                # -----------------------------------------

                print("\n" + "-" * 60)
                print("Te has encontrado con el entrenador de tipo Fuego")

                # Ciclo de batalla entre Arceus y Charizard
                while Arceus_vida > 0 and Charizard_vida > 0:

                    os.system("cls")  # Limpia la consola
                    ataque_pokemon = random.randint(1, 4)  # Selección aleatoria de ataque de Charizard
                    print("-" * 60)
                    print("Es el turno de atacar de Charizard")
                    barra_de_vida_Charizard = int(Charizard_vida * Tam_barra_vida / Charizard_inicial_vida)
                    print("Charizard: [{}{}][{}/{}]".format("-" * barra_de_vida_Charizard,
                                                            " " * (Tam_barra_vida - barra_de_vida_Charizard),
                                                            Charizard_vida, Charizard_inicial_vida))
                    print("-" * 60)

                    # Determina el ataque que usará Charizard y reduce la vida de Arceus
                    if ataque_pokemon == 1:
                        print("El Pokémon atacó con: Llamarada - (PS - 30)\n")
                        Arceus_vida -= 30
                    elif ataque_pokemon == 2:
                        print("El Pokémon atacó con: Cuerpo Llama - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 3:
                        print("El Pokémon atacó con: Giga Impacto - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 4:
                        print("El Pokémon atacó con: Viento Fuego - (PS - 20)\n")
                        Arceus_vida -= 20

                    # Verifica si Arceus ha sido derrotado
                    if Arceus_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Charizard ganó la partida")
                        print("-" * 60)
                        Arceus_vida = 0
                        print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                             " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                             Arceus_inicial_vida))
                        print("-" * 60)
                        exit()  # Termina el juego

                    Arceus_ataque = None  # Reinicia la variable del ataque de Arceus
                    print("-" * 60)
                    print("Es el turno de atacar de Arceus")
                    barra_de_vida_Arceus = int(Arceus_vida * Tam_barra_vida / Arceus_inicial_vida)
                    print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                         " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                         Arceus_inicial_vida))
                    print("-" * 60)
                    # Muestra las opciones de ataque de Arceus

                    print("Opción A - Corte Fuego")
                    print("Opción B - Puño Trueno")
                    print("Opción C - Bola Sombra")
                    print("Opción D - Poder divino(?)")

                    # Ciclo para seleccionar el ataque de Arceus

                    while Arceus_ataque not in ["A", "B", "C", "D"]:
                        Arceus_ataque = input("¿Qué ataque debe hacer Arceus? ").upper()
                        if Arceus_ataque == "A":
                            print("El Pokémon atacó con: Corte Fuego - (PS - 80)\n")
                            Charizard_vida -= 40
                            time.sleep(3)
                        elif Arceus_ataque == "B":
                            print("El Pokémon atacó con: Puño Trueno - (PS - 20)\n")
                            Charizard_vida -= 20
                            time.sleep(3)
                        elif Arceus_ataque == "C":
                            print("El Pokémon atacó con: Bola Sombra - (PS - 20)\n")
                            Charizard_vida -= 25
                            time.sleep(3)
                        elif Arceus_ataque == "D":
                            print("El Pokémon atacó con: Poder divino - (PS - ?)")
                            poder_divino = int(random.randint(1, 3))  # Selección aleatoria del efecto de Poder divino
                            if poder_divino == 1:
                                print("Poder divino: Furia de los caídos - (PS - 50)\n")
                                Charizard_vida -= 50
                                time.sleep(3)
                            elif poder_divino == 2:
                                print("Poder divino: Mismo destino - (Resta a tu vida - 40 PS)\n")
                                Arceus_vida -= 40
                                time.sleep(3)
                            elif poder_divino == 3:
                                print("Poder divino: Castigo de los dioses - (PS - 80)\n")
                                Charizard_vida -= 80
                                time.sleep(3)

                    # Verifica si Charizard ha sido derrotado
                    if Charizard_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Arceus ganó la partida")
                        print("Arceus Utilizo cura sagrada")
                        print("Arceus recupero toda la vida")
                        Arceus_vida = 80  # Restablece la vida de Arceus
                        print("-" * 60)
                        Charizard_vida = 0

                        print("Charizard: [{}{}][{}/{}]".format("-" * barra_de_vida_Charizard,
                                                                " " * (Tam_barra_vida - barra_de_vida_Charizard),
                                                                Charizard_vida, Charizard_inicial_vida))

                        print("-" * 60)
                        MAP_OBJECTS.remove(entrenador)  # Elimina el entrenador derrotado de la lista
                        COACH_DEFEATED += 1  # Incrementa el contador de entrenadores derrotados
                        time.sleep(4)
                        break  # Termina el bucle de batalla
                    os.system("cls")  # Limpia la consola para la siguiente ronda de batalla


            # Verifica si el tipo de entrenador es "Tierra"
            elif TIPO_ENTRENADOR == "Tierra":

                # -----------------------------------------

                # Entrenador tipo Tierra

                # -----------------------------------------

                print("\n" + "-" * 60)
                print("Te has encontrado con el entrenador de tipo Tierra")

                # Ciclo de batalla entre Arceus y Torterra
                while Arceus_vida > 0 and Torterra_vida > 0:

                    ataque_pokemon = random.randint(1, 4)  # Selección aleatoria de ataque de Torterra
                    print("-" * 60)
                    print("Es el turno de atacar de Torterra")
                    barra_de_vida_Torterra = int(Torterra_vida * Tam_barra_vida / Torterra_inicial_vida)
                    print("Torterra: [{}{}][{}/{}]".format("-" * barra_de_vida_Torterra,
                                                           " " * (Tam_barra_vida - barra_de_vida_Torterra),
                                                           Torterra_vida, Torterra_inicial_vida))
                    print("-" * 60)

                    # Determina el ataque que usará Torterra y reduce la vida de Arceus
                    if ataque_pokemon == 1:
                        print("El Pokémon atacó con: Terremoto - (PS - 30)\n")
                        Arceus_vida -= 30
                    elif ataque_pokemon == 2:
                        print("El Pokémon atacó con: Hoja Afilada - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 3:
                        print("El Pokémon atacó con: Rayo Solar - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 4:
                        print("El Pokémon atacó con: Golpe Rocoso - (PS - 20)\n")
                        Arceus_vida -= 20

                    # Verifica si Arceus ha sido derrotado
                    if Arceus_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Torterra ganó la partida")
                        print("-" * 60)
                        Arceus_vida = 0
                        print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                             " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                             Arceus_inicial_vida))
                        print("-" * 60)
                        exit()  # Termina el juego

                    Arceus_ataque = None  # Reinicia la variable del ataque de Arceus
                    print("-" * 60)
                    print("Es el turno de atacar de Arceus")
                    barra_de_vida_Arceus = int(Arceus_vida * Tam_barra_vida / Arceus_inicial_vida)
                    print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                         " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                         Arceus_inicial_vida))
                    print("-" * 60)

                    # Muestra las opciones de ataque de Arceus
                    print("Opción A - Corte Fuego")
                    print("Opción B - Puño Trueno")
                    print("Opción C - Bola Sombra")
                    print("Opción D - Poder divino(?)")

                    # Ciclo para seleccionar el ataque de Arceus
                    while Arceus_ataque not in ["A", "B", "C", "D"]:
                        Arceus_ataque = input("¿Qué ataque debe hacer Arceus? ").upper()
                        if Arceus_ataque == "A":
                            print("El Pokémon atacó con: Corte Fuego - (PS - 80)\n")
                            Torterra_vida -= 40
                            time.sleep(3)
                        elif Arceus_ataque == "B":
                            print("El Pokémon atacó con: Puño Trueno - (PS - 20)\n")
                            Torterra_vida -= 20
                            time.sleep(3)
                        elif Arceus_ataque == "C":
                            print("El Pokémon atacó con: Bola Sombra - (PS - 20)\n")
                            Torterra_vida -= 25
                            time.sleep(3)
                        elif Arceus_ataque == "D":
                            print("El Pokémon atacó con: Poder divino - (PS - ?)")
                            poder_divino = int(random.randint(1, 3))  # Selección aleatoria del efecto de Poder divino
                            if poder_divino == 1:
                                print("Poder divino: Furia de los caídos - (PS - 50)\n")
                                Torterra_vida -= 50
                                time.sleep(3)
                            elif poder_divino == 2:
                                print("Poder divino: Mismo destino - (Resta a tu vida - 40 PS)\n")
                                Arceus_vida -= 40
                                time.sleep(3)
                            elif poder_divino == 3:
                                print("Poder divino: Castigo de los dioses - (PS - 80)\n")
                                Torterra_vida -= 80
                                time.sleep(3)

                    # Verifica si Torterra ha sido derrotado
                    if Torterra_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Arceus ganó la partida")
                        print("Arceus Utilizo cura sagrada")
                        print("Arceus recupero toda la vida")
                        Arceus_vida = 80  # Restablece la vida de Arceus
                        print("-" * 60)
                        Torterra_vida = 0

                        print("Torterra: [{}{}][{}/{}]".format("-" * barra_de_vida_Torterra,
                                                               " " * (Tam_barra_vida - barra_de_vida_Torterra),
                                                               Torterra_vida, Torterra_inicial_vida))

                        print("-" * 60)
                        MAP_OBJECTS.remove(entrenador)  # Elimina el entrenador derrotado de la lista
                        COACH_DEFEATED += 1  # Incrementa el contador de entrenadores derrotados
                        time.sleep(4)
                        break  # Termina el bucle de batalla
                    os.system("cls")  # Limpia la consola para la siguiente ronda de batalla



            # Verifica si el tipo de entrenador es "Planta"
            elif TIPO_ENTRENADOR == "Planta":

                # -----------------------------------------

                # Entrenador tipo Planta

                # -----------------------------------------

                os.system("cls")
                print("\n" + "-" * 60)
                print("Te has encontrado con el entrenador de tipo Planta")
                # Ciclo de batalla entre Arceus y Venusaur
                while Arceus_vida > 0 and Venusaur_vida > 0:

                    ataque_pokemon = random.randint(1, 4)  # Selección aleatoria de ataque de Venusaur
                    print("-" * 60)
                    print("Es el turno de atacar de Venusaur")
                    barra_de_vida_Venusaur = int(Venusaur_vida * Tam_barra_vida / Venusaur_inicial_vida)
                    print("Venusaur: [{}{}][{}/{}]".format("-" * barra_de_vida_Venusaur,
                                                           " " * (Tam_barra_vida - barra_de_vida_Venusaur),
                                                           Venusaur_vida, Venusaur_inicial_vida))
                    print("-" * 60)

                    # Determina el ataque que usará Venusaur y reduce la vida de Arceus
                    if ataque_pokemon == 1:
                        print("El Pokémon atacó con: Rayo Solar - (PS - 30)\n")
                        Arceus_vida -= 30
                    elif ataque_pokemon == 2:
                        print("El Pokémon atacó con: Drenadoras - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 3:
                        print("El Pokémon atacó con: Hoja Afilada - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 4:
                        print("El Pokémon atacó con: Bomba Lodo - (PS - 20)\n")
                        Arceus_vida -= 20

                    # Verifica si Arceus ha sido derrotado
                    if Arceus_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Venusaur ganó la partida")
                        print("-" * 60)
                        Arceus_vida = 0
                        print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                             " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                             Arceus_inicial_vida))
                        print("-" * 60)
                        exit()  # Termina el juego

                    Arceus_ataque = None  # Reinicia la variable del ataque de Arceus
                    print("-" * 60)
                    print("Es el turno de atacar de Arceus")
                    barra_de_vida_Arceus = int(Arceus_vida * Tam_barra_vida / Arceus_inicial_vida)
                    print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                         " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                         Arceus_inicial_vida))
                    print("-" * 60)

                    # Muestra las opciones de ataque de Arceus
                    print("Opción A - Corte Fuego")
                    print("Opción B - Puño Trueno")
                    print("Opción C - Bola Sombra")
                    print("Opción D - Poder divino(?)")

                    # Ciclo para seleccionar el ataque de Arceus
                    while Arceus_ataque not in ["A", "B", "C", "D"]:
                        Arceus_ataque = input("¿Qué ataque debe hacer Arceus? ").upper()
                        if Arceus_ataque == "A":
                            print("El Pokémon atacó con: Corte Fuego - (PS - 80)\n")
                            Venusaur_vida -= 40
                            time.sleep(3)
                        elif Arceus_ataque == "B":
                            print("El Pokémon atacó con: Puño Trueno - (PS - 20)\n")
                            Venusaur_vida -= 20
                            time.sleep(3)
                        elif Arceus_ataque == "C":
                            print("El Pokémon atacó con: Bola Sombra - (PS - 20)\n")
                            Venusaur_vida -= 25
                            time.sleep(3)
                        elif Arceus_ataque == "D":
                            print("El Pokémon atacó con: Poder divino - (PS - ?)")
                            poder_divino = int(random.randint(1, 3))  # Selección aleatoria del efecto de Poder divino
                            if poder_divino == 1:
                                print("Poder divino: Furia de los caídos - (PS - 50)\n")
                                Venusaur_vida -= 50
                                time.sleep(3)
                            elif poder_divino == 2:
                                print("Poder divino: Mismo destino - (Resta a tu vida - 40 PS)\n")
                                Arceus_vida -= 40
                                time.sleep(3)
                            elif poder_divino == 3:
                                print("Poder divino: Castigo de los dioses - (PS - 80)\n")
                                Venusaur_vida -= 80
                                time.sleep(3)

                    # Verifica si Venusaur ha sido derrotado
                    if Venusaur_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Arceus ganó la partida")
                        print("Arceus Utilizo cura sagrada")
                        print("Arceus recupero toda la vida")
                        Arceus_vida = 80  # Restablece la vida de Arceus
                        print("-" * 60)
                        Venusaur_vida = 0

                        print("Venusaur: [{}{}][{}/{}]".format("-" * barra_de_vida_Venusaur,
                                                               " " * (Tam_barra_vida - barra_de_vida_Venusaur),
                                                               Venusaur_vida, Venusaur_inicial_vida))

                        print("-" * 60)
                        MAP_OBJECTS.remove(entrenador)  # Elimina el entrenador derrotado de la lista
                        COACH_DEFEATED += 1  # Incrementa el contador de entrenadores derrotados
                        time.sleep(4)
                        break  # Termina el bucle de batalla

                    os.system("cls")  # Limpia la consola para la siguiente ronda de batalla


            elif TIPO_ENTRENADOR == "Fantasma":

                # -----------------------------------------
                # Entrenador tipo Fantasma
                # -----------------------------------------

                print("\n" + "-" * 60)
                print("Te has encontrado con el entrenador de tipo Fantasma")

                # Ciclo de batalla entre Arceus y Gengar
                while Arceus_vida > 0 and Gengar_vida > 0:

                    os.system("cls")  # Limpia la consola
                    ataque_pokemon = random.randint(1, 4)  # Selección aleatoria de ataque de Gengar

                    print("-" * 60)
                    print("Es el turno de atacar de Gengar")
                    barra_de_vida_Gengar = int(Gengar_vida * Tam_barra_vida / Gengar_inicial_vida)
                    print("Gengar: [{}{}][{}/{}]".format("-" * barra_de_vida_Gengar,
                                                         " " * (Tam_barra_vida - barra_de_vida_Gengar),
                                                         Gengar_vida, Gengar_inicial_vida))
                    print("-" * 60)

                    # Determina el ataque que usará Gengar y reduce la vida de Arceus
                    if ataque_pokemon == 1:
                        print("El Pokémon atacó con: Bola Sombra - (PS - 30)\n")
                        Arceus_vida -= 30
                    elif ataque_pokemon == 2:
                        print("El Pokémon atacó con: Puño Fuego - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 3:
                        print("El Pokémon atacó con: Maldición - (PS - 15)\n")
                        Arceus_vida -= 15
                    elif ataque_pokemon == 4:
                        print("El Pokémon atacó con: Garra Umbría - (PS - 20)\n")
                        Arceus_vida -= 20

                    # Verifica si Arceus ha sido derrotado
                    if Arceus_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Gengar ganó la partida")
                        print("-" * 60)
                        Arceus_vida = 0
                        print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                             " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                             Arceus_inicial_vida))
                        print("-" * 60)
                        exit()  # Termina el juego

                    Arceus_ataque = None  # Reinicia la variable del ataque de Arceus

                    print("-" * 60)
                    print("Es el turno de atacar de Arceus")
                    barra_de_vida_Arceus = int(Arceus_vida * Tam_barra_vida / Arceus_inicial_vida)
                    print("Arceus: [{}{}][{}/{}]".format("-" * barra_de_vida_Arceus,
                                                         " " * (Tam_barra_vida - barra_de_vida_Arceus), Arceus_vida,
                                                         Arceus_inicial_vida))
                    print("-" * 60)

                    # Muestra las opciones de ataque de Arceus
                    print("Opción A - Corte Fuego")
                    print("Opción B - Puño Trueno")
                    print("Opción C - Bola Sombra")
                    print("Opción D - Poder divino(?)")

                    # Ciclo para seleccionar el ataque de Arceus
                    while Arceus_ataque not in ["A", "B", "C", "D"]:
                        Arceus_ataque = input("¿Qué ataque debe hacer Arceus? ").upper()
                        if Arceus_ataque == "A":
                            print("El Pokémon atacó con: Corte Fuego - (PS - 80)\n")
                            Gengar_vida -= 40
                            time.sleep(3)
                        elif Arceus_ataque == "B":
                            print("El Pokémon atacó con: Puño Trueno - (PS - 20)\n")
                            Gengar_vida -= 20
                            time.sleep(3)
                        elif Arceus_ataque == "C":
                            print("El Pokémon atacó con: Bola Sombra - (PS - 20)\n")
                            Gengar_vida -= 25
                            time.sleep(3)
                        elif Arceus_ataque == "D":
                            print("El Pokémon atacó con: Poder divino - (PS - ?)")
                            poder_divino = int(random.randint(1, 3))  # Selección aleatoria del efecto de Poder divino
                            if poder_divino == 1:
                                print("Poder divino: Furia de los caídos - (PS - 50)\n")
                                Gengar_vida -= 50
                                time.sleep(3)
                            elif poder_divino == 2:
                                print("Poder divino: Mismo destino - (Resta a tu vida - 40 PS)\n")
                                Arceus_vida -= 40
                                time.sleep(3)
                            elif poder_divino == 3:
                                print("Poder divino: Castigo de los dioses - (PS - 80)\n")
                                Gengar_vida -= 80
                                time.sleep(3)

                    # Verifica si Gengar ha sido derrotado
                    if Gengar_vida <= 0:
                        os.system("cls")
                        print("-" * 60)
                        print("Arceus ganó la partida")
                        print("Arceus Utilizo cura sagrada")
                        print("Arceus recupero toda la vida")
                        Arceus_vida = 80  # Restablece la vida de Arceus
                        print("-" * 60)
                        Gengar_vida = 0
                        print("Gengar: [{}{}][{}/{}]".format("-" * barra_de_vida_Gengar,
                                                             " " * (Tam_barra_vida - barra_de_vida_Gengar),
                                                             Gengar_vida, Gengar_inicial_vida))
                        print("-" * 60)
                        MAP_OBJECTS.remove(entrenador)  # Elimina el entrenador derrotado de la lista
                        COACH_DEFEATED += 1  # Incrementa el contador de entrenadores derrotados
                        time.sleep(4)
                        break  # Termina el bucle de batalla

                    os.system("cls")  # Limpia la consola para la siguiente ronda de batalla

    os.system("cls")