"""
Miten voimme Pythonilla mallintaa esim. seuraavanlaista dataa,
jossa saattaa olla 5-5000 eri postinumeroa?

74701 Kiuruvesi
35540 Juupajoki
00100 Helsinki
74705 Pakettiautomaatti
"""

postinumerot = {}
postinumerot["74701"] = "Kiuruvesi"
postinumerot["00100"] = "Helsinki"

print(postinumerot)

print(postinumerot["00100"])

if "90210" in postinumerot:
    print(postinumerot["90210"])
else:
    print("ei löytynyt")


print(len(postinumerot))
