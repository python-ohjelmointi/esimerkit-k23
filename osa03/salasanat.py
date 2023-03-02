from random import choice

KIRJAIMET = 'abcdefghijklmnopqrstuvwxyzåäö'
NUMEROT = '0123456789'
ERIKOISMERKIT = '!#¤%&/()=?`'

KAIKKI = KIRJAIMET + KIRJAIMET.upper() + NUMEROT + ERIKOISMERKIT


def luo_salasana(pituus):
    '''
    Luo ja palauttaa satunnaisen salasanan.
    '''
    pituus = max(32, pituus)
    salasana = ''

    while len(salasana) < pituus:
        salasana += choice(KAIKKI)

    return salasana
