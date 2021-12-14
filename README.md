# Examen
Mi dirección para el repositorio del examen es la siguiente: https://github.com/juaannavarro/Examen

El examen trata de 2 ejercicios:

El primero de ellos consiste en crear un juego donde Kevin y Stuart juegan uno en contra del otro. El objetivo del juego será escribir una palabra y con esa palabra Stuart puntuará todas las palabras formadas a partir de esa que empiecen por consonante y Kevin lo hará con las que empiecen por vocal. El que tenga mayor puntuación ganará y para ellos he creado el siguiente código:





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
