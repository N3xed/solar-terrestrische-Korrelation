import numpy as np
import os
import re
import netCDF4 as nc
from datetime import date

# Saves the data as a numpy array formatted as such:
# - 2-dimensional array
# - first dimension contains all datapoints
# - second dimension contains:
#   - index 0: number of days since 01.01.1900
#   - index 1: solar wind proton particales temperature measured in Kelvin
#   - index 2: solar wind proton particles density in 1/cm^3
#   - index 3: solar wind proton particales velocity X component in Geocentric Solar Ecliptic coordinates
#   - index 4: solar wind proton particales velocity Y component in Geocentric Solar Ecliptic coordinates
#   - index 5: solar wind proton particales velocity Z component in Geocentric Solar Ecliptic coordinates
# - sorted from earliest to latest

FIRST_DAY = date(1900, 1, 1)
def day_num(date_time):
    if date_time < FIRST_DAY:
        return None
    else:
        return (date_time - FIRST_DAY).days

def mean(values, ignore_value):
    n = 0
    sum = 0.0
    for v in values:
        if v[...] == ignore_value:
            continue
        sum += v[...]
        n += 1
    if n == 0:
        return None
    else:
        return sum / n

result = []

matcher = re.compile(r'oe_f1m_dscovr_s([0-9]{4})([0-9]{2})([0-9]{2}).+\.nc')

workDir = os.path.join(os.curdir, 'raw')
for file in os.listdir(workDir):
    filename = os.fsdecode(file)
    match = matcher.match(filename)
    if match is None:
        #print("Skipping file '{}'".format(filename))
        continue

    year = int(match.group(1))
    month = int(match.group(2))
    real_day = int(match.group(3))
    date_v = date(year, month, real_day)
    day = day_num(date_v)
    if day is None:
        print("Skipping file '{}': {} earlier than 1900".format(filename, year))
        continue

    path = os.path.join(workDir, filename)
    with open(path, mode='rb') as file_obj:
        with nc.Dataset('dummy', mode='r', memory=file_obj.read()) as ds:
            proton_temp_iter = ds.variables['proton_temperature'][:].data
            proton_temp_mean = mean(proton_temp_iter, ds.variables['proton_temperature'].missing_value)

            proton_density_iter = ds.variables['proton_density'][:].data
            proton_density_mean = mean(proton_density_iter, ds.variables['proton_density'].missing_value)

            proton_vx_gse_iter = ds.variables['proton_vx_gse'][:].data
            proton_vx_gse_mean = mean(proton_vx_gse_iter, ds.variables['proton_vx_gse'].missing_value)

            proton_vy_gse_iter = ds.variables['proton_vy_gse'][:].data
            proton_vy_gse_mean = mean(proton_vy_gse_iter, ds.variables['proton_vy_gse'].missing_value)

            proton_vz_gse_iter = ds.variables['proton_vz_gse'][:].data
            proton_vz_gse_mean = mean(proton_vz_gse_iter, ds.variables['proton_vz_gse'].missing_value)

            data_point = [day, proton_temp_mean, proton_density_mean, proton_vx_gse_mean, proton_vy_gse_mean, proton_vz_gse_mean]
            if None in data_point:
                print("Found none value, skipping {}".format(date_v))
            print(data_point)
            result.append(data_point)
            print("{}".format(date_v), end='\r')

result.sort(key=lambda v: v[0])
np.save('solar_wind', np.array(result))