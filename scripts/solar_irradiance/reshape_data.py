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
#   - index 1: total amount of energy input at the top of earth's atmosphere
#              at a distance of 1au in the uv-spectrum (115.5-380nm), measured
#              in W/m^2
#   - index 2: amount of uncertainty in uv-spectrum total energy measured in
#              in W/m^2
#   - index 3: total amount of energy input at the top of earth's atmosphere
#              at a distance of 1au in the light-spectrum (380nm-772.5nm), measured
#              in W/m^2
#   - index 4: amount of uncertainty in light-spectrum total energy measured in
#              in W/m^2
#   - index 5: total amount of energy input at the top of earth's atmosphere
#              at a distance of 1au in the infrared-spectrum (777.5nm-99975nm), measured
#              in W/m^2
#   - index 6: amount of uncertainty in infrared-spectrum total energy measured in
#              in W/m^2
# - sorted from earliest to latest

FIRST_DAY = date(1900, 1, 1)
def day_num(date_time):
    if date_time < FIRST_DAY:
        return None
    else:
        return (date_time - FIRST_DAY).days

result = []
max_uv = 0.0
max_light = 0.0
max_infrared = 0.0

matcher = re.compile(r'ssi_\S{6}_daily_s([0-9]{4})[^\.]+\.nc')

workDir = os.path.join(os.curdir, 'raw')
for file in os.listdir(workDir):
    filename = os.fsdecode(file)
    match = matcher.match(filename)
    if match is None:
        print("Skipping file '{}'".format(filename))
        continue

    year = int(match.group(1))
    if year < 1900:
        print("Skipping file '{}': {} earlier than 1900".format(filename, year))
        continue

    path = os.path.join(workDir, filename)
    with open(path, mode='rb') as file_obj:
        with nc.Dataset('dummy', mode='r', memory=file_obj.read()) as ds:
            wavelengths = ds.variables['wavelength'][:]
            ssi_arr = ds.variables['SSI'][:]
            unc_arr = ds.variables['SSI_UNC'][:]
            date_units = ds.variables['time'].units
            ssi_mv = ds.variables['SSI'].missing_value
            ssi_unc_mv = ds.variables['SSI_UNC'].missing_value
            num_days = ds.variables['time'].size
            days = [day_num(nc.num2date(d[...], date_units).date()) for d in ds.variables['time'][:]]

            it_0 = enumerate(zip(days, ssi_arr, unc_arr))
            for index, (day, power_spectrum, uncs) in it_0:
                if day is None:
                    print("Found earlier date, skipping: {}".format(power_spectrum))
                    continue
                tot_uv = 0.0
                tot_uv_unc = 0.0
                tot_light = 0.0
                tot_light_unc = 0.0
                tot_infrared = 0.0
                tot_infrared_unc = 0.0

                it_1 = zip([x for x in power_spectrum[:] if x != ssi_mv], wavelengths[:], [x for x in uncs[:] if x != ssi_unc_mv])
                for irradiance, wavelength, uncertainty in it_1:
                    if wavelength <= 380:
                        tot_uv += irradiance[...] * wavelength[...]
                        tot_uv_unc += uncertainty[...] * wavelength[...]
                    elif wavelength <= 773:
                        tot_light += irradiance[...] * wavelength[...]
                        tot_light_unc += uncertainty[...] * wavelength[...]
                    elif wavelength <= 99975:
                        tot_infrared += irradiance[...] * wavelength[...]
                        tot_infrared_unc += uncertainty[...] * wavelength[...]
                    else:
                        raise 'Encountered invalid wavelength {}'.format(wavelength)
                max_uv = max(max_uv, tot_uv)
                max_light = max(max_light, tot_light)
                max_infrared = max(max_infrared, tot_infrared)

                result.append([day, tot_uv, tot_uv_unc, tot_light, tot_light_unc, tot_infrared, tot_infrared_unc])

                print("Year {}: day {}/{}".format(year, index + 1, num_days), end='\r')

result.sort(key=lambda v: v[0])
np.save('solar_irradiance', np.array(result))

print("max_uv: {}, max_light: {}, max_infrared: {}".format(max_uv, max_light, max_infrared))