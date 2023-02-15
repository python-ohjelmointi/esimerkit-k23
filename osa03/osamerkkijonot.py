# https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

kirjaimet = 'abcdefghijklmnopqrstuvwxyzåäö'
# -----------0123456789

print(kirjaimet[0])
print(kirjaimet[1])
print(kirjaimet[2])

vika_indeksi = len(kirjaimet) - 1
print(f'pituus: {len(kirjaimet)}, vika indeksi {vika_indeksi}')
print(kirjaimet[vika_indeksi])  # 28 => ö
print(kirjaimet[-1])            # -1 => ö

print('Osamerkkijonot:')
print(kirjaimet[0:3])
print(kirjaimet[10:15])

# alku on oletuksena nolla:
print(kirjaimet[:15])

# loppu on oletuksena "loppuun asti":
print(kirjaimet[15:])

# ei loppua eikä alkua?!
print(kirjaimet[:])

# kahden välein alusta loppuun:
print(kirjaimet[::2])

# negatiivisella askeleella saadaan käytyä lopusta alkuun:
i = 15
j = 10
k = -1
print(kirjaimet[i:j:k])

# kääntäen koko merkkijono:
print(kirjaimet[::-1])
