## Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

## Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
## Gregory A. de Wet, Benjamin V. Gaglioti

## DOI: pending

## Code Author: Kurt R. Lindberg

### Figure S1 in Supporting Information S1 ###
## (a) CF817-03 sediment core image
## (b) RPO and EA subsampling depths
## (c) Magnetic susceptibility
## (d) Age-depth model from rbacon (see lipd_gcr_basics.R)

## panels a and d added using Inkscape

## See cf8_rpo_conda_env.yml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from composition_stats import closure
import pyleoclim as pyleo
from pylipd.lipd import LiPD
import cf8rpo_functions as cf8_fun

## Figure parameters for editing in Inkscape
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"

## Import data from LiPD files
ms_ens, ms = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='MS',
  depth_name='geotekDepth',
  val_unit='SI'
)

rpo_depth_ens, rpo_depth = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='RPOdepth',
  depth_name='RPOdepth',
  val_unit='cm'
)

ea_depth_ens, ea_depth = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='EAdepth',
  depth_name='EAdepth',
  val_unit='cm'
)

rpo_pos = np.full((1, len(rpo_depth.depth)), 1)
ea_pos = np.full((1, len(ea_depth.depth)), 3)

## Figure S1 b-c script
fig, axs = plt.subplots(1, 4)

## Figure S1b: RPO and EA subsampling depths
ax = axs[0]
ax.scatter(rpo_pos, rpo_depth.depth, marker='o', color='gray', edgecolors='black', linewidth=0.75, label='RPO')
ax.scatter(ea_pos, ea_depth.depth, marker='d', color='gray', edgecolors='black', linewidth=0.75, label='EA')

ax.set_xlim([0, 5])
ax.set_xticks([])
ax.set_xticklabels("")
ax.set_ylim([112, 0])
ax.set_yticks(ticks=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
ax.set_ylabel("CF817-03 Depth (cm)")
ax.legend(loc='lower center', bbox_to_anchor=(0.5,1))
ax.grid(visible=False)

## Figure S1c: Magnetic susceptibility
ax = axs[1]
ax.plot(ms.paleoData_values, ms.depth, color='black', linewidth=0.75)

ax.set_ylim([112, 0])
ax.set_xlim([-5, 150])
ax.set_xticks(ticks=[0, 50, 100, 150])
ax.set_yticks([])
ax.set_yticklabels("")
ax.set_xlabel('MS')
ax.grid(visible=False)

fig.delaxes(axs[2])
fig.delaxes(axs[3])
# fig.delaxes(axs[4])

figures1bc = plt.gcf()
# figures1bc.savefig('cf8rpo_figures1bc.svg')
