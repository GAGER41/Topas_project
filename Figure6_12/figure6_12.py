import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# paths = [r"",
#          r"",
#          r"C:\Users\gabri\Documents\Université\Maitrise\Session 1\physique_radiations\Devoir\Topas_project\Figure6_12\Dose_water_phantom_122MeV_14.csv"]
path = r"C:\Users\gabri\Documents\Université\Maitrise\Session 1\physique_radiations\Devoir\Topas_project\Figure6_12\Dose_water_phantom_230MeV_15.csv"
data = np.loadtxt(path, skiprows=9, delimiter=', ', usecols=(2, 3, 4))
# print(data)
field = 100 # cm2
history = 1000
fluence = history/field
plt.plot(data[:, 0]*0.35, data[:, 1]/1.602176565e-13/1000/fluence)
plt.xlabel('depth (cm)')
plt.ylabel("Energy deposition (MeV/g)")
plt.show()

# the energy is divided byt the history number so we have the energy depoosition per proton

# spread of 0.65 cm
# cuttof of 5. cm
# bigger world: 50cm x 50cm x 50cm