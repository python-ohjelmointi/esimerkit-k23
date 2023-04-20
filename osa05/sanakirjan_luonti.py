# Sanakirjoja voidaan luoda useilla eri syntakseilla. "Paras" syntaksi
# riippuu käyttötapauksesta: onko esim. arvot tiedossa jo koodia
# kirjoitettaessa vai muodostetaanko data täysin dynaamisesti.

skirja1 = {"Helsinki": "00100"}
print(skirja1)

skirja2 = dict(Helsinki="00100")
print(skirja2)

skirja3 = dict([("Helsinki", "00100"), ("Juupajoki", "35540")])
print(skirja3)
