import math
import os
import random
import re
import sys

def verticalRooks(r1, r2):
    comienza=2
    for torre1,torre2 in zip(r1, r2):
        distancia_entre_torres= abs(torre2-torre1)
        ganador=" "
        if comienza==2:
            if distancia_entre_torres==1:
                distancia_entre_torres==1
                ganador=" Jugador 1 "
                comienza=2
            else:
                ganador=" Jugador 2 "
                comienza=1
        else:
            if distancia_entre_torres==1:
                ganador=" Jugador 2 "
                comienza=1
            else:
                ganador=" Jugador 1 "
                comienza=2
    if ganador==" Jugador 1 ":
        return "player_1"
    else:
        return "player_2"
    
        

if __name__ == '__main__':
 
 fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
 t = int(input().strip())
 
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