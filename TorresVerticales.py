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


