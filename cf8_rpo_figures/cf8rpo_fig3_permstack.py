## Lake CF8 RPO Figure 3
# Comparison of permafrost reconstruction methods
# RPO CO2 14C age offests, MixSIAR outputs, OC accumulation rates

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

## Import data from LiPD files
s1_conc_ens, s1_conc = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                               paleoData_variableName='split1concentration',
                               depth_name='RPOdepth',
                               val_unit='umol')

s2_conc_ens, s2_conc = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                               paleoData_variableName='split2concentration',
                               depth_name='RPOdepth',
                               val_unit='umol')

s3_conc_ens, s3_conc = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                               paleoData_variableName='split3concentration',
                               depth_name='RPOdepth',
                               val_unit='umol')

s4_conc_ens, s4_conc = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                               paleoData_variableName='split4concentration',
                               depth_name='RPOdepth',
                               val_unit='umol')

s5_conc_ens, s5_conc = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                               paleoData_variableName='split5concentration',
                               depth_name='RPOdepth',
                               val_unit='umol')

s1_fm_ens, s1_fm = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                           paleoData_variableName='split1fractionModern',
                           depth_name='RPOdepth',
                           val_unit ='unitless')

s2_fm_ens, s2_fm = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                           paleoData_variableName='split2fractionModern',
                           depth_name='RPOdepth',
                           val_unit ='unitless')

s3_fm_ens, s3_fm = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                           paleoData_variableName='split3fractionModern',
                           depth_name='RPOdepth',
                           val_unit ='unitless')

s4_fm_ens, s4_fm = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                           paleoData_variableName='split4fractionModern',
                           depth_name='RPOdepth',
                           val_unit ='unitless')

s5_fm_ens, s5_fm = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                           paleoData_variableName='split5fractionModern',
                           depth_name='RPOdepth',
                           val_unit ='unitless')

rpo_dbd_ens, rpo_dbd = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                               paleoData_variableName='dryBulkDensity',
                               depth_name='RPOdepth',
                               val_unit='g/cm3')

rpo_dbdstdev_ens, rpo_dbdstdev = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                                         paleoData_variableName='dryBulkDensityStdev',
                                         depth_name='RPOdepth',
                                         val_unit='g/cm3')

rpo_acc_ens, rpo_acc = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                               paleoData_variableName='accumulation',
                               depth_name='RPOdepth',
                               val_unit='cm/yr')

rpo_toc_ens, rpo_toc = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                               paleoData_variableName='RPOtotalOrganicCarbon',
                               depth_name='RPOdepth',
                               val_unit='percent')

mix_aqua_ens, mix_aqua = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                                 paleoData_variableName='mixsiarAquatic',
                                 depth_name='RPOdepth',
                                 val_unit='fraction')

mix_aquastdev_ens, mix_aquastdev = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                                           paleoData_variableName='mixsiarAquaticStdev',
                                           depth_name='RPOdepth',
                                           val_unit='fraction')

mix_post_ens, mix_post = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                                 paleoData_variableName='mixsiarPostglacial',
                                 depth_name='RPOdepth',
                                 val_unit='fraction')

mix_poststdev_ens, mix_poststdev = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                                           paleoData_variableName='mixsiarPostglacialStdev',
                                           depth_name='RPOdepth',
                                           val_unit='fraction')

mix_mis5_ens, mix_mis5 = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                                 paleoData_variableName='mixsiarMIS5',
                                 depth_name='RPOdepth',
                                 val_unit='fraction')

mix_mi5stdev_ens, mix_mis5stdev = cf8_fun.getlipd('Lindberg.CF8.2024.lpd',
                                          paleoData_variableName='mixsiarMIS5Stdev',
                                          depth_name='RPOdepth',
                                          val_unit='fraction')

## Calculations for CO2 amount-weighted bulk RPO, inverse CO2 cummulative yield

# CF817-03 macrofossil fraction modern values reported in Crump et al. (2021)
# DOI: https://doi.org/10.1073/pnas.2019069118
# Import macrofossil fraction modern from NOAA paleoclimate data sheet
cf8_noaa_chron = pd.read_excel("Lindberg_2024_CF8_NOAA_paleoclimate.xlsm",
                         sheet_name="Chronology",
                         header=19)
macro_fm = np.array(cf8_noaa_chron.fraction_modern)

