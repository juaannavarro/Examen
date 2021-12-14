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