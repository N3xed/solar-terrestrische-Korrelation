import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta

def plotGraph():
    IrradianceDataset = np.load("C:/Users/Domim00/Documents/Dominic_Schule/astroweather/astrological-weather/data/astronomical/solar_irradiance.npy")


    SunspotDataset = np.load("C:/Users/Domim00/Documents/Dominic_Schule/astroweather/astrological-weather/data/astronomical/total_sunspots.npy")

    dailySunspots = []

    for row in SunspotDataset:
        dailySunspots.append(row[1])

    start = date(1900,1,1)  

    particleDensity = []
    lastday = 0
    Date = []
    for row in IrradianceDataset:
        particleDensity.append(row[2])
        delta = timedelta(lastday)
        offset = start + delta
        Date.append(offset)
        lastday = row[0]

    
    print("length of sunspots Dataset: " + str(len(dailySunspots)))
    print("length of irradiance Dataset: " + str(len(particleDensity)))

    
    # plt.plot(Date, dailySunspots[0:43464], label = "sunspots daily")

    # plt.plot(Date,particleDensity, label = "particle density daily")


    # plt.legend()

    plt.show()

plotGraph()