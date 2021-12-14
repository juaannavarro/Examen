# Examen
Mi dirección para el repositorio del examen es la siguiente: https://github.com/juaannavarro/Examen

El examen trata de 2 ejercicios:

# 1 Juego del minion
El primero de ellos consiste en crear un juego donde Kevin y Stuart juegan uno en contra del otro. El objetivo del juego será escribir una palabra y con esa palabra Stuart puntuará todas las palabras formadas a partir de esa que empiecen por consonante y Kevin lo hará con las que empiecen por vocal. El que tenga mayor puntuación ganará y para ellos he creado el siguiente código:
<img width="388" alt="Captura de pantalla 2021-12-14 a las 11 38 34" src="https://user-images.githubusercontent.com/91721668/145982676-4c24cef8-8b6f-45a4-aa27-a7c616b82867.png">




#Inicio


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
Para ello hemos creado el siguiente código:




