'''
Kirjoita ohjelma yleisin_kirjain.py, joka kysyy käyttäjältä merkkijonoa, ja
tulostaa sen yksittäisen kirjaimen, joka esiintyy annetussa merkkijonossa
useammin kuin mikään muu kirjain.

Tehtävässä käytettyjä rakenteita:

Toistorakenne
* merkkijonon count-metodi tai oma vastaava funktio
* "Sopivimman säilyttäjä"
* Sanakirja
* Bonus: Counter-luokka
* max-funktio ja key-parametri
'''

syote = 'lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas'
yleisin_kirjain = syote[0]

for kirjain in syote:
    maara = syote.count(kirjain)
    if maara > syote.count(yleisin_kirjain):
        yleisin_kirjain = kirjain

print(f'Yleisin kirjain on {yleisin_kirjain}.')
