import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta

solarirradiance = np.load("../data/astronomical/solar_irradiance.npy")

Weather = np.load("../data/weather/switzerland/weather_ZurichFluntern.npy")

solarirradiance = solarirradiance.astype(np.float)
Weather = Weather.astype(np.float)

start = date(1900,1,1)
data = []

lastyear = start.year
lastday = solarirradiance[0][0]
date = []
buff = 0
anz = 0
for node in solarirradiance:
    if node[0] != lastday:

        delta = timedelta(lastday)       
        offset = start + delta
        
        if offset.year != lastyear:
            date.append(offset.year)
            data.append(buff / (anz + 1))
            anz = 0
            buff = 0
        else:
            buff += node[5]
        anz += 1
        lastyear = offset.year
    else:
        buff += node[5]
    lastday = node[0]

data = np.array(data)


#plt.plot(date,data, label="solarirradiance")

print("first temperature date:\t" + str(date[0]) + "\tlast Sunspot Date:\t" + str(date[-1]))

cloudData = []
tempData = []
lastyear = start.year

lastday = Weather[0][0]
date = []
buff = 0
tempBuff = 0
anz = 0

for node in Weather:
    if node[0] != lastday:      
        delta = timedelta(lastday)       
        offset = start + delta
        
        if offset.year != lastyear:
            tempData.append(tempBuff / (anz + 1))
            cloudData.append(buff / (anz + 1))
            date.append(offset.year)
            buff = 0
            tempBuff = 0
            anz = 0
        else:
            buff += node[3]
            tempBuff += node[7]

        anz += 1
        lastyear = offset.year
    else:
        buff += node[3]
        tempBuff += node[7]

    lastday = node[0]

# multiply temp- and cloudData 
i = 0
while i < len(cloudData):
    # cloudData[i] = (cloudData[i] )
    i += 1

cloudData = np.array(cloudData)

print("first temperature date:\t" + str(date[0]) + "\tlast temperature Date:\t" + str(date[-1]))

print("len weather:\t"+str(len(cloudData))+"\t len solarirradiance:\t" + str(len(data)))

i = 0

while i < len(cloudData):
    if np.isnan(cloudData[i]):
        print("nan!!")
        cloudData[i] = 50
    i += 1

i = 0

while i < len(data):
    if np.isnan(data[i]):
        print("nan!!")
        data[i] = 50
    elif data[i] > 172500:
        data[i] = 172500
    i += 1


plt.scatter(data[0:118],cloudData[0:118])


z = np.polyfit(data[0:118],cloudData[0:118],1)
p = np.poly1d(z)
plt.plot(data[0:118],p(data[0:118]),"r--")

#plt.plot(date ,cloudData, label="clouds in %")

#plt.legend()

plt.show()