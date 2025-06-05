# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Code Author: Kurt R. Lindberg

# Figure S10 in Supporting Information S1
# (a) Elemental Analyzer % Carbon
# (b) Elemental Analyzer Carbon:Nitrogen
# (c) Elemental Analyzer d13C
# (d) ITRAX Magnesium/Iron
# (e) Geotek Magnetic Susceptibility


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

ea_cn_ens, ea_cn = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='C/N',
    depth_name='EAdepth',
    val_unit='unitless'
)

ea_d13c_ens, ea_d13c = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='d13C',
    depth_name='EAdepth',
    val_unit='permil'
)

mnfe_ens, mnfe = cf8_fun.getlipd(
    'Lindberg.CF8.20242.lpd',
    paleoData_variableName='Mn/Fe',
    depth_name='itraxDepth',
    val_unit='unitless'
)

ms_ens, ms = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='MS',
    depth_name='geotekDepth',
    val_unit='SI'
)


# Figure S10 a-e script
fig, axs = plt.subplots(5,1)

# Figure S10a: Elemental Analyzer % Carbon
ax = axs[0]
ea_totalc_ens.common_time(
    time_axis=ea_totalc.ageMedian,
    bounds_error=False
).plot_envelope(
    ax=ax,
    curve_clr='#5e3c99',
    shade_clr='#5e3c99',
    plot_legend=False
)
ax.plot(
    ea_totalc.ageMedian, ea_totalc.paleoData_values,
    linestyle='--', color='black',
    zorder=100
)

ax.set_xlim([12500,0])
ax.set_ylim([0,16])
ax.set_xticks([])
ax.set_yticks(ticks=[0,4,8,12,16])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel('EA %C')
ax.legend([])
ax.grid(visible=False)

# Figure S10b: Elemental Analyzer Carbon:Nitrogen
ax = axs[1]
ea_cn_ens.common_time(
    time_axis=ea_cn.ageMedian,
    bounds_error=False
).plot_envelope(
    ax=ax,
    curve_clr='#4dac26',
    shade_clr='#4dac26',
    plot_legend=False
)
ax.plot(
    ea_cn.ageMedian, ea_cn.paleoData_values,
    linestyle='--', color='black',
    zorder=100
)

ax.set_xlim([12500,0])
ax.set_ylim([8,16])
ax.set_xticks([])
ax.set_yticks(ticks=[8,10,12,14,16])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel('EA C:N')
ax.yaxis.set_label_position("right")
ax.yaxis.set_ticks_position("right")
ax.legend([])
ax.grid(visible=False)

# Figure S10c: Elemental Analyzer d13C
ax = axs[2]
ea_d13c_ens.common_time(
    time_axis=ea_d13c.ageMedian,
    bounds_error=False
).plot_envelope(
    ax=ax,
    curve_clr='#d7191c',
    shade_clr='#d7191c',
    plot_legend=False
)
ax.plot(
    ea_d13c.ageMedian, ea_d13c.paleoData_values,
    linestyle='--', color='black',
    zorder=100
)

ax.set_xlim([12500,0])
ax.set_ylim([-35,-15])
ax.set_xticks([])
ax.set_yticks(ticks=[-35,-30,-25,-20,-15])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel('EA d13C (permil)')
ax.legend([])
ax.grid(visible=False)

# Figure S10d: ITRAX Magnesium/Iron
ax = axs[3]
mnfe_ens.common_time(
    time_axis=mnfe.ageMedian,
    bounds_error=False
).plot_envelope(
    ax=ax,
    curve_clr='#993404',
    shade_clr='#993404',
    plot_legend=False
)
# ax.plot(mnfe.ageMedian, mnfe.paleoData_values, linestyle='--', color='black', zorder=100)

ax.set_xlim([12500,0])
ax.set_ylim([0,0.008])
ax.set_xticks([])
ax.set_yticks([0,0.002,0.004,0.006,0.008])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel('Mn/Fe')
ax.yaxis.set_label_position("right")
ax.yaxis.set_ticks_position("right")
ax.legend([])
ax.grid(visible=False)

# Figure S10e: Geotek Magnetic Susceptibility
ax = axs[4]
ms_ens.common_time(
    time_axis=ms.ageMedian,
    bounds_error=False
).plot_envelope(
    ax=ax,
    curve_clr='gray',
    shade_clr='gray',
    plot_legend=False
)
ax.plot(
    ms.ageMedian, ms.paleoData_values,
    linewidth=1, linestyle='--', color='black',
    zorder=100
)

ax.set_xlim([12500,0])
ax.set_ylim([-10,150])
ax.set_xticks(
    ticks=[12000,11000,10000,9000,8000,7000,6000,5000,4000,3000,2000,1000,0],
    labels=[12000,"",10000,"",8000,"",6000,"",4000,"",2000,"",0]
)
ax.set_yticks(ticks=[0,50,100,150])
ax.set_xlabel('Age (cal yr BP)')
ax.set_ylabel('MS')
ax.legend([])
ax.grid(visible=False)

figs10 = plt.gcf()
# figs10.savefig('cf8rpo_figs10_geochem.svg')
