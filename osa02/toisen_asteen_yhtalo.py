'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''
from math import sqrt

a = 1
b = 2
c = -8

# b² => b ** 2
# 4ac => 4 * a * c
# 2a => 2 * a
x0 = (-b + sqrt((b ** 2) - (4 * a * c))) / (2 * a)
x1 = (-b - sqrt((b ** 2) - (4 * a * c))) / (2 * a)

print(f'Juuret ovat {x0} ja {x1}')
