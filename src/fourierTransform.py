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

fft = np.fft.fft(data)
freq = np.fft.fftfreq(data.shape[-1])


print("last Sunspot Date: " + str(date[-1]))

print("Len Sunspot Data: " + str(len(data)) + "Len Sunspot Date: " + str(len(date)))

plt.plot(freq[1:500], fft.real[1:500], label ="sunspots fft")

data2 = []
lastday = Sunspots[0][0]
date = []
buff = 0
anz = 0

for node in Weather:
    if node[0] != lastday:      
        delta = timedelta(lastday)       
        offset = start + delta
        data2.append(buff / (anz + 1))
        date.append(offset)
        anz = 0
        buff = node[6]
    else:
        anz += 1
        buff += node[6]
    lastday = node[0]

data2 = np.array(data2)

fft = np.fft.fft(data2)

i = 0
while i < len(fft):
    fft[i] *= 50
    i+=1
    
freq = np.fft.fftfreq(data.shape[-1])

del date[-1]

print("last temperature Date: " + str(date[-1]))

print("Len Data: " + str(len(data)) + "Len Date: " + str(len(date)))

plt.plot(freq[1:500], fft.real[1:500], label = "temperature fft")

plt.legend()

# plt.scatter(data[0:40000], data2[0:40000])

# z = np.polyfit(data[0:40000],data2[0:40000],1)
# p = np.poly1d(z)
# plt.plot(data[0:40000],data[0:40000],"r--")

plt.show()