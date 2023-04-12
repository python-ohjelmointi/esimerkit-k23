# https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple

Paivamaara = namedtuple("Paivamaara", "vuosi kk paiva")

alkuaika = Paivamaara(2023, 4, 12)
loppuaika = Paivamaara(2023, 5, 1)

# namedtuple mahdollistaa sen, että käytämme indeksien sijasta nimiä:
if alkuaika.vuosi > loppuaika.vuosi:
    pass

# vrt. indeksillä. Nyt [0] tarkoittaa vuotta:
if alkuaika[0] > loppuaika[0]:
    pass


print(alkuaika)
print(loppuaika)

print(alkuaika[0], alkuaika.vuosi)
print(alkuaika[1], alkuaika.kk)
