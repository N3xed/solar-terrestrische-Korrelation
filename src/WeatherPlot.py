import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta

Sunspots = np.load("../data/astronomical/total_sunspots.npy")

Weather = np.load("../data/weather/switzerland/weather_ZurichFluntern.npy")

Sunspots = Sunspots.astype(float)
Weather = Weather.astype(float)

start = date(1900,1,1)

data = []
lastday = Sunspots[0][0]
date = []
buff = 0
anz = 0
for node in Sunspots:
    if node[0] != lastday:      
        delta = timedelta(lastday)       
        offset = start + delta
        data.append(buff / (anz + 1))
        date.append(offset)
        anz = 0
        buff = node[1]
    else:
        anz += 1
        buff += node[1]
    lastday = node[0]

data = np.array(data)

fft = np.fft.fft(data[0:95])
freq = np.fft.fftfreq(95)

print("last Sunspot Date: " + str(date[-1]))

print("Len Sunspot Data: " + str(len(data)) + " Len Sunspot Date: " + str(len(date)))

# plt.plot(freq[1:], fft[1:], label ="sunspots fft")

data = []
dataTemp = []
lastday = Weather[0][0]
date = []
buff = 0
tempBuff = 0
anz = 0
for node in Weather:
    if node[0] != lastday:      
        delta = timedelta(lastday)       
        offset = start + delta
        dataTemp.append(tempBuff / (anz + 1))
        data.append(buff / (anz + 1))
        date.append(offset)
        anz = 0
        buff = node[3]
        tempBuff = node[7]
    else:
        anz += 1
        buff += node[3]
        tempBuff += node[7]
    lastday = node[0]

data = np.array(data)

data = np.diff(data)

i = 0
while i < len(fft):
    # fft[i] *= 10
    i+=1

fft = np.fft.fft(data[0:95])

freq = np.fft.fftfreq(95)

print("last temperature Date: " + str(date[-1]))

print("Len Data: " + str(len(data)) + " Len Date: " + str(len(date)))

# plt.plot(date[0:95], data[0:95])


plt.plot(freq[1:],fft[1:], label = "cloud cover fft")

plt.legend()

plt.show()