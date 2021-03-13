import matplotlib.pyplot as plt
import csv

data = [[],[],[]]

with open('logs.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data[0].append(float(row[0]))
        data[1].append(float(row[1]))
        data[2].append(float(row[2]))




x = list(range(len(data[0])))
print(len(data[0]))
print(len(data[1]))
print(len(data[2]))
plt.plot(x, data[0], 'r', x, data[1], 'b', x, data[2], 'g')
plt.axis([0,len(x),  0, max(data[0])])
plt.show()