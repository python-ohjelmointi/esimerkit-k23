teksti = 'Hinta on'
hinta = 99.9

# Tapa 1: numero voidaan muuttaa tekstiksi, jolloin + toimii:
print('Tapa 1:')
print(teksti + ' ' + str(hinta))
mjono1 = teksti + ' ' + str(hinta)
print(mjono1)

print()  # tyhjä rivi tulosteeseen

# Tapa 2: print-funktiolla voidaan tulostaa monta eri tyyppistä arvoa:
print('Tapa 2:')
print(teksti, hinta)
mjono2 = teksti, hinta  # pilkku ei yhdistä, vaan luo "monikon"
print(mjono2)

print()

# Tapa 3: f-merkkiojonot: https://ohjelmointi-22.mooc.fi/osa-1/3-lisaa-muuttujista#tulostaminen-f-merkkijonojen-avulla
print('Tapa 3:')
print(f'{teksti} {hinta}')
