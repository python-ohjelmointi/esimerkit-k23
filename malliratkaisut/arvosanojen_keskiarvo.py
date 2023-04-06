'''
Toteuta funktio arvosanojen_keskiarvo, joka saa parametrinaan listan
kokonaislukuja, ja palauttaa niiden keskiarvon. Erikoisuutena arvosanojen
keskiarvoja laskettaessa nollat tulee jättää huomioimatta. Jos siis funktiolle
annetaan lista, joka sisältää arvot [1, 0, 2, 0], lasketaan keskiarvo vain
nollasta poikkeavista arvoista eli 1 ja 2.

Tehtävässä käytettyjä rakenteita:
* summan kokoaminen ja nollien laskeminen
* sum-funktio, count-funktio, jne..
* listan "filtteröinti"
* from statistics import mean
'''


def arvosanojen_keskiarvo(arvosanat: list) -> float:
    '''
    Saa parametrinaan listan kokonaislukuja, ja palauttaa niiden keskiarvon.
    Erikoisuutena arvosanojen keskiarvoja laskettaessa nollat tulee jättää
    huomioimatta.
    '''
    summa = 0
    nollasta_poikkeavat = 0
    for arvosana in arvosanat:
        if arvosana > 0:
            summa += arvosana
            nollasta_poikkeavat += 1

    return summa / nollasta_poikkeavat
