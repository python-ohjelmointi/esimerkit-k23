from postinumerot import postinumerot

numero = input("Syötä postinumero: ")

# in-operaatio tarkastaa löytyykö **avaimista**
if numero in postinumerot:
    print(f"{numero} löytyy toimipaikasta {postinumerot[numero]}")
else:
    print("Ei löytynyt")
