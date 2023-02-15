from random import choice

kirjaimet = 'abcdefghijklmnopqrstuvwxyzåäö'
kirjaimet = kirjaimet + kirjaimet.upper() + '0123456789!"#¤%&/()=?`'

pituus = 64
salasana = ''

while len(salasana) < pituus:
    salasana += choice(kirjaimet)

print(salasana)
