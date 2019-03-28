import pcinput

getal1 = pcinput.getInteger('Getal1 = ')
getal2 = pcinput.getInteger('Getal2 = ')
getal3 = pcinput.getInteger('Getal3 = ')
som = getal1 + getal2 + getal3
gemiddelde = float(som/3)

print('Het grootste getal is {}').format(max(getal1, getal2, getal3))
print('Het kleinste getal is {}').format(min(getal1, getal2, getal3))
print('Het gemiddelde is {}').format(gemiddelde)
