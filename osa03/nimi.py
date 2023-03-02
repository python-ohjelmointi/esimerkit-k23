hello = 'world'

# kun ohjelma on "pääohjelma", tulostuu '__main__',
# muuten tulostuu 'nimi'
print(__name__)


if __name__ == '__main__':
    print('pääohjelma')
else:
    print('ei pääohjelma')
