import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


MeV_to_joule = 1.602176565e-13 # J/MeV

# paths = [r"",
#          r"",
#          r"C:\Users\gabri\Documents\Université\Maitrise\Session 1\physique_radiations\Devoir\Topas_project\Figure6_12\Dose_water_phantom_122MeV_14.csv"]
# path = r"C:\Users\gabri\Documents\Université\Maitrise\Session 1\physique_radiations\Devoir\Topas_project\Figure6_12\6_12_carbon_430MeV_broad.csv"
path = r"Topas_project\Figure6_12\6_12_carbon_350MeV_broad.csv"
data = np.loadtxt(path, skiprows=9, delimiter=', ', usecols=(2, 3, 4))
# print(data)
field = 100 # cm2
history = 10000
fluence = history/field
bin = data[:, 0]
dose = data[:, 1]
std = data[:, 2]
bin_thick = 0.1

std_rel = (np.nanmean(std/dose))*100
std_max = (np.nanmax(std/dose))*100
print("mean: ", std_rel)
print("max: ", std_max)

plt.plot(bin*bin_thick, dose/MeV_to_joule/1000/fluence)
plt.xlabel('depth (cm)')
plt.ylabel("Energy deposition (MeV/g)")
plt.show()

# the energy is divided by the history number so we have the energy deposition per proton, and the surface of the beam

# beamcuttof of 5. cm
# beamspread of 0.5 mm for narrow, 6.5 mm for broad
# bigger world necessary: 50cm x 50cm x 50cm

# voxel volume: 2x2x2 = 8mm^3
#               5x5x5 = 125 mm^3
# code cloé: 62.5 mm^3