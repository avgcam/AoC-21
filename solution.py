import numpy as np

file = 'input1.txt'
data = np.loadtxt(file, delimiter=' ', dtype=int)

print(data)