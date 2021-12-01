import numpy as np

file = 'input1.txt'
data = np.loadtxt(file, delimiter=' ', dtype=int)

for i in data:
	print(i)
