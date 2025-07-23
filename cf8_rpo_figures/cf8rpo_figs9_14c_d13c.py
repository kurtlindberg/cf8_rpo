# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Code Author: Kurt R. Lindberg

# Figure S9 in Supporting Information S1
# (a) RPO CO2 14C ages
# (b) RPO CO2 d13C


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
s1_fm_ens, s1_fm = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split1fractionModern',
    depth_name='RPOdepth',
    val_unit ='unitless'
)
s2_fm_ens, s2_fm = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split2fractionModern',
    depth_name='RPOdepth',
    val_unit ='unitless'
)
s3_fm_ens, s3_fm = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split3fractionModern',
    depth_name='RPOdepth',
    val_unit ='unitless'
)
s4_fm_ens, s4_fm = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split4fractionModern',
    depth_name='RPOdepth',
    val_unit ='unitless'
)
s5_fm_ens, s5_fm = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split5fractionModern',
    depth_name='RPOdepth',
    val_unit ='unitless'
)

ea_d13c_ens, ea_d13c = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='d13C',
    depth_name='EAdepth',
    val_unit='permil'
)

s1_d13c_ens, s1_d13c = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split1d13C',
    depth_name='RPOdepth',
    val_unit='permil'
)
s2_d13c_ens, s2_d13c = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split2d13C',
    depth_name='RPOdepth',
    val_unit='permil'
)
s3_d13c_ens, s3_d13c = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split3d13C',
    depth_name='RPOdepth',
    val_unit='permil'
)
s4_d13c_ens, s4_d13c = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split4d13C',
    depth_name='RPOdepth',
    val_unit='permil'
)
s5_d13c_ens, s5_d13c = cf8_fun.getlipd(
    'Lindberg.CF8.2024.lpd',
    paleoData_variableName='split5d13C',
    depth_name='RPOdepth',
    val_unit='permil'
)

# Import data from NOAA Paleoclimate data sheet
cf8_noaa_chron = pd.read_excel(
    "Lindberg_CF8_RPO_biogeochem.xlsm",
    sheet_name="Chronology",
    header=19
)

macro_fm = np.array(cf8_noaa_chron.fraction_modern)
macro_d13c = np.array(cf8_noaa_chron.d13C)

cf8_noaa_rpo = pd.read_excel(
    "Lindberg_CF8_RPO_biogeochem.xlsm",
    sheet_name="RPO_Data",
    header=48
)
cf8_noaa_soil = cf8_noaa_rpo[
    (cf8_noaa_rpo['lab_id'] == 'DB-2294') |
    (cf8_noaa_rpo['lab_id'] =='DB-2296')
]

# Not real soil ages, just to space on figure x-axis for visualization purposes
cf8soilage = np.array([-1000, -250])


# Figure S9 script
fig, axs = plt.subplots(2,1)

# Figure S9a: RPO CO2 14C
ax = axs[0]
ax.scatter(s1_fm.ageMedian, cf8_fun.fm_to14c(macro_fm), marker='s', s=30, color='black', edgecolor='black', linewidths=0.75, label='Macrofossil')
ax.scatter(s1_fm.ageMedian, cf8_fun.fm_to14c(s1_fm.paleoData_values), marker='o', s=40, color='#2166ac', edgecolor='black', linewidths=0.75, label='Split 1')
ax.scatter(s2_fm.ageMedian, cf8_fun.fm_to14c(s2_fm.paleoData_values), marker='o', s=40, color='#67a9cf', edgecolor='black', linewidths=0.75, label='Split 2')
ax.scatter(s3_fm.ageMedian, cf8_fun.fm_to14c(s3_fm.paleoData_values), marker='o', s=40, color='#fddbc7', edgecolor='black', linewidths=0.75, label='Split 3')
ax.scatter(s4_fm.ageMedian, cf8_fun.fm_to14c(s4_fm.paleoData_values), marker='o', s=40, color='#ef8a62', edgecolor='black', linewidths=0.75, label='Split 4')
ax.scatter(s5_fm.ageMedian, cf8_fun.fm_to14c(s5_fm.paleoData_values), marker='o', s=40, color='#b2182b', edgecolor='black', linewidths=0.75, label='Split 5')