co2_df = pd.concat([pd.Series(data=s1_conc.paleoData_values, name='s1'),
                    pd.Series(data=s2_conc.paleoData_values, name='s2'),
                    pd.Series(data=s3_conc.paleoData_values, name='s3'),
                    pd.Series(data=s4_conc.paleoData_values, name='s4'),
                    pd.Series(data=s5_conc.paleoData_values, name='s5')],
                    axis=1)

fm_df = pd.concat([pd.Series(data=s1_fm.paleoData_values, name='s1'),
                   pd.Series(data=s2_fm.paleoData_values, name='s2'),
                   pd.Series(data=s3_fm.paleoData_values, name='s3'),
                   pd.Series(data=s4_fm.paleoData_values, name='s4'),
                   pd.Series(data=s5_fm.paleoData_values, name='s5')],
                   axis=1)

co2_yield = np.array(co2_df)
fm_arr = np.array(fm_df)

icy = np.zeros(np.shape(np.array(co2_yield)))
for i in range(0, np.shape(icy)[0]):
    for j in range(0, np.shape(icy)[1]):
        icy[i, j] = 1/(np.sum(co2_yield[i, 0:j+1]))

co2_frac = closure(co2_yield)
icy_yint = np.zeros(np.shape(icy)[0])

fm_bulk = np.zeros(np.shape(icy)[0])
for i in range(0, np.shape(fm_bulk)[0]):
    fm_bulk[i] = np.sum(co2_frac[i,:]*fm_arr[i,:])/np.sum(co2_frac[i,:])

oc_acc_mean = (rpo_dbd.paleoData_values*(rpo_toc.paleoData_values*0.01)*rpo_acc.paleoData_values)*(1e4)
oc_acc_psd = ((rpo_dbd.paleoData_values+rpo_dbdstdev.paleoData_values)*(rpo_toc.paleoData_values*0.01)*rpo_acc.paleoData_values)*(1e4)
oc_acc_msd = ((rpo_dbd.paleoData_values-rpo_dbdstdev.paleoData_values)*(rpo_toc.paleoData_values*0.01)*rpo_acc.paleoData_values)*(1e4)


## Figure script
fig, axs = plt.subplots(3, 1)

ax = axs[0]
ax.scatter(s1_fm.ageMedian, (cf8_fun.fm_to14c(s1_fm.paleoData_values)-cf8_fun.fm_to14c(macro_fm)),
           marker='o', s=40, color='#2166ac', edgecolors='black', linewidths=0.75, label='Split 1', zorder=2)
ax.scatter(s2_fm.ageMedian, (cf8_fun.fm_to14c(s2_fm.paleoData_values)-cf8_fun.fm_to14c(macro_fm)),
           marker='o', s=40, color='#67a9cf', edgecolors='black', linewidths=0.75, label='Split 2', zorder=2)
ax.scatter(s3_fm.ageMedian, (cf8_fun.fm_to14c(s3_fm.paleoData_values)-cf8_fun.fm_to14c(macro_fm)),
           marker='o', s=40, color='#fddbc7', edgecolors='black', linewidths=0.75, label='Split 3', zorder=2)
ax.scatter(s4_fm.ageMedian, (cf8_fun.fm_to14c(s4_fm.paleoData_values)-cf8_fun.fm_to14c(macro_fm)),
           marker='o', s=40, color='#ef8a62', edgecolors='black', linewidths=0.75, label='Split 4', zorder=2)
ax.scatter(s5_fm.ageMedian, (cf8_fun.fm_to14c(s5_fm.paleoData_values)-cf8_fun.fm_to14c(macro_fm)),
           marker='o', s=40, color='#b2182b', edgecolors='black', linewidths=0.75, label='Split 5', zorder=2)
ax.scatter(s1_fm.ageMedian, (cf8_fun.fm_to14c(fm_bulk)-cf8_fun.fm_to14c(macro_fm)),
           marker='x', s=100, color='black', edgecolors='black', linewidths=1.5, label='Bulk Avg.', zorder=1)
ax.set_xticks([])
ax.set_xlim([12500, 0])
ax.set_ylim([-100, 2100])
ax.set_yticks(ticks=[0, 500, 1000, 1500, 2000])
ax.set_ylabel('RPO CO2 Age Offset (14C yrs)')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.6))

ax = axs[1]
ax.errorbar(mix_aqua.ageMedian, mix_aqua.paleoData_values*100, yerr=mix_aquastdev.paleoData_values*100,
            fmt='o', capsize=5, ecolor='blue', markeredgecolor='blue', markerfacecolor='blue', label='Aquatic')
