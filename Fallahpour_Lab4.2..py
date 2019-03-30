# Ildiko Fallahpour
# Complete

# This program displays how much the ocean's level rises each year for 25 years.
print("This program displays how much the ocean's level rises in 25 years.")
print()
#Print the table headings.
print('Year\tRise  (in millimeters)')
print('------------------------------')

#Print the Years from 1 to 25 and the corresponding rise.
for year in range(1, 26):
    rise = year*1.80
    print(year, '\t', format(rise, '.2f'))
