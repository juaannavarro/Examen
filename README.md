# Examen
Mi dirección para el repositorio del examen es la siguiente: https://github.com/juaannavarro/Examen

El examen trata de 2 ejercicios:

# 1 Juego del minion
El primero de ellos consiste en crear un juego donde Kevin y Stuart juegan uno en contra del otro. El objetivo del juego será escribir una palabra y con esa palabra Stuart puntuará todas las palabras formadas a partir de esa que empiecen por consonante y Kevin lo hará con las que empiecen por vocal. El que tenga mayor puntuación ganará y para ellos he creado el siguiente código:
<img width="388" alt="Captura de pantalla 2021-12-14 a las 11 38 34" src="https://user-images.githubusercontent.com/91721668/145982676-4c24cef8-8b6f-45a4-aa27-a7c616b82867.png">




#Inicio

```
def juego_del_minion(s):
    
    puntuacionStuart=0
    puntuacionKevin=0
    vocales="AEIOU"
    s=s.upper()
    
    for i in range (len(s)):
        if s[i] not in vocales:
            puntuacionStuart=puntuacionStuart+(len(s)-i)
        else:
            puntuacionKevin=puntuacionKevin+(len(s)-i)
    
    if puntuacionStuart>puntuacionKevin:
        print("Ha ganado Stuart  ", puntuacionStuart)
    elif puntuacionStuart<puntuacionKevin:
        print("Ha ganado Kevin ", puntuacionKevin)
    else:
        print("Empate ")

if __name__ == '__main__':
    
    
    s=input("Elija una palabra: ")
    juego_del_minion(s)
#Fin

# 2 Torres Verticales
El segundo de ellos es un juego que se juega entre dos jugadores que realizan movimientos por turnos hasta que uno de ellos no puede realizar ningún movimiento. El jugador que no puede hacer un movimiento pierde el juego y el otro jugador es declarado ganador.
Las únicas piezas que se utilizan en el juego son las torres. Una torre en HackerChess se mueve
solo verticalmente, lo que significa que nunca deja una columna a la que pertenece. Además,
en un solo movimiento, una torre atraviesa cualquier número de casillas desocupadas.
Tenga en cuenta que no hay capturas en HackerChess, dos torres no pueden ocupar la misma
celda y una torre no puede saltar sobre otra torre. Cada jugador tiene exactamente una torre
en cada una de las columnas del tablero.
Dada la posición inicial de las torres y sabiendo que el segundo jugador hace el primer
movimiento, decide quién ganará el juego si ambos jugadores juegan de manera óptima.
<img width="311" alt="Captura de pantalla 2021-12-14 a las 11 48 02" src="https://user-images.githubusercontent.com/91721668/145984144-1f093058-bdd0-4630-be8e-f2bef703e0e1.png">



Para ello hemos creado el siguiente código:

import math
import os
import random
import re
import sys
import pprint

def verticalRooks(r1, r2):
    winner=''
    chess=[]
    for i in range(len(r1)):
        fila = []
        for j in range(len(r1)):
            if r1[j]==i+1:
                fila.append('T1')
            elif r2[j]==i+1:
                fila.append('T2')
            else:
                fila.append(' ')
        chess.append(fila)
    pprint.pprint(chess)
    print
    jugador_1 = 'T1'
    jugador_2 = 'T2'
    jugador=jugador_2
    while True:
        movimiento=False
        for i in range(len(r1)):
            for j in range(len(r1)):
                if chess[i][j]==jugador:
                    if i-1 > 0 and chess[i-1][j]==' ':
                        print('el jugador '+jugador+' mueve a posicion ('+str(i-1)+','+str(j)+')')
                        chess[i-1][j]=jugador
                        chess[i][j]= ' '  
                        movimiento = True
                        if (jugador == jugador_2):
                            jugador=jugador_1
                        else:
                            jugador=jugador_2
                        break
                    elif i+1 < len(r1) and chess[i+1][j]==' ':
                        print('el jugador '+jugador+' mueve a posicion ('+str(i+1)+','+str(j)+')')
                        chess[i+1][j]=jugador
                        chess[i][j]= ' ' 
                        movimiento = True
                        if (jugador == jugador_2):
                            jugador=jugador_1
                        else:
                            jugador=jugador_2
                        break
            if movimiento==True:
                break
        if movimiento==True:
            continue
        elif movimiento==False:
            print('No es posible realizar más movimientos al jugador '+jugador)
            if (jugador == jugador_1):
                winner = 'player-2'
            else:
                winner = 'player-1'
            break

    print('ganador '+winner)
    return winner

if __name__ == '__main__':
    fptr = open('prueba', 'w')

    t = int(input("Introduce numeros del 1 al 3: ").strip())
    while True:
        if t<1 and t>3:
            print("Vuelva a intentarlo: ")
            break
        else:
            print("Introduce otro numero: ")
            break
    for t_itr in range(t):
        n = int(input().strip())

        r1 = []

        for _ in range(n):
            r1_item = int(input().strip())
            r1.append(r1_item)

        r2 = []

        for _ in range(n):
            r2_item = int(input().strip())
            r2.append(r2_item)

        result = verticalRooks(r1, r2)

        fptr.write(result + '\n')

    fptr.close()


