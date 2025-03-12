num = input('Three-digit number: ')

units = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

hundreds = {
    '0': '',
    '1': 'one hundred',
    '2': 'two hundred',
    '3': 'three hundred',
    '4': 'four hundred',
    '5': 'five hundred',
    '6': 'six hundred',
    '7': 'seven hundred',
    '8': 'eight hundred',
    '9': 'nine hundred'
}

tens = {
    '0': '',
    '1': 'ten',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}

special = {
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

out = ''
if num[1:] in special:
    out = hundreds[num[0]] + ' ' + special[num[1:]]
else:
    out = (hundreds[num[0]] + ' ' +
           tens[num[1]] + ' ' +
           units[num[2]])

print('In words:', out)
