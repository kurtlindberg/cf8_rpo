## Lake CF8 RPO Supplemental Figure 4
# RPO Tmax by sample type (lake sediment, soil, aquatic moss)

# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Author: Kurt R. Lindberg
# Last edited: 09/25/2024

# Import necessary packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set graphical parameters for editing in Inkscape
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = "sans-serif"

# Import data from NOAA paleoclimate datasheet
cf8_noaa_rpo = pd.read_excel("Lindberg_2024_CF8_NOAA_paleoclimate.xlsm",
                             sheet_name="RPO_Data",
                             header=48)

sample_type_num = [1,1,1,1,1,1,1,1,2,2,2,3,3]


# Figure script
fig, ax = plt.subplots(1, 1)

ax.scatter(sample_type_num, cf8_noaa_rpo.tmax, s=125, edgecolors='black')
ax.set_xlim([0.5, 3.5])
ax.set_ylim([350, 550])
ax.set_xticks(ticks=[1,2,3], labels=["Lake Sediment", "Soil", "Aquatic Moss"])
ax.set_ylabel("RPO Tmax (C)")

figures4 = plt.gcf()
# figures4.savefig('cf8rpo_sfig4_tmax.svg')