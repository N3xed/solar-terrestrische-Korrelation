#***************************************************
# BMA 2019 Neural Network for predicting           *
# temperature anomalies                            *
#***************************************************
import tensorflow as tf
from tensorflow import keras
from keras.utils import plot_model
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from PIL import Image
import os
import csv

tempAnomalie = []
sunspots = []

# Dataset source: https://cdiac.ess-dive.lbl.gov/ftp/trends/temp/lugina/0-90N.dat(Data: northern hemisphere)
with open("../data/AVERAGE/AV.csv","r") as csvfile:
    input = csv.reader(csvfile, delimiter=";")
    for row in input:
        tempAnomalie.append(row)

# Write the sunspot Data to an array
with open("../data/AVERAGE/SN_d_tot_V2.0.csv","r") as output:
    input = csv.reader(output, delimiter=";")
    for row in input:
        sunspots.append(row)

# this Block adds together all the sunspots from one month and prints it
# j is a variable for debugging purposes, it indicates the number of months        
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
                f.write("\n2019: Havent aquired enough Data!")
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

del sunspotsMonthly[-1]

year = []
# Temp list ist nur für den Plot, die Werte stimmen nicht
temp = []
for row in tempAnomalie:
    year.append(row[0])
    temp.append(row[1])

temp = list(map(float,temp))
j = 0
while j < len(temp):
    temp[j] *= 50000
    print("Temp: \t" + str(temp[j])) 
    j += 1
y = 0
tempYearly = []
for row in tempAnomalie:
    tempYearly.append(0)
    k = 1
    while k < 13:
        tempYearly[y] += (float(row[k]) / 12)
        k += 1
    y += 1

plt.figure(figsize=(10,10))
plt.xticks(np.arange(0,210,step= 10))
# plt.yticks(np.arange(0,1,step= 10))
# plt.yticks(np.arange(0,0))
# plt.plot(year,sunspotsMonthly[0:125])
tempYearly = list(map(float,tempYearly))
plt.plot(year,tempYearly)
plt.show()


print(tempYearly)

i = 0
tempYearly[i] = 2
i += 1

while i < (len(tempYearly)-1):    
    if tempYearly[i] < tempYearly[i-1] and tempYearly[i] < tempYearly[i+1]:
        tempYearly[i] = 0
    elif tempYearly[i] > tempYearly[i-1] and tempYearly[i] > tempYearly[i+1]:
        tempYearly[i] = 1
    elif tempYearly[i] > tempYearly[i-1] and tempYearly[i] < tempYearly[i+1]:
        tempYearly[i] = 2
    else:
        tempYearly[i] = 3
    i += 1

#i = 1881
#for row in sunspotsMonthly:
#    row.append(i)
#    i += 1

print(tempYearly)

# sunspots monthly: 
# 1881:  |-----------------------|
#        |  jan | feb | .. | dec | 
#        |-----------------------|
#
#... :   |-----------------------|
#        |  jan | feb | .. | dec | 
#        |-----------------------|
#       
#2005:   |-----------------------|
#        |  jan | feb | .. | dec | 
#        |-----------------------|
#

trainData = tf.convert_to_tensor(sunspotsMonthly[0:90])
trainLabel = tf.convert_to_tensor(tempYearly[0:90], float)

testData =  tf.convert_to_tensor(sunspotsMonthly[90:125])
testLabel = tf.convert_to_tensor(tempYearly[90: 125], float)
       
print(trainLabel)

# Create a sequential Keras Model
   
model = keras.Sequential([
    keras.layers.Dense(128,input_shape=(12,), activation=tf.nn.relu),  # Densly connected hidden layer with 128 neurons
    keras.layers.Dense(10, activation=tf.nn.softmax) # 10 Output layers 
])

model.compile(optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
    )


model.fit(trainData, trainLabel, epochs=10, steps_per_epoch=125)

test_loss, test_acc = model.evaluate(testData,testLabel, steps=35)

print("accuraty on test set: ", test_acc)
print("loss on test set: ", test_loss)

plot_model(model,to_file="simplemodel.png")