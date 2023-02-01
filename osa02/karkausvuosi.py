'''
Saat tutkia ja muokata tätä esimerkkikoodia harjoitustehtävän idean ymmärtämiseksi
ja asioiden opettelemiseksi, mutta koodin kopiointi tehtävän ratkaisuun on kielletty.
'''

# 2011 ei ole, 2020 on, 1800 ei ole, 2000 on
vuosi = 2011

jaollinen_4 = vuosi % 4 == 0
jaollinen_100 = vuosi % 100 == 0
jaollinen_400 = vuosi % 400 == 0

if jaollinen_4 and (not jaollinen_100 or jaollinen_400):
    print(f'vuosi {vuosi} on karkausvuosi')
else:
    print(f'vuosi {vuosi} ei ole karkausvuosi')

# and       => molemmat tosi
# not and   => kumpi tahansa tai molemmat epätosi

# or        => kumpi tahansa tosi
# not or    => molemmat epätosia
