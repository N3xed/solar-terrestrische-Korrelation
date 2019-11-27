## Swiss weather data
The data is available as multiple numpy files, named: weather_<location>.npy
- 2-dimensional array
- first dimension contains the number of datapoints
- second dimension contains:
  - index 0: number of days since 01.01.1900
  - index 1: Global radiation; daily mean, in W/m²
  - index 2: Total snow depth; morning recording at 6 UTC in cm
  - index 3: Cloud cover; daily mean in %
  - index 4: Pressure at station level (QFE); daily mean in hPa
  - index 5: Precipitation; daily total 6 UTC - 6 UTC following day in mm
  - index 6: Sunshine duration; daily total in min
  - index 7: Air temperature 2 m above ground; daily mean in °C
  - index 8: Air temperature 2 m above ground; daily minimum in °C
  - index 9: Air temperature 2 m above ground; daily maximum in °C
  - index 10: Relative air humidity; 2 m above ground; daily mean in %
- sorted from earliest to latest
- source: https://opendata.swiss/en/dataset/klimamessnetz-tageswerte