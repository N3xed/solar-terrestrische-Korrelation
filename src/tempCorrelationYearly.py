import matplotlib.pyplot as plt
import numpy as np
import csv

swissTemp = []
year = []
temp = []

with open("C:\\Users\\Domim00\\Documents\\Dominic_Schule\\astroweather\\astrological-weather\\data\\swissYearly.csv","r") as csvfile:
    input = csv.reader(csvfile, delimiter=";")
    for row in input:        
        row = list(map(float, row))
        year.append(row[0])
        temp.append(row[19])
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
            if row[0] == '2018':
                sunspotsMonthly[k].append(i)
                f.write("\nYear: \t" + str(lastyear) +"\t Month: \t" + str(old)+"\t Sunspots: \t" + str(i) + "\n")
                f.write("\n2019: haven't aquired enough Data!")
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

sunspotYearly = []
buff = 0
for row in sunspotsMonthly:
    print(row)
    buff = 0
    for i in row:
        buff += i
    sunspotYearly.append(buff)

i = 0
while i < len(temp):
#    temp[i] -= 10
#    temp[i] *= 1000
    i+=1

temp = np.array(temp)
sunspotYearly = np.array(sunspotYearly)

i = 0
while year[i] < 1881:
    i+= 1

plt.scatter(sunspotYearly[0:120],temp[i:i+120])


z = np.polyfit(sunspotYearly[0:120],temp[i:i+120],1)
p = np.poly1d(z)
plt.plot(sunspotYearly[0:120],p(sunspotYearly[0:120]),"r--")

#fft = np.fft.fft(sunspotYearly)
#freq = np.fft.fftfreq(sunspotYearly.shape[-1])

#plt.plot(freq[1:60],fft.real[1:60],label="sunspot")

#print("len fft: " + str(len(fft)))
#print("len freq: " + str(len(freq)))

#print("len of Sunspot: " + str(len(sunspotYearly))+ " len of temp: " + str(len(temp)))

#fft2 = np.fft.fft(temp[i:])

#freq = np.fft.fftfreq(len(temp)-i)

#i = 0

#while i < len(fft2):
#    fft2[i] *= 10000
#    i+=1

#print("len fft2: " + str(len(fft2)))
#print("len freq2: " + str(len(freq)))

#plt.plot(freq[1:60],fft2.real[1:60], label="temp")


plt.legend()

#plt.plot(year[i: i + 100], sunspotYearly[0:100])

#z = np.polyfit(sunspotYearly[0:120],temp[i:i+120],1)
#p = np.poly1d(z)
#plt.plot(sunspotYearly[0:120],p(sunspotYearly[0:120]),"r--")

plt.show()

