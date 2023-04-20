# Sanakirja "muistaa" järjestyksen, jossa arvot on lisätty:
sanakirja = {}

sanakirja["a"] = 1
sanakirja["x"] = 2
sanakirja["k"] = 3
sanakirja["y"] = 4
sanakirja["b"] = 5

print(sanakirja)
print(sanakirja.keys())  # 'a', 'x', 'k', 'y', 'b'

# Sanakirja voidaan käydä läpi "aakkosjärjestyksessä" sorttaamalla avaimet:
for kirjain in sorted(sanakirja.keys()):
    print(kirjain, sanakirja[kirjain])
