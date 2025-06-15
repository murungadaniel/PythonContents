# import numpy as np
from time import time

start = time()
a = [i for i in range(100)]
b = [i for i in range(100)]

c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
print("Time Taken",start - time())

