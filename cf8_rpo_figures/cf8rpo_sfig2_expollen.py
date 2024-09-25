## Lake CF8 RPO Supplemental Figure 2
# Core 02-CF8-01 exotic pollen
# Data from Crump et al. (2021)
# DOI: https://doi.org/10.1073/pnas.2019069118
# Link to data on Neotoma database (Site ID: 27331): https://apps.neotomadb.org/explorer/

# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Author: Kurt R. Lindberg
# Last edited: 09/25/2024

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from composition_stats import closure
import pyleoclim as pyleo
from pylipd.lipd import LiPD
import cf8rpo_functions as cf8_fun

plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = "sans-serif"

# Import data from LiPD files
cf8_pollen_ens, cf8_pollen = cf8_fun.getlipd('Crump.CF8.2021.lpd',
                                     paleoData_variableName='exoticPollenPercent',
                                     depth_name='depth',
                                     val_unit='percent')

fig, ax = plt.subplots(1, 1)
cf8_pollen_ens.common_time(time_axis=cf8_pollen.ageMedian, bounds_error=False).plot_envelope(ax=ax,
                                                                                             curve_clr='#006d2c',
                                                                                             shade_clr='#006d2c',
                                                                                             plot_legend=False)
ax.plot(cf8_pollen.ageMedian, cf8_pollen.paleoData_values, linestyle='--', color='black', zorder=100)
ax.set_xlim([12500, 0])
ax.set_xticks(ticks=[12000, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0],
              labels=[12000, "", 10000, "", 8000, "", 6000, "", 4000, "", 2000, "", 0])
ax.set_ylim([0, 5])
ax.set_xlabel('Age (cal yr BP)')
ax.set_ylabel('Exotic Pollen %')
ax.legend([])
ax.grid(visible=False)

figures2 = plt.gcf()
# figures2.savefig('cf8rpo_figures2.svg')
