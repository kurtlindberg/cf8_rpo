## Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

## Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
## Gregory A. de Wet, Benjamin V. Gaglioti

## DOI: pending

## Code Author: Kurt R. Lindberg

### Figure S2 in Supporting Information S1 ###
## RPO CO2 14C ages pre- and post-blank correction


## See cf8_rpo_conda_env.yml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

## Figure parameters for editing in Inkscape
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"

## Import data from blank correction comparison spreadsheet
blanks = pd.read_excel('cf8rpo_blankcorrect.xlsx')


## Figure S2 script

rpo_colors = [
    '#2166ac',
    '#67a9cf',
    '#fddbc7',
    '#ef8a62',
    '#b2182b'
]

fig, axs = plt.subplots(1,1)

ax = axs
ax.errorbar(
    x=blanks.num, y=blanks.noblank_14c, yerr=blanks.noblank_unc,
    ecolor='black', markeredgecolor='black',
    linestyle="None", markersize=5, fmt='', zorder=1
)
ax.scatter(
    x=blanks.num, y=blanks.noblank_14c,
    c=rpo_colors*8, edgecolors='black', marker='^', s=30, zorder=2
)
ax.errorbar(
    x=blanks.num, y=blanks.blank_14c, yerr=blanks.blank_unc,
    ecolor='black', markeredgecolor='black',
    linestyle="None", markersize=5, fmt='', zorder=3
)
ax.scatter(
    x=blanks.num, y=blanks.blank_14c,
    c=rpo_colors*8, edgecolors='black', marker='o', s=30,
    zorder=4
)
ax.set_xticks(
    ticks=[3,8,13,18,23,28,33,38],
    labels=[5,15,45,75,85,95,105,110]
)
ax.set_yticks(
    ticks=[12000, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0],
    labels=[12000, "", 10000, "", 8000, "", 6000, "", 4000, "", 2000, "", 0]
)
ax.set_xlabel('Sample Top Depth (cm)')
ax.set_ylabel('RPO CO2 Age (14C yrs)')

sfigure_blank = plt.gcf()
# sfigure_blank.savefig('cf8rpo_sfig_blank.svg')

