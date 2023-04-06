
def voittaa(asento1: str, asento2: str) -> bool:
    '''
    Kivi voittaa sakset (kivellä voi rikkoa sakset eikä saksilla voi leikata kiveä)
    Paperi voittaa kiven (kiven voi peittää paperilla)
    Sakset voittaa paperin (saksilla voi leikata paperia)

    >>> voittaa('kivi', 'sakset')
    True
    >>> voittaa('paperi', 'paperi')
    False
    '''
    if asento1 == 'kivi' and asento2 == 'sakset':
        return True
    if asento1 == 'sakset' and asento2 == 'paperi':
        return True
    if asento1 == 'paperi' and asento2 == 'kivi':
        return True
    return False


def vastustajan_asento(kierros: int) -> str:
    '''
    Vastustajan eli automaattisen tietokonepelaajan valinta tulee toteuttaa
    vuorottelemalla valintoja "kivi", "paperi" ja "sakset" aina samassa
    järjestyksessä.

    >>> vastustajan_asento(0)
    'kivi'
    >>> vastustajan_asento(1)
    'paperi'
    >>> vastustajan_asento(2)
    'sakset'
    >>> vastustajan_asento(3)
    'kivi'
    '''
    asennot = ['kivi', 'paperi', 'sakset']
    return asennot[kierros % len(asennot)]


def pelaa(kierrokset: int):
    voitot = 0
    tappiot = 0
    i = 0

    while voitot + tappiot < kierrokset:
        pelaaja = input('Valitse kivi, paperi tai sakset: ')
        if pelaaja not in ['kivi', 'paperi', 'sakset']:
            continue

        vastustaja = vastustajan_asento(i)
        print(f'Vastustajan valinta on {vastustaja}')

        if voittaa(pelaaja, vastustaja):
            voitot += 1
            print('Voitit!')
        elif voittaa(vastustaja, pelaaja):
            tappiot += 1
            print('Hävisit!')
        else:
            print('Tasapeli!')

        i += 1
        print()

    print(f'Voitot: {voitot}\nTappiot: {tappiot}')


if __name__ == '__main__':
    kierrokset = int(input('Kuinka monta kierrosta pelataan: '))
    pelaa(kierrokset)
