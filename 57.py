import pcinput
import math

zijde1 = pcinput.getFloat('Lengte rechthoekszijde1 = ')
zijde2 = pcinput.getFloat('Lengte rechthoekszijde1 = ')
kwadraat = zijde1**2 + zijde2**2
schuinezijde = math.sqrt(zijde1**2 + zijde2**2)

print('De schuine zijde = %.2f') % schuinezijde
