# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

rivinvaihdolla = 'heittomerkit \'tehdään näin\''
print(rivinvaihdolla)

numero = 10
print('tekstiä + ' + str(numero))

leveys = 60
# merkkijonojen "kertolasku"
print('.' * leveys)

merkkijono = 'Spring Security on hankalaa'

print(merkkijono.lower())
print(merkkijono.upper())
print(merkkijono)  # alkuperäinen ei koskaan muutu!

print(merkkijono.capitalize())

print(merkkijono.swapcase())
print(merkkijono.title())

print(merkkijono.center(leveys, '*'))
print(merkkijono.ljust(leveys, '*'))
print(merkkijono.rjust(leveys, '*'))

print('   python   '.lstrip() + '.')
print('   python   '.rstrip() + '.')
print('   python   '.strip() + '.')
