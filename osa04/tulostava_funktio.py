

def tutki(parametri):
    print(f'Sisältö: {parametri}')
    print(f'Pituus: {len(parametri)}')

    # yksittäiset arvot haetaan hakasuluilla ja indeksillä:
    print(f'Eka: {parametri[0]}')  # indeksit alkavat 0:sta
    print(f'Vika: {parametri[-1]}')  # negatiiviset indeksit otetaan lopusta

    # osajonot
    print(f'Kolme ekaa: {parametri[:3]}')  # "puoliavoin väli"
    # jos yläraja jää pois, otetaan loppuun asti:
    print(f'Kolme vikaa: {parametri[-3:]}')

    # osajono "takaperin":
    print(f'Takaperin: {parametri[::-1]}')

    # Sisällön tutkiminen:
    print(f'Sisältää "ma": {("ma" in parametri)}')

    # yhteen- ja kertolaskut
    print(f'Yhteenlasku: {parametri + parametri}')
    print(f'Kertolasku: {parametri * 2}')

    print()  # tyhjä rivi


suomeksi = 'terve maailma'
englanniksi = 'hello world'

tutki(suomeksi)
tutki(englanniksi)

# listat toimivat monelta osin täysin identtisesti merkkijonojen kanssa:
monta_sanaa = ['ma', 'ti', 'ke', 'to', 'pe', 'la', 'su']
tutki(monta_sanaa)
