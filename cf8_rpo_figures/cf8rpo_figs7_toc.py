# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Code Author: Kurt R. Lindberg

# Figure S7 in Supporting Information S1
# RPO total organic carbon % and Elemental Analyzer % Carbon vs. age


# See cf8_rpo_conda_env.yml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from composition_stats import closure
import pyleoclim as pyleo
from pylipd.lipd import LiPD
import cf8rpo_functions as cf8_fun

# Figure parameters for editing in Inkscape
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"

# Import data from LiPD files
ea_totalc_ens, ea_totalc = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='totalCarbon',
    depth_name='EAdepth',
    val_unit='percent'
)

rpo_toc_ens, rpo_toc = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='RPOtotalOrganicCarbon',
    depth_name='RPOdepth',
    val_unit='percent'
)


# Figure S7 script
fig, ax = plt.subplots(1,1)

ax.plot(
    rpo_toc.ageMedian, rpo_toc.paleoData_values,
    color='black', linestyle='-', linewidth=0.75,
    zorder=1
)
ax.scatter(
    rpo_toc.ageMedian, rpo_toc.paleoData_values,
    s=50, marker='o', color='gray', edgecolors='black', linewidths=0.75,
    zorder=2, label='RPO'
)
ax.plot(
    ea_totalc.ageMedian, ea_totalc.paleoData_values,
    color='black', linestyle='--', linewidth=0.75,
    zorder=3
)
ax.scatter(
    ea_totalc.ageMedian, ea_totalc.paleoData_values,
    s=50, marker='d', color='gray', edgecolors='black', linewidths=0.75,
    zorder=4, label='EA'
)
ax.set_ylim([0,16])
ax.set_xlim([12500,0])
ax.set_yticks(ticks=[0,4,8,12,16])
ax.set_xticks(
    ticks=[12000,11000,10000,9000,8000,7000,6000,5000,4000,3000,2000,1000,0],
    labels=[12000,"",10000,"",8000,"",6000,"",4000,"",2000,"",0]
)
ax.set_xlabel('RPO %TOC, EA %C')
ax.set_ylabel('CF817-3A-1B-02 Depth (cm)')
ax.legend()
ax.grid(visible=False)

figs7 = plt.gcf()
# Uncomment to save figure
# figs7.savefig('cf8rpo_figs7_toc.svg')
