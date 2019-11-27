## Solar Flares
- first dimension contains all datapoints
- second dimension contains:
  - index 0: number of days since 01.01.1900
  - index 1: start_time in seconds since 00:00h
  - index 2: delta_time in seconds
  - index 3: optical importance based on flare area, possible values are:
      - 0
      - 1/3
      - 0.5
      - 2/3
      - 1
  - index 4: optical brightness, possible values are:
      - 0
      - 0.5
      - 1
  - index 5: x ray intensity, possible values are:
      - 1 .. 9.9
      - 10 .. 99
      - 100 .. 990
      - 1000 .. 9900
- sorted from earliest to latest
- Source: https://www.ngdc.noaa.gov/stp/solar/solarflares.html

## Solar Wind
- first dimension contains all datapoints
- second dimension contains:
  - index 0: number of days since 01.01.1900
  - index 1: solar wind proton particales temperature measured in Kelvin
  - index 2: solar wind proton particles density in 1/cm^3
  - index 3: solar wind proton particales velocity X component in Geocentric Solar Ecliptic coordinates
  - index 4: solar wind proton particales velocity Y component in Geocentric Solar Ecliptic coordinates
  - index 5: solar wind proton particales velocity Z component in Geocentric Solar Ecliptic coordinates
- sorted from earliest to latest
- Source: https://www.ngdc.noaa.gov/dscovr/portal/index.html#/

## Solar Irradiance
- first dimension contains all datapoints
- second dimension contains:
  - index 0: number of days since 01.01.1900
  - index 1: total amount of energy input at the top of earth's atmosphere
             at a distance of 1au in the uv-spectrum (115.5-380nm), measured
             in W/m^2
  - index 2: amount of uncertainty in uv-spectrum total energy measured in
             in W/m^2
  - index 3: total amount of energy input at the top of earth's atmosphere
             at a distance of 1au in the light-spectrum (380nm-772.5nm), measured
             in W/m^2
  - index 4: amount of uncertainty in light-spectrum total energy measured in
             in W/m^2
  - index 5: total amount of energy input at the top of earth's atmosphere
             at a distance of 1au in the infrared-spectrum (777.5nm-99975nm), measured
             in W/m^2
  - index 6: amount of uncertainty in infrared-spectrum total energy measured in
             in W/m^2
- sorted from earliest to latest
- Source:  
        (ncdc.noaa.gov)[https://www.ncdc.noaa.gov/cdr/atmospheric/solar-spectral-irradiance]
        (data.nodc.noaa.gov)[https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.ncdc:C00899]
- Citation:  
    Odele Coddington, Judith L. Lean, Doug Lindholm, Peter Pilewskie, Martin Snow, and NOAA CDR Program (2015): NOAA Climate Data Record (CDR) of Solar Spectral Irradiance (SSI), NRLSSI Version 2. [indicate subset used]. NOAA National Centers for Environmental Information. doi:10.7289/V51J97P6 [24.10.2019].

## Sunspots
- first dimension contains the number of datapoints
- second dimension contains:
  - index 0: number of days since 01.01.1900
  - index 1: total nunber of sunspots of the day
- sorted from earliest to latest
- Source: http://www.sidc.be/silso/datafiles