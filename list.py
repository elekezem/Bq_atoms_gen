import os
import csv

n = []
for k in range(1,200):
    n.append(k)
with open('list.csv', 'w', newline='') as csvfile:
    cubewriter = csv.writer(csvfile, delimiter=' ')
    for c in range(len(n)):
        cubewriter.writerow([n[c]])
    pass
