import pcinput

getal1 = pcinput.getFloat('Getal1 = ')
getal2 = pcinput.getFloat('Getal2 = ')
getal3 = pcinput.getFloat('Getal3 = ')
som = getal1 + getal2 + getal3
gemiddelde = som/3

print('Het grootste getal is {}').format(int(max(getal1, getal2, getal3)))
print('Het kleinste getal is {}').format(int(min(getal1, getal2, getal3)))
print('Het gemiddelde is %.2f') % gemiddelde
