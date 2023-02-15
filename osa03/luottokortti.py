# https://en.wikipedia.org/wiki/Payment_card_number
# https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm

# MC: 5555555555554444
# Visa: 4111111111111111
kortti = '9876543'

if kortti[0] == '4':
    print('Visa')
elif 51 <= int(kortti[:2]) <= 55 or 2221 <= int(kortti[:4]) <= 2720:
    print('Mastercard')
else:
    print('Tuntematon')
