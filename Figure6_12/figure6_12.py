import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

path = r"C:\Users\gabri\Documents\Université\Maitrise\Session 1\physique_radiations\Devoir\Figure6_12\Dose_water_phantom_122MeV.csv"
data = np.loadtxt(path, skiprows=9, delimiter=', ', usecols=(2, 3, 4))
# print(data)

plt.plot(data[:, 0]*0.333, data[:, 1])
plt.xlabel('depth (cm)')
plt.ylabel("Energy deposition (Gy)")
plt.show()

