from datetime import date
import csv
import numpy as np

# Saves the data as a numpy array formatted as such:
# - 2-dimensional array
# - first dimension contains the number of datapoints
# - second dimension contains:
#   - index 0: number of days since 01.01.1900
#   - index 1: total nunber of sunspots of the day
# - sorted from earliest to latest

FIRST_DAY = date(1900, 1, 1)
def day_num(date_time):
    if date_time < FIRST_DAY:
        return None
    else:
        return (date_time - FIRST_DAY).days

result = []
max_sunspots = 0

with open('total_sunspots.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        year = int(row[0])
        month = int(row[1])
        day = int(row[2])
        day = day_num(date(year, month, day))
        provisional = row[7] == '*'

        sunspots = int(row[4])
        if day is None or sunspots == -1 or provisional:
            print("Skipping {}|{}|{}".format(day, sunspots, provisional))
            continue

        max_sunspots = max(sunspots, max_sunspots)

        result.append([day, sunspots])

result.sort(key=(lambda val: val[0]))

np.save('total_sunspots', np.array(result))
print('max_sunspots: {}'.format(max_sunspots))