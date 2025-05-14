## Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

## Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
## Gregory A. de Wet, Benjamin V. Gaglioti

## DOI: pending

## Code Author: Kurt R. Lindberg

### Figure S5 in Supporting Information S1 ###
## 02-CF8-01 dry bulk density


## See cf8_rpo_conda_env.yml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from composition_stats import closure
import pyleoclim as pyleo
from pylipd.lipd import LiPD
import cf8rpo_functions as cf8_fun

plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"

## Import data from LiPD files
cf8_dbd02_ens, cf8_dbd02 = cf8_fun.getlipd(
  'Axford.CF8.2009.lpd',
  paleoData_variableName='dryBulkDensity',
  depth_name='dryDepth',
  val_unit='g/cm3'
)

rpo_dbd_ens, rpo_dbd = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='dryBulkDensity',
  depth_name='RPOdepth',
  val_unit='g/cm3'
)

rpo_dbdstdev_ens, rpo_dbdstdev = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='dryBulkDensityStdev',
  depth_name='RPOdepth',
  val_unit='g/cm3'
)


## Figure S5 script
fig, axs = plt.subplots(1, 2)

ax = axs[0]
ax.plot(cf8_dbd02.paleoData_values, cf8_dbd02.depth, linewidth=0.75, color='black', zorder=10)
ax.scatter(cf8_dbd02.paleoData_values, cf8_dbd02.depth, s=10, color='black', zorder=10)
ax.hlines(y=107, xmin=0, xmax=1.25, colors='black', linestyles='--')
ax.vlines(x=rpo_dbd.paleoData_values[7], ymin=107, ymax=120, color='gray')
ax.axvspan(
  xmin=(rpo_dbd.paleoData_values[7]-rpo_dbdstdev.paleoData_values[7]),
  xmax=(rpo_dbd.paleoData_values[7]+rpo_dbdstdev.paleoData_values[7]),
  ymin=0, ymax=((120-107)/120), color='gray', alpha=0.25
)
ax.vlines(x=rpo_dbd.paleoData_values[0], ymin=0, ymax=107, color='#d95f0e')
ax.axvspan(
  xmin=(rpo_dbd.paleoData_values[0]-rpo_dbdstdev.paleoData_values[0]),
  xmax=(rpo_dbd.paleoData_values[0]+rpo_dbdstdev.paleoData_values[0]),
  ymin=((120-107)/120), ymax=1, color='#d95f0e', alpha=0.25
)

ax.set_xticks(ticks=[0, 0.25, 0.5, 0.75, 1.0, 1.25])
ax.set_yticks(ticks=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
ax.set_xlim([0, 1.25])
ax.set_ylim([120, 0])
ax.set_xlabel('Dry Bulk Density (g/cm3)')
ax.set_ylabel('Core 02-CF8-01 Depth (cm)')
ax.grid(visible=False)

fig.delaxes(axs[1])

figs5 = plt.gcf()
# figs5.savefig('cf8rpo_figs5.svg')