ax.errorbar(mix_post.ageMedian, mix_post.paleoData_values*100, yerr=mix_poststdev.paleoData_values*100,
            fmt='o', capsize=5, ecolor='orange', markeredgecolor='orange', markerfacecolor='orange', label='Postglacial')
ax.errorbar(mix_mis5.ageMedian, mix_mis5.paleoData_values*100, yerr=mix_mis5stdev.paleoData_values*100,
            fmt='o', capsize=5, ecolor='black', markeredgecolor='black', markerfacecolor='black', label='MIS 5')
ax.set_xticks([])
ax.set_xlim([12500, 0])
ax.set_ylim([-10, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
ax.yaxis.set_label_position("right")
ax.yaxis.set_ticks_position("right")
ax.set_ylabel('MixSIAR % Contribution')
# ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

ax = axs[2]
ax.plot(mix_aqua.ageMedian, (oc_acc_mean*mix_aqua.paleoData_values),
        color='blue', linestyle='-', linewidth=1, marker='o', markersize=4, label='Aquatic')
ax.plot(mix_aqua.ageMedian, (oc_acc_msd*(mix_aqua.paleoData_values-mix_aquastdev.paleoData_values)),
        color='blue', linewidth=0)
ax.plot(mix_aqua.ageMedian, (oc_acc_psd*(mix_aqua.paleoData_values+mix_aquastdev.paleoData_values)),
        color='blue', linewidth=0)
ax.fill_between(mix_aqua.ageMedian,
                (oc_acc_msd*(mix_aqua.paleoData_values-mix_aquastdev.paleoData_values)),
                (oc_acc_psd*(mix_aqua.paleoData_values+mix_aquastdev.paleoData_values)),
                color='blue', alpha=0.15)

ax.plot(mix_post.ageMedian, (oc_acc_mean*mix_post.paleoData_values),
        color='orange', linestyle='-', linewidth=1, marker='o', markersize=4, label='Postglacial')
ax.plot(mix_post.ageMedian, (oc_acc_msd*(mix_post.paleoData_values-mix_poststdev.paleoData_values)),
        color='orange', linewidth=0)
ax.plot(mix_post.ageMedian, (oc_acc_psd*(mix_post.paleoData_values+mix_poststdev.paleoData_values)),
        color='orange', linewidth=0)
ax.fill_between(mix_post.ageMedian,
                (oc_acc_msd*(mix_post.paleoData_values-mix_poststdev.paleoData_values)),
                (oc_acc_psd*(mix_post.paleoData_values+mix_poststdev.paleoData_values)),
                color='orange', alpha=0.15)

ax.plot(mix_mis5.ageMedian, (oc_acc_mean*mix_mis5.paleoData_values),
        color='black', linestyle='-', linewidth=1, marker='o', markersize=4, label='MIS 5')
ax.plot(mix_mis5.ageMedian, (oc_acc_msd*(mix_mis5.paleoData_values-mix_mis5stdev.paleoData_values)),
        color='black', linewidth=0)
ax.plot(mix_mis5.ageMedian, (oc_acc_psd*(mix_mis5.paleoData_values+mix_mis5stdev.paleoData_values)),
        color='black', linewidth=0)
ax.fill_between(mix_mis5.ageMedian,
                (oc_acc_msd*(mix_mis5.paleoData_values-mix_mis5stdev.paleoData_values)),
                (oc_acc_psd*(mix_mis5.paleoData_values+mix_mis5stdev.paleoData_values)),
                color='black', alpha=0.15)

ax.set_xlim([12500, 0])
ax.set_xticks(ticks=[12000, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0],
              labels=[12000, "", 10000, "", 8000, "", 6000, "", 4000, "", 2000, "", 0])
ax.set_xlabel('Age (cal yr BP)')
ax.set_ylim([-1, 26])
ax.set_yticks(ticks=[0, 5, 10, 15, 20, 25])
ax.set_ylabel('OC Accumulation Rate (g OC/m2/yr)')
ax.legend(loc='center left', bbox_to_anchor=(1.05, 0.5))

axs[0].grid(visible=False)
axs[1].grid(visible=False)
axs[2].grid(visible=False)

figure3 = plt.gcf()
figure3.savefig('cf8rpo_figure3.svg')
