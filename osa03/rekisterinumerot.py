# Huom! Ei paras tapa käsitellä rekisterinumeroita, mutta toimii
# tämän aiheen esimerkkinä...

# 1-3 kirjainta, (tasan yksi) väliviiva ja 1-3 numeroa
rekisterinumero = 'ABCD-23'

# Vähintään 3 merkkiä, korkeintaan 7
pituus = len(rekisterinumero)
pituus_ok = 3 <= pituus <= 7

viivojen_maara = rekisterinumero.count('-')

if pituus_ok and viivojen_maara == 1:
    vasen, oikea = rekisterinumero.split('-')

    if vasen.isalpha() and oikea.isdigit():
        print('Rekkari on OK!')
    else:
        print('Rekkari ei ok')

else:
    print('Rekkari ei ok')
