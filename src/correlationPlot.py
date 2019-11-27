import matplotlib.pyplot as plt
import numpy as np
import csv

swissTemp = []

FullYear = []
year = []
temp = []
rain = []
tempYearly = []
CorrRain = []
with open("C:\\Users\\Domim00\\Documents\\Dominic_Schule\\astroweather\\astrological-weather\\data\\swissData.csv","r") as csvfile:
    input = csv.reader(csvfile, delimiter=";")
    for row in input:        
        row = list(map(float, row))
        year.append(row[0] + row[1] / 13)
        temp.append(row[2])
        rain.append(row[3])
        swissTemp.append(row)

sunspots = []
with open("C:\\Users\\Domim00\\Documents\\Dominic_Schule\\astroweather\\astrological-weather\\data\\SN_d_tot_V2.0.csv","r") as output:
    input = csv.reader(output, delimiter=";")
    for row in input:
        sunspots.append(row)

sunspotsMonthly = [[],[]]
i = 0
j = 0
k = 0
old = '1'
lastyear = '1881'
f = open("debug.txt", "w")
f.write("")
f.close()
for row in sunspots:
    if row[1] == old:
        i +=  int(row[4])
    else:
        f = open("debug.txt", "a")
        if row[0] != lastyear:
            if row[0] == '2006':
                sunspotsMonthly[k].append(i)
                f.write("\nYear: \t" + str(lastyear) +"\t Month: \t" + str(old)+"\t Sunspots: \t" + str(i) + "\n")
                f.write("\n2019: Havnt aquired enough Data!")
                break
            else:
                f.write("\nYear: \t" + str(lastyear) +"\t Month: \t" + str(old)+"\t Sunspots: \t" + str(i) + "\n")
                sunspotsMonthly[k].append(i)
                sunspotsMonthly.append([])
                lastyear = row[0]
                k += 1
        else:
            f.write("\nYear: \t" + str(row[0]) +"\t Month: \t" + str(old)+"\t Sunspots: \t" + str(i) + "\n")
            sunspotsMonthly[k].append(i)
        j += 1
        i = 0
    old = row[1]

allSunspot = []
sunspotYearly = []
buff = 0
for row in sunspotsMonthly:
    buff = 0
    for i in row:
        buff += i
        allSunspot.append(i)
    sunspotYearly.append(buff)

# Read Rain and temperature yearly
last = 1864
i = 0
buff = 0
tempbuff = 0
while i < len(rain): 
    if last != int(year[i]):
        last = int(year[i])
        tempYearly.append(tempbuff / 12)
        CorrRain.append(buff)
        FullYear.append(int(year[i]))
        buff = 0
        tempbuff = 0
    else:
        tempbuff += temp[i]
        buff += rain[i]
    i += 1

i = 0
while i < len(temp):
    temp[i] -= 10
    temp[i] *= 100
    rain[i] *= 10
    i+=1

i = 0
while FullYear[i] < 1881:
    i+= 1

npspot = np.array(allSunspot[0: 200])

fftspot = np.fft.fft(npspot)
spotfref = np.fft.fftfreq(fftspot.size)

# plt.plot(spotfref, fftspot, label= "sunspot Fouriertransform")

nptemp = np.array(temp[0:200])
fourieTransform = np.fft.fft(nptemp)
freq = np.fft.fftfreq(nptemp.size)

#plt.plot(freq, fourieTransform, label="temperature Fouriertransform")

plt.legend(loc ='upper left')

# plt.plot(FullYear[i: i + 50], sunspotYearly[0:50])
# plt.plot(FullYear[i: i + 50], CorrRain[i:i + 50])
plt.scatter(sunspotYearly[0: 100],tempYearly[i:i + 100])
# plt.plot(FullYear[0: 100], tempYearly[0:100], label="temperature")
# plt.plot(year[i:i+ 500], rain[i:i+ 500], label="rain")
# plt.plot(year[i:i+ 500],allSunspot[0:500], label="sunspot")
# plt.legend(loc='upper left')

#plt.plot(year[i: i + 100], sunspotYearly[0:100])

z = np.polyfit(sunspotYearly[0:100],tempYearly[17:17+100],1)
p = np.poly1d(z)
plt.plot(sunspotYearly[0:100],p(sunspotYearly[0:100]),"r--")

plt.show()


