## Lake CF8 RPO Supplemental Figure X
# Compiled MixSIAR endmember d13C by sample type

# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Author: Kurt R. Lindberg
# Last edited: 02/24/2025

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set graphical parameters for editing in Inkscape
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"

# Import data from compilation spreadsheet
mix_d13c = pd.read_excel('mixsiar_d13c_compilation.xlsx')

aq = mix_d13c[mix_d13c['aq'] == 1]
pg = mix_d13c[mix_d13c['pg'] == 1]
mis5 = mix_d13c[mix_d13c['mis5'] == 1]
mix = mix_d13c[mix_d13c['mix'] == 1]


# Figure Script

colors = [
    'blue',
    'orange',
    'black',
    'white'
]

fig, axs = plt.subplots(1,1)

ax = axs
ax.scatter(np.full(shape=len(aq.d13c), fill_value=1), aq.d13c, marker='o', s=50, color='blue', edgecolors='black', linewidths=0.75)
ax.scatter(np.full(shape=len(pg.d13c), fill_value=2), pg.d13c, marker='o', s=50, color='orange', edgecolors='black', linewidths=0.75)
ax.scatter(np.full(shape=len(mis5.d13c), fill_value=3), mis5.d13c, marker='o', s=50, color='grey', edgecolors='black', linewidths=0.75)
ax.scatter(np.full(shape=len(mix.d13c), fill_value=4), mix.d13c, marker='o', s=50, color='white', edgecolors='black', linewidths=0.75)
ax.set_xlim([0,5])
ax.set_ylim([-40,-5])
ax.set_xticks(
    ticks=[1,2,3,4],
    labels=['Aquatic','Postglacial','MIS 5','CF8 Sediment (Mix)']
)
ax.set_xlabel("Endmember/Mixture")
ax.set_ylabel("d13C (%)")

sfigure_mixd13c = plt.gcf()
sfigure_mixd13c.savefig('cf8rpo_sfig_mixd13c.svg')
