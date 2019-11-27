from datetime import date
import numpy as np
import os
import re

# Saves the data as a numpy array formatted as such:
# - 2-dimensional array
# - first dimension contains all datapoints
# - second dimension contains:
#   - index 0: number of days since 01.01.1900
#   - index 1: start_time in seconds since 00:00h
#   - index 2: delta_time in seconds
#   - index 3: optical importance based on flare area, possible values are:
#       - 0
#       - 1/3
#       - 0.5
#       - 2/3
#       - 1
#   - index 4: optical brightness, possible values are:
#       - 0
#       - 0.5
#       - 1
#   - index 5: x ray intensity, possible values are:
#       - 1 .. 9.9
#       - 10 .. 99
#       - 100 .. 990
#       - 1000 .. 9900
# - sorted from earliest to latest

FIRST_DAY = date(1900, 1, 1)
IMPORTANCE_LEVELS = {
    's': 0,
    '1': 1/3,
    '2': 2/3,
    '3': 1
}
BRIGHTNESS_LEVELS = {
    'f': 0,
    'n': 0.5,
    'b': 1
}
X_RAY_INTENSITY_CLS = {
    'b': 1,
    'c': 10,
    'm': 100,
    'x': 1000
}

def day_num(date_time):
    if date_time < FIRST_DAY:
        return None
    else:
        return (date_time - FIRST_DAY).days

result = []

matcher = re.compile(r'goes-xrs-report_([0-9]+)\S*\.txt')

workDir = os.path.join(os.curdir, 'raw')
for file in os.listdir(workDir):
    filename = os.fsdecode(file)
    match = matcher.match(filename)
    if match is None:
        print("Skipping file '{}'".format(filename))
        continue

    year = int(match.group(1))
    path = os.path.join(workDir, filename)
    currYear = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            day = 0
            if len(line) <= 5:
                print("Read invalid line in '{}': {}".format(filename, line))
                continue
            try:
                month = int(line[7:9])
                day = int(line[9:11])
                if year < 0 or year > 3000 or month < 1 or month > 12 or day < 1 or day > 31:
                    print("Read invalid datapoint in '{}', {}.{}.{}: {}".format(filename, year, month, day, line))
                day = day_num(date(year, month, day))
                if day is None:
                    continue
            except Exception as e:
                print("Read invalid datapoint in '{}', {}: {}".format(filename, e, line))
                exit()
                
            if day in currYear:
                currYear[day].append(line)
            else:
                currYear[day] = [line]
    
    for day, flares in currYear.items():
        for flare in flares:
            start_time = int(flare[13:15]) * 3600 + int(flare[15:17]) * 60
            end_time = int(flare[18:20]) * 3600 + int(flare[20:22]) * 60
            delta_time = end_time - start_time
            val = flare[34:35].lower()
            importance = 0.5
            if val in IMPORTANCE_LEVELS:
                importance = IMPORTANCE_LEVELS[val]
            
            val = flare[35:36].lower()
            brightness = 0.5
            if val in BRIGHTNESS_LEVELS:
                brightness = BRIGHTNESS_LEVELS[val]

            val = flare[59:60].lower()
            x_ray_intensity_cls = 1
            x_ray_intensity = 0
            if val in X_RAY_INTENSITY_CLS:
                x_ray_intensity_cls = X_RAY_INTENSITY_CLS[val]
            try:
                x_ray_intensity = x_ray_intensity_cls * float(flare[60:63])
            except:
                print('Could not convert x_ray_intensity_factor: {}'.format(flare[60:63]))
                x_ray_intensity = x_ray_intensity_cls

            data_point = [
                day,
                start_time,
                delta_time,
                importance,
                brightness,
                x_ray_intensity
            ]
            print(data_point)
            result.append(data_point)

def sorter(val):
    return val[0]
result.sort(key=sorter)
np.save('solar_flares', np.array(result))
