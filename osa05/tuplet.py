alkuaika = (2023, 4, 12)

print(alkuaika)
print(type(alkuaika))

# Tuplen käyttäminen toimii hyvin samalla tavalla kuin listan:
print(alkuaika[0])
print(alkuaika[-1])
print(sum(alkuaika))
print(alkuaika[0:1])

# Tuple on muuttumaton:
# alkuaika.remove(2013)   # ei sallittu
# alkuaika[0] = 2014      # ei sallittu

# Tuple voidaan purkaa erillisiin muuttujiin (kuten listat ja str)
vuosi, kk, paiva = alkuaika
print(f"{vuosi=}, {kk=}, {paiva=}")
