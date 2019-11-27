from datetime import date
import csv
import numpy as np
import os
import re
import sys
import hashlib


# Saves the data as multiple numpy arrays, named: weather_<canton>.npy
# - 2-dimensional array
# - first dimension contains the number of datapoints
# - second dimension contains:
#   - index 0: number of days since 01.01.1900
#   - index 1: Global radiation; daily mean, in W/m²
#   - index 2: Total snow depth; morning recording at 6 UTC in cm
#   - index 3: Cloud cover; daily mean in %
#   - index 4: Pressure at station level (QFE); daily mean in hPa
#   - index 5: Precipitation; daily total 6 UTC - 6 UTC following day in mm
#   - index 6: Sunshine duration; daily total in min
#   - index 7: Air temperature 2 m above ground; daily mean in °C
#   - index 8: Air temperature 2 m above ground; daily minimum in °C
#   - index 9: Air temperature 2 m above ground; daily maximum in °C
#   - index 10: Relative air humidity; 2 m above ground; daily mean in %
# - sorted from earliest to latest

STATION_LOCATIONS = {
    'alt': 'Altdorf',
    'ant': 'Andermatt',
    'rag': 'BadRagaz',
    'bas': 'BaselBinningen',
    'ber': 'BernZollikofen',
    'chd': 'Chateau_dOex',
    'chm': 'Chaumont',
    'gsb': 'Col_duGrandStBernard',
    'dav': 'Davos',
    'elm': 'Elm',
    'eng': 'Engelberg',
    'gve': 'GeneveCointrin',
    'grc': 'Graechen',
    'grh': 'GrimselHospiz',
    'jun': 'Jungfraujoch',
    'cdf': 'LaChaux_deFonds',
    'otl': 'LocarnoMonti',
    'lug': 'Lugano',
    'luz': 'Luzern',
    'mer': 'Meiringen',
    'neu': 'Neuchatel',
    'pay': 'Payerne',
    'sam': 'Samedan',
    'sae': 'Saentis',
    'sbe': 'StBernardino',
    'sia': 'Segl-Maria',
    'sio': 'Sion',
    'stg': 'StGallen',
    'sma': 'ZurichFluntern'
}
FIRST_DAY = date(1900, 1, 1)
def day_num(date_time):
    if date_time < FIRST_DAY:
        return None
    else:
        return (date_time - FIRST_DAY).days

result = {}

def parse_float(s):
    s = str(s).strip()
    if (len(s) == 0) or (s == "-"):
        return np.NaN
    else:
        return float(s)

def reshape_row(row, filename):
    if len(row) == 0:
        return
    station = row[0].lower().strip()
    if station == 'stn':
        return
    if len(station) == 0:
        print('Station "{}" invalid: {}', station, filename)
        return
    mean_radiation = 0.0
    total_snow_depth = 0.0
    cloud_cover = 0.0
    mean_pressure = 0.0
    mean_precipitation = 0.0
    sunshine_duration = 0.0
    mean_air_temp = 0.0
    min_air_temp = 0.0
    max_air_temp = 0.0
    mean_humidity = 0.0
    day_val = None
    date_val = None
    try:
        year = int(row[1][:4])
        month = int(row[1][4:6])
        day = int(row[1][6:8])
        date_val = date(year, month, day)
        day_val = day_num(date_val)
        if day_val is None:
            #print('Skipping row, {} earlier than 1900-1-1'.format(date_val))
            return
        mean_radiation = parse_float(row[2])
        total_snow_depth = parse_float(row[3])
        cloud_cover = parse_float(row[4])
        mean_pressure = parse_float(row[5])
        mean_precipitation = parse_float(row[6])
        sunshine_duration = parse_float(row[7])
        mean_air_temp = parse_float(row[8])
        min_air_temp = parse_float(row[9])
        max_air_temp = parse_float(row[10])
        mean_humidity = parse_float(row[11])
    except IndexError:
        pass
    except Exception as e:
        print('Failed to parse row {} in file "{}": {}'.format(row, filename, e))
    data_point = [
        day_val,
        mean_radiation,
        total_snow_depth,
        cloud_cover,
        mean_pressure,
        mean_precipitation,
        sunshine_duration,
        mean_air_temp,
        min_air_temp,
        max_air_temp,
        mean_humidity
    ]
    if station in result:
        result[station].append(data_point)
    else:
        result[station] = [data_point]

matcher = re.compile(r'.*\.csv')
workDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'raw')
for file in os.listdir(workDir):
    filename = os.fsdecode(file)
    match = matcher.match(filename)
    if match is None:
        print("Skipping file '{}'".format(filename))
        continue
    path = os.path.join(workDir, filename)
    num_rows = sum(1 for l in csv.reader(open(path, mode='r'), delimiter=';'))
    with open(os.path.join(workDir, filename), mode='r') as f:
        reader = csv.reader(f, delimiter=';')
        for i, row in enumerate(reader):
            reshape_row(row, filename)
            if i % 50 == 0:
                print("row {}/{} ({:4.2f}%)".format(i + 1, num_rows, (i + 1) / num_rows * 100), end='                     \r')

BUF_SIZE = 65536
hashes = {}
def hash_file(path):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
    return (md5.hexdigest(), sha1.hexdigest())

for key, dps in result.items():
    location = STATION_LOCATIONS[key]
    dps.sort(key=lambda v: v[0])
    filename = 'weather_{}.npy'.format(location)
    np.save(filename, np.array(dps))

    hashes[filename] = hash_file(filename)

print("HASHES---------------------------")
print(hashes)
