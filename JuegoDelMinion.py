def juego_del_minion(s):
    puntuacionStuart=0
    puntuacionKevin=0
    vocales="AEIOU"
    mayusculas=s.upper()
    
    for i in range (len(s)):
        if s[i] not in vocales:
            puntuacionStuart=puntuacionStuart+len(s[i])
        else:
            puntuacionKevin=puntuacionKevin+len(s[i])
    
    if 
if __name__ == '__main__':
    s=input("Elija una palabra: ")
    juego_del_minion(s)