import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


MeV_to_joule = 1.602176565e-13 # J/MeV

# paths = [r"Topas_project\Figure6_12\6_13_carbon_430MeV_i75_5.csv", 
#         r"Topas_project\Figure6_12\6_13_carbon_430MeV_i1000.csv", 
#         r"Topas_project\Figure6_12\6_13_carbon_430MeV_i500.csv", 
#         r"Topas_project\Figure6_12\6_13_carbon_430MeV_i250.csv", 
#         r"Topas_project\Figure6_12\6_13_carbon_430MeV_i125.csv", 
#         r"Topas_project\Figure6_12\6_13_carbon_430MeV_i150.csv"]
paths =[r"Topas_project\Figure6_12\6_12_carbon_220MeV_broad_1.csv",
        r"Topas_project\Figure6_12\6_12_carbon_430MeV_broad_2.csv"]
energy =[75, 1000, 500, 250, 125, 150]
i = 0
for path in paths:
    data = np.loadtxt(path, skiprows=9, delimiter=', ', usecols=(2, 3, 4))
    # print(data)
    field = 1 # cm2
    history = 1000
    fluence = history/field
    bin = data[:, 0]
    dose = data[:, 1]
    std = data[:, 2]
    bin_thick = 0.1

    # std_rel = (np.nanmean(std/dose))*100
    # std_max = (np.nanmax(std/dose))*100
    # print("mean: ", std_rel)
    # print("max: ", std_max)

    plt.plot(bin*bin_thick, dose/MeV_to_joule/1000/fluence, label=energy[i])
    i+=1

plt.xlabel('depth (cm)')
plt.ylabel("Energy deposition (MeV/g)")
# plt.xlim(29, 31.5)
# plt.legend()
plt.show()

# the energy is divided by the history number so we have the energy deposition per proton, and the surface of the beam

# beamcuttof of 5. cm
# beamspread of 0.5 mm for narrow, 6.5 mm for broad
# bigger world necessary: 50cm x 50cm x 50cm

# voxel volume: 2x2x2 = 8mm^3
#               5x5x5 = 125 mm^3
# code cloé: 62.5 mm^3


# essayé pour carbone: 
    # i:Sc/DoseAtPhantom/EBin = 100
    # d:Sc/DoseAtPhantom/EBinMin = 0 MeV
    # d:Sc/DoseAtPhantom/EBinMax = 2, 10 MeV, aucune différence


# essayé pour i-value:
    # =100, aucune différence