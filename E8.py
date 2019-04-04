import pcinput

input = pcinput.getInteger('Geef een aantal minuten: ')
aantalSeconden = input * 60
aantalUren = int(input/ 60)
aantalMinuten = (input - aantalUren * 60)
print('{} minuten is gelijk aan {} seconden').format(input, aantalSeconden)
print('{} minuten is gelijk aan {} uur en {} minuten').format(input, aantalUren, aantalMinuten)
