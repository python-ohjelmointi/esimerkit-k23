'''
Ohjelma selvittää päivän keskimääräisen pituuden tarkastamalla vuosien pituudet
merkittävän pitkältä aikaväliltä ja laskemalla niistä keskiarvon.

'Vuoden pituus on keskimäärin 365.2425 päivää'
'''

vuosia = 10_000_000
paivia = 0
nyk_vuosi = 0

while nyk_vuosi < vuosia:
    paivia += 365

    jaollinen_4 = nyk_vuosi % 4 == 0
    jaollinen_100 = nyk_vuosi % 100 == 0
    jaollinen_400 = nyk_vuosi % 400 == 0

    # onko karkausvuosi?
    if jaollinen_4 and (not jaollinen_100 or jaollinen_400):
        paivia += 1

    nyk_vuosi += 1

print(f'Vuoden pituus on keskimäärin {paivia / vuosia} päivää')
