## Lake CF8 RPO Figure 1
# Site map and modern climatology
# Monthly temperature and precipitation

# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Author: Kurt R. Lindberg
# Last edited: 09/25/2024

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy import config

plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = "sans-serif"

projLcc = ccrs.LambertConformal(central_longitude=-70,central_latitude=60)
resol = '50m'
land = cfeature.NaturalEarthFeature('physical', 'land', scale=resol, edgecolor='black')
border = cfeature.NaturalEarthFeature(category='cultural', name='admin_0_boundary_lines_land', scale=resol, facecolor='none')
ocean = cfeature.NaturalEarthFeature('physical', 'ocean', scale=resol, edgecolor='none', facecolor=cfeature.COLORS['water'])
lakes = cfeature.NaturalEarthFeature('physical', 'lakes', scale=resol, edgecolor='none', facecolor=cfeature.COLORS['water'])

ax = plt.axes(projection=projLcc)
#ax.coastlines(resolution=resol, color='black', zorder=10)
gl = ax.gridlines(draw_labels=False, linewidth=1, color='black', alpha=0.5, linestyle='--', zorder=200)
ax.add_feature(land, facecolor='white', alpha=0.7, zorder=5)
ax.add_feature(border, alpha=0.7, linewidth=1, zorder=50)
ax.add_feature(ocean, zorder=1)
#ax.add_feature(lakes, zorder=25)
ax.set_extent([-85, -55, 59, 76], crs=ccrs.PlateCarree())

plt.plot([-68.94968], [70.55818], '*', color='red', markeredgecolor='black', markersize=20, zorder=100, transform=ccrs.PlateCarree())

figure1a = plt.gcf()
# figure1a.savefig('cf8rpo_figure1a.svg')


# ERA5 climatology data from Climate Reanalyzer (https://climatereanalyzer.org/research_tools/monthly_tseries/)
tempc = pd.read_csv('CF8_ClimRean_temp_all.csv', header=8)
precipmm = pd.read_csv('CF8_ClimRean_precip_all.csv', header=8)

tempc = tempc[(tempc['Year'] > 1990) & (tempc['Year'] <= 2020)]
temp_plot = pd.concat([tempc.Jan,
                       tempc.Feb,
                       tempc.Mar,
                       tempc.Apr,
                       tempc.May,
                       tempc.Jun,
                       tempc.Jul,
                       tempc.Aug,
                       tempc.Sep,
                       tempc.Oct,
                       tempc.Nov,
                       tempc.Dec]).to_frame(name="Temp")
temp_plot.insert(loc=1,
                 column="Month",
                 value=(
                 ['Jan']*len(tempc.Jan) +
                 ['Feb']*len(tempc.Feb) +
                 ['Mar']*len(tempc.Mar) +
                 ['Apr']*len(tempc.Apr) +
                 ['May']*len(tempc.May) +
                 ['Jun']*len(tempc.Jun) +
                 ['Jul']*len(tempc.Jul) +
                 ['Aug']*len(tempc.Aug) +
                 ['Sep']*len(tempc.Sep) +
                 ['Oct']*len(tempc.Oct) +
                 ['Nov']*len(tempc.Nov) +
                 ['Dec']*len(tempc.Dec)))

precipmm = precipmm[(precipmm['Year'] > 1990) & (precipmm['Year'] <= 2020)]
precip_plot = pd.concat([precipmm.Jan,
                       precipmm.Feb,
                       precipmm.Mar,
                       precipmm.Apr,
                       precipmm.May,
                       precipmm.Jun,
                       precipmm.Jul,
                       precipmm.Aug,
                       precipmm.Sep,
                       precipmm.Oct,
                       precipmm.Nov,
                       precipmm.Dec]).to_frame(name="Precip")
precip_plot.insert(loc=1,
                 column="Month",
                 value=(
                 ['Jan']*len(precipmm.Jan) +
                 ['Feb']*len(precipmm.Feb) +
                 ['Mar']*len(precipmm.Mar) +
                 ['Apr']*len(precipmm.Apr) +
                 ['May']*len(precipmm.May) +
                 ['Jun']*len(precipmm.Jun) +
                 ['Jul']*len(precipmm.Jul) +
                 ['Aug']*len(precipmm.Aug) +
                 ['Sep']*len(precipmm.Sep) +
                 ['Oct']*len(precipmm.Oct) +
                 ['Nov']*len(precipmm.Nov) +
                 ['Dec']*len(precipmm.Dec)))

fig, axs = plt.subplots(2, 1)

# ax = axs[0, 0]
ax = axs[0]
sns.pointplot(ax=ax, x=temp_plot.Month, y=temp_plot.Temp, color='red', marker=None, linewidth=1.5)
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel("Temp. (C)")
ax.set_yticks(ticks=[-30, -20, -10, 0, 10])
ax.set_ylim([-35, 10])

# ax = axs[1, 0]
ax = axs[1]
sns.pointplot(ax=ax, x=precip_plot.Month, y=(precip_plot.Precip*1000), color='blue', marker=None, linewidth=1.5)
ax.set_xlabel("")
ax.set_ylabel("Precip. (mm)")
ax.set_yticks(ticks=[0, 20, 40, 60])
ax.set_ylim([0, 70])

# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 1])

figure1b = plt.gcf()
# figure1b.savefig('cf8rpo_figure1b.svg')