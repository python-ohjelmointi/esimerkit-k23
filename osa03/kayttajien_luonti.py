from salasanat import luo_salasana

i = 0

while i < 100:
    tunnus = f'user{i}'
    salasana = luo_salasana(64)

    print(f'CREATE USER "{tunnus}" IDENTIFIED BY "{salasana}";')

    i += 1
