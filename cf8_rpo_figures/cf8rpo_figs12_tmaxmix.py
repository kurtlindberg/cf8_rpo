# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Code Author: Kurt R. Lindberg

# Figure S10 in Supporting Information S1
# (a) MixSIAR postglacial soil OC % vs. RPO Tmax
# (b) MixSIAR aquatic OC % vs. RPO Tmax

# See cf8_rpo_conda_env.yml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import scipy.stats
from composition_stats import closure
import pyleoclim as pyleo
from pylipd.lipd import LiPD
import cf8rpo_functions as cf8_fun

# Figure parameters for editing in Inkscape
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"

# Import data from LiPD files
rpo_tmax_ens, rpo_tmax = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='tmax',
    depth_name='RPOdepth',
    val_unit='deg C'
)

mix_aqua_ens, mix_aqua = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='mixsiarAquatic',
    depth_name='RPOdepth',
    val_unit='fraction'
)

mix_post_ens, mix_post = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='mixsiarPostglacial',
    depth_name='RPOdepth',
    val_unit='fraction'
)

tmax_mix = pd.DataFrame(
    {
        'tmax':rpo_tmax.paleoData_values,
        'mix_aqua':mix_aqua.paleoData_values,
        'mix_post':mix_post.paleoData_values
    }
).sort_values(by='tmax')

modelaqua = LinearRegression().fit(
    np.array(tmax_mix.tmax).reshape((-1,1)), np.array(tmax_mix.mix_aqua)*100
)
modelpost = LinearRegression().fit(
    np.array(tmax_mix.tmax).reshape((-1,1)), np.array(tmax_mix.mix_post)*100
)

aqua_corr = np.array(scipy.stats.pearsonr(tmax_mix.tmax, tmax_mix.mix_aqua))
post_corr = np.array(scipy.stats.pearsonr(tmax_mix.tmax, tmax_mix.mix_post))


# Figure S12 a-b script
fig, axs = plt.subplots(2,2)

# Figure S12a: MixSIAR postglacial soil OC % vs. RPO Tmax
ax = axs[0,0]
ax.scatter(
    tmax_mix.tmax, tmax_mix.mix_post*100,
    s=40, color='orange', edgecolors='black', zorder=2,
    label="R = " + str(np.round(post_corr[0], decimals=3)) + "; p = " + str(np.round(post_corr[1], decimals=2))
)
ax.plot(
    tmax_mix.tmax, (np.array(tmax_mix.tmax)*modelpost.coef_+modelpost.intercept_),
    linestyle='--', color='black',
    zorder=1
)
ax.set_xlim([375,450])
ax.set_ylim([0,100])
ax.set_xlabel('RPO Tmax (C)')
ax.set_ylabel('MixSIAR Postglacial %')
ax.legend(loc='upper left')
ax.grid(visible=False)

# Figure S12b: MixSIAR aquatic OC % vs. RPO Tmax
ax = axs[0,1]
ax.scatter(
    tmax_mix.tmax, tmax_mix.mix_aqua*100,
    s=40, color='blue', edgecolors='black', zorder=2,
    label="R = " + str(np.round(aqua_corr[0], decimals=3)) + "; p = " + str(np.round(aqua_corr[1], decimals=2))
)
ax.plot(
    tmax_mix.tmax, (np.array(tmax_mix.tmax)*modelaqua.coef_+modelaqua.intercept_),
    linestyle='--', color='black', zorder=1
)
ax.set_xlim([375,450])
ax.set_ylim([0,100])
ax.set_xlabel('RPO Tmax (C)')
ax.set_ylabel('MixSIAR Aquatic %')
ax.legend(loc='upper left')
ax.grid(visible=False)

fig.delaxes(axs[1,0])
fig.delaxes(axs[1,1])

figs12 = plt.gcf()
# figs12.savefig('cf8rpo_figs12_tmaxmix.svg')


# Regresssion test removing lowest Tmax data point

tmax_test = tmax_mix[tmax_mix['tmax'] > 400]
print(tmax_test)
print(tmax_mix)

aqua_corr2 = np.array(scipy.stats.pearsonr(tmax_test.tmax, tmax_test.mix_aqua))
post_corr2 = np.array(scipy.stats.pearsonr(tmax_test.tmax, tmax_test.mix_post))

print(post_corr)
print(post_corr2)
print(aqua_corr)
print(aqua_corr2)
