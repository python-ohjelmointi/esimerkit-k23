from collections import namedtuple

# Dict on tässä esimerkissä enemmän "tietotyyppi" kuin kokoelma:
monty_python = {
    "nimi": "Monty Python",
    "ohjaaja": "Renny Pytholin",
    "vuosi": 1900,
    "pituus": 100,
}

# Tietotyyppiä varten voimme määritellä oman "Leffa"-tuplen, jossa on **oltava** aina tietyt arvot.
# Leffa on kirjoitettu isolla alkukirjaimella, jotta se erottuu "tavallisista" muuttujista:
Leffa = namedtuple("Leffa", "nimi ohjaaja vuosi pituus")

# Leffa-tyypistä voidaan nyt luoda uusi tuple, joka vastaa yhtä elokuvaa:
py_lentokoneessa = Leffa("Python lentokoneessa", "Renny Pytholin", 2001, 94)

# Lopputulos on aika samanlainen sekä dict- että namedtuple-toteutuksissa:
print(monty_python)
print(py_lentokoneessa)

# Jos tiedon mallinnus kiinnostaa enemmän, kannattaa
# käydä jatkokurssia ainakin osaan 8 asti.
