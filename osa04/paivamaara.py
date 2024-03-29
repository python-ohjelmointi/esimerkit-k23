from datetime import date

paivat = [
    'maanantai', 'tiistai', 'keskiviikko',
    'torstai', 'perjantai', 'lauantai', 'sunnuntai'
]

kuukaudet = [
    'tammi', 'helmi', 'maalis', 'huhti', 'touko', 'kesä',
    'heinä', 'elo', 'syys', 'loka', 'marras', 'joulu'
]


def muotoile_pvm(pvm: date) -> str:
    '''
    >>> muotoile_pvm(date(2023, 12, 24))
    'sunnuntai 24. joulukuuta 2023'

    >>> muotoile_pvm(date(2023, 12, 25))
    'maanantai 25. joulukuuta 2023'
    '''
    kk = pvm.month  # tammi = 1, joulu = 12
    pv = pvm.isoweekday()  # Monday == 1 ... Sunday == 7

    return f'{paivat[pv - 1]} {pvm.day}. {kuukaudet[kk - 1]}kuuta {pvm.year}'


def main():
    tanaan: date = date.today()
    muotoiltu = muotoile_pvm(tanaan)

    print(muotoiltu.title())
    print(muotoile_pvm(date(2023, 12, 24)))


if __name__ == '__main__':
    main()
