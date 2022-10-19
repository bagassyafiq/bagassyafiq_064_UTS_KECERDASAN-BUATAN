#Nama : Bagas Syafiq Aero Pradana
#NIM : 21091397064/Kelas B 2021

import numpy as np

inputs = [2.10, 3.10, 2.11, 4.13, 14.5, 12.3, 8.9, 7.7, 3.7, 6.7]
weights = [13.2, 12.2, 41.3, 10.6, 11.5, 16.2, 12.4, 19.2, 18.5, 13.7]

bias = 3.9

outputs = np.dot(weights, inputs) + bias
print(outputs)
