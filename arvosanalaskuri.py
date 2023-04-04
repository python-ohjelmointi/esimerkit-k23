DISCLAIMER = '''
Tässä laskurissa mahdollisesti esiintyvät bugit ja virheet eivät muuta tai korvaa
virallista arviointia ja siihen liittyvää kaavaa. Laskuri antaa vain ei-sitovan
arvion loppuarvosanasta.
'''

print('''
Voit kokeilla tämän laskurin avulla, minkä loppuarvosanan eri
osasuoritukset tuottavat. Viikkotehtävien pistemäärän voit
tarkastaa osoitteesta https://tmc.mooc.fi/org/haaga-helia/.

* Viikkotehtävien painoarvo on 50 %
* Kokeen painoarvo on 50 %

''')

TEHTAVIA = 201


def laske_arvosana(tehtavapisteet: int) -> float:
    assert 0 <= tehtavapisteet <= TEHTAVIA, 'Virheellinen tehtäväpistemäärä'

    minimi = 0.25 * TEHTAVIA

    if tehtavapisteet < minimi:
        return 0

    return 1 + 4 * (tehtavapisteet - minimi) / (TEHTAVIA - minimi)


def main():
    omat_tehtavat = int(
        input(f'Syötä ratkaistujen viikkotehtävien määrä (0-{TEHTAVIA}): '))
    t_arvosana = laske_arvosana(omat_tehtavat)

    print(f'{omat_tehtavat} tehtäväpistettä vastaa arvosanaa {t_arvosana:.2f}')
    print()

    koe = float(input('Syötä kokeen arvosana (0.0-5.0): '))
    assert 0 <= koe <= 5, 'Virheellinen koearvosana'

    print()

    if min(t_arvosana, koe) >= 1:
        arvosana = t_arvosana * 0.5 + koe * 0.5
        print(f'Loppuarvosana on {round(arvosana)} ({round(arvosana, 2)})')
        print()
        print(DISCLAIMER)

    else:
        print('Suoritusta tulee täydentää')


main()
