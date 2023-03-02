from salasanat import luo_salasana

# haluan suorittaa nämä vain, jos tätä skriptiä suoritetaan "pääohjelmana"
pituus = int(input('Syötä salasanan pituus: '))
print(f'Salasanasi on {luo_salasana(pituus)}')