ax.scatter(cf8soilage, cf8_fun.fm_to14c(cf8_noaa_soil.split1_fraction_modern), marker='o', s=40, color='#2166ac', edgecolor='black', linewidths=0.75)
ax.scatter(cf8soilage, cf8_fun.fm_to14c(cf8_noaa_soil.split2_fraction_modern), marker='o', s=40, color='#67a9cf', edgecolor='black', linewidths=0.75)
ax.scatter(cf8soilage, cf8_fun.fm_to14c(cf8_noaa_soil.split3_fraction_modern), marker='o', s=40, color='#fddbc7', edgecolor='black', linewidths=0.75)
ax.scatter(cf8soilage, cf8_fun.fm_to14c(cf8_noaa_soil.split4_fraction_modern), marker='o', s=40, color='#ef8a62', edgecolor='black', linewidths=0.75)
ax.scatter(cf8soilage, cf8_fun.fm_to14c(cf8_noaa_soil.split5_fraction_modern), marker='o', s=40, color='#b2182b', edgecolor='black', linewidths=0.75)
ax.vlines(x=0, ymin=0, ymax=12500, linestyles='--', color='black')

ax.set_xlim([12500,-1500])
ax.set_xticks(
    ticks=[12000,11000,10000,9000,8000,7000,6000,5000,4000,3000,2000,1000,0],
    labels=[12000,"",10000,"",8000,"",6000,"",4000,"",2000,"",0]
)
ax.set_ylim([0,12500])
ax.set_yticks(ticks=[12000,10000,8000,6000,4000,2000,0])
ax.set_xticklabels("")
ax.set_ylabel('Age (14C yrs)')
# ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
ax.grid(visible=False)

# Figure S9b: RPO CO2 d13C
ax = axs[1]
ax.scatter(
    s1_d13c.ageMedian, macro_d13c,
    marker='s', s=30, color='black', edgecolor='black', linewidths=0.75,
    label='Macrofossil'
)
ax.scatter(
    s1_d13c.ageMedian, s1_d13c.paleoData_values,
    marker='o', s=40, color='#2166ac', edgecolor='black', linewidths=0.75,
    label='Split 1'
)
ax.scatter(
    s2_d13c.ageMedian, s2_d13c.paleoData_values,
    marker='o', s=40, color='#67a9cf', edgecolor='black', linewidths=0.75,
    label='Split 2'
)
ax.scatter(
    s3_d13c.ageMedian, s3_d13c.paleoData_values,
    marker='o', s=40, color='#fddbc7', edgecolor='black', linewidths=0.75,
    label='Split 3'
)
ax.scatter(
    s4_d13c.ageMedian, s4_d13c.paleoData_values,
    marker='o', s=40, color='#ef8a62', edgecolor='black', linewidths=0.75,
    label='Split 4'
)
ax.scatter(
    s5_d13c.ageMedian, s5_d13c.paleoData_values,
    marker='o', s=40, color='#b2182b', edgecolor='black', linewidths=0.75,
    label='Split 5'
)
ax.scatter(
    ea_d13c.ageMedian, ea_d13c.paleoData_values,
    marker='d', s=40, color='gray', edgecolor='black', linewidths=0.75,
    label='EA'
)

ax.scatter(
    cf8soilage, cf8_noaa_soil.split1_d13C,
    marker='o', s=40, color='#2166ac', edgecolor='black', linewidths=0.75
)
ax.scatter(
    cf8soilage, cf8_noaa_soil.split2_d13C,
    marker='o', s=40, color='#67a9cf', edgecolor='black', linewidths=0.75
)
ax.scatter(
    cf8soilage, cf8_noaa_soil.split3_d13C,
    marker='o', s=40, color='#fddbc7', edgecolor='black', linewidths=0.75
)
ax.scatter(
    cf8soilage, cf8_noaa_soil.split4_d13C,
    marker='o', s=40, color='#ef8a62', edgecolor='black', linewidths=0.75
)
ax.scatter(
    cf8soilage, cf8_noaa_soil.split5_d13C,
    marker='o', s=40, color='#b2182b', edgecolor='black', linewidths=0.75
)
ax.vlines(x=0, ymin=-35, ymax=-17.5, linestyles='--', colors='black')

ax.set_ylim([-35,-15])
ax.set_xlim([12500,-1500])
ax.set_xticks(
    ticks=[12000,11000,10000,9000,8000,7000,6000,5000,4000,3000,2000,1000,0],
    labels=[12000,"",10000,"",8000,"",6000,"",4000,"",2000,"",0]
)
ax.set_yticks(
    ticks=[-35,-32.5,-30,-27.5,-25,-22.5,-20,-17.5,-15],
    labels=[-35,"",-30,"",-25,"",-20,"",-15]
)
ax.set_ylabel('d13C (permil)')
ax.set_xlabel('Age (cal byr BP)')
ax.legend(loc='center left', bbox_to_anchor=(1,0.5))
ax.grid(visible=False)

figs9 = plt.gcf()
# Uncomment to save figure
# figs9.savefig('cf8rpo_figs9_14c_d13c.svg')
