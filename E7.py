import pcinput
from math import pi

straal = pcinput.getFloat('Geef een straal: ')
diameter = straal * 2
omtrek = diameter * pi
oppervlakte = (straal**2) * pi
print('Omtrek is {} meter').format(omtrek)
print('Oppervlakte is {} vierkante meter').format(oppervlakte)
