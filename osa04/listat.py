
kuukaudet = []

kuukaudet.append('tammi')
kuukaudet.append('helmi')
kuukaudet.append('maalis')

print(kuukaudet)

kuukaudet.pop(0)
kuukaudet.pop(-1)

print(kuukaudet)

kuukaudet.append('huhti')
kuukaudet.append('touko')

print(kuukaudet)

# insert lisää tiettyyn indeksiin ja siirtää seuraavia arvoja eteenpäin
kuukaudet.insert(0, 'tammi')
kuukaudet.insert(2, 'maalis')

print(kuukaudet)

# "assignment" operaatio korvaa aikaisemman arvon ko. indeksistä
kuukaudet[0] = 'january'
print(kuukaudet)
