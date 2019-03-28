# tweeEuroMunt, eenEuroMunt, vijftigEurocent, twintigEurocent,
# tienEurocent, vijfEurocent, tweeEurocent, eenEurocent, bedrag,
# inCenten, aantalTweeEuroMunt, aantalEenEuroMunt,
# aantalVijftigEurocent, aantalTwintigEurocent, aantalTienEurocent,
# aantalVijfEurocent, aantalTweeEurocent en aantalEenEurocent

bedrag = 187.45

tweeEuroMunt = 2
eenEuroMunt = 1
vijftigEurocent = 0.50
twintigEurocent = 0.20
tienEurocent = 0.10
vijfEurocent = 0.05
tweeEurocent = 0.02
eenEurocent = 0.01

print "Het bedrag is {}".format(bedrag)

# 2
aantalTweeEuroMunt = int(bedrag / tweeEuroMunt)
bedrag -= aantalTweeEuroMunt * tweeEuroMunt
print "{} 2-euromunt".format(aantalTweeEuroMunt)
# 1
aantalEenEuroMunt = int(bedrag / eenEuroMunt)
bedrag -= aantalEenEuroMunt * eenEuroMunt
print "{} 2-euromunt".format(aantalEenEuroMunt)
# 0.50
aantalVijftigEurocent = int(bedrag / vijftigEurocent)
bedrag -= aantalVijftigEurocent * vijftigEurocent
print "{} 2-euromunt".format(aantalVijftigEurocent)
#0.20
aantalTwintigEurocent = int(bedrag / twintigEurocent)
bedrag -= aantalTwintigEurocent * twintigEurocent
print "{} 2-euromunt".format(aantalTwintigEurocent)

print "Rest in eurocent is {}".format(bedrag * 100)
