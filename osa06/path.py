from pathlib import Path

# Pythonissa on "taikamuuttuja" __file__, joka sisältää nykyisen tiedoston polun:
file = Path(__file__)

# Nykyisen tiedoston hakemisto on sen "parent", joka saadaan Path-oliolta seuraavasti:
parent = Path(__file__).parent

# Nykyisen hakemiston perään voidaan lisätä toisen tiedoston nimi, jolloin saadaan
# työhakemistosta riippumatta oikea polku luettavaan tiedostoon:
csv = Path(__file__).parent / "tyontekijat.csv"

print("File:", file)
print("Parent:", parent)
print("tyontekijat.csv:", csv)
print("Exists?", csv.exists())
