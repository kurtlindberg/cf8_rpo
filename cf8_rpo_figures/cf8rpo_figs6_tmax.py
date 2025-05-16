# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

## Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
## Gregory A. de Wet, Benjamin V. Gaglioti

## DOI: pending

## Code Author: Kurt R. Lindberg

### Figure S6 in Supporting Information S1 ###
## RPO Tmax by sample type


## See cf8_rpo_conda_env.yml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Figure parameters for editing in Inkscape
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"

## Import data from NOAA paleoclimate datasheet
cf8_noaa_rpo = pd.read_excel(
  "Lindberg_2024_CF8_NOAA_paleoclimate.xlsm",
  sheet_name="RPO_Data",
  header=48
)

sample_type_num = [1,1,1,1,1,1,1,1,2,2,2,3,3]


# Figure S6 script
fig, ax = plt.subplots(1,1)

ax.scatter(sample_type_num, cf8_noaa_rpo.tmax, s=125, edgecolors='black')
ax.set_xlim([0.5,3.5])
ax.set_ylim([350,550])
ax.set_xticks(ticks=[1,2,3], labels=["Lake Sediment", "Soil", "Aquatic Moss"])
ax.set_ylabel("RPO Tmax (C)")

figs6 = plt.gcf()
# figs6.savefig('cf8rpo_figs6_tmax.svg')
