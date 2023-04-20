postinumerot: dict = {"HELSINKI": ["00100", "00730"]}

print(postinumerot)

# Aiheuttaa KeyError-poikkeuksen, jos avainta ei löydy:
print(postinumerot["HELSINKI"])

# Ei aiheuta poikkeusta, vaikka avainta ei löytyisi:
print(postinumerot.get("ESPOO", "ei löytynyt"))
