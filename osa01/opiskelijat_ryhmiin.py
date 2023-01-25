'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

import math

opiskelijoita = int(input('Montako opiskelijaa? '))
ryhmakoko = int(input('Mikä on ryhmän koko? '))
ryhmia = math.ceil(opiskelijoita / ryhmakoko)

print(f'Ryhmien määrä: {ryhmia}')
