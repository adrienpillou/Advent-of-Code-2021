import numpy as np

m = np.zeros((3, 3), int)
m[2, 2] = 1

print(m)
print("")
print(m[1:3, 1:3])