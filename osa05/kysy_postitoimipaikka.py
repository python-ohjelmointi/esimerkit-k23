from postinumerot import postinumerot

etsittava_nimi = input("Syötä toimipaikan nimi: ")

# Dict:in `values` palauttaa listan kaltaisen kokoelman kaikista sanakirjan **arvoista**
if etsittava_nimi in postinumerot.values():

    tulokset: list[str] = []

    # `items` palauttaa avaimet ja arvot pareittain, jolloin läpikäynti on helppoa:
    for numero, toimipaikka in postinumerot.items():
        if etsittava_nimi == toimipaikka:
            tulokset.append(numero)

    print(tulokset)

else:
    print("ei löydy")
