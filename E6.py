# Imports
import pcinput

# Inputs
oorspronkelijkSaldo = pcinput.getFloat('Geef oorspronkelijk saldo: ')
rente = pcinput.getFloat('Geef rente: ')
aantalJaar = pcinput.getInteger('Geef het aantal jaar: ')

# Berekeningen
groeifactor = 1 + rente/100
nieuwSaldo = round(oorspronkelijkSaldo * groeifactor**aantalJaar,2)

# Eindresultaat printen
print('Na {} jaar is je banksaldo {}').format(aantalJaar, nieuwSaldo)
