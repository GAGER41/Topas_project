import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# paths = [r"",
#          r"",
#          r"C:\Users\gabri\Documents\Université\Maitrise\Session 1\physique_radiations\Devoir\Topas_project\Figure6_12\Dose_water_phantom_122MeV_14.csv"]
path = r"C:\Users\gabri\Documents\Université\Maitrise\Session 1\physique_radiations\Devoir\Topas_project\Figure6_12\6_12_protons_230MeV_rect_10000h.csv"
data = np.loadtxt(path, skiprows=9, delimiter=', ', usecols=(2, 3, 4))
# print(data)
field = 100 # cm2
history = 10000
fluence = history/field
plt.plot(data[:, 0]*0.1, data[:, 1]/1.602176565e-13/1000/10000)
plt.xlabel('depth (cm)')
plt.ylabel("Energy deposition (MeV/g)")
plt.show()

# the energy is divided by the history number so we have the energy deposition per proton, and the surface of the beam

# beamcuttof of 5. cm
# beamspread of 0.5 mm for narrow, 6.5 mm for broad
# bigger world necessary: 50cm x 50cm x 50cm