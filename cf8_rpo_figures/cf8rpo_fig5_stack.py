## Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

## Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
## Gregory A. de Wet, Benjamin V. Gaglioti

## DOI: pending

## Code Author: Kurt R. Lindberg

### Figure 5 ###
## (a) Permafrost endmember OC mass accumulation rates
## (b) Chironomid cold taxa relative summer temperature
## (c) Agassiz ice cap d18O temperature
## (d) Elemental Analyzer % Carbon
## (e) Chironomid head capsule concentration
## (f) Elemental Analyzer Carbon:Nitrogen
## (g) Magnetic susceptibility


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
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = "sans-serif"


## Import data from LiPD files
s1_conc_ens, s1_conc = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='split1concentration',
  depth_name='RPOdepth',
  val_unit='umol'
)
s2_conc_ens, s2_conc = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='split2concentration',
  depth_name='RPOdepth',
  val_unit='umol'
)
s3_conc_ens, s3_conc = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='split3concentration',
  depth_name='RPOdepth',
  val_unit='umol'
)
s4_conc_ens, s4_conc = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='split4concentration',
  depth_name='RPOdepth',
  val_unit='umol'
)
s5_conc_ens, s5_conc = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='split5concentration',
  depth_name='RPOdepth',
  val_unit='umol'
)

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

mix_aqua_ens, mix_aqua = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='mixsiarAquatic',
  depth_name='RPOdepth',
  val_unit='fraction'
)
mix_aquastdev_ens, mix_aquastdev = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='mixsiarAquaticStdev',
  depth_name='RPOdepth',
  val_unit='fraction'
)

mix_post_ens, mix_post = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='mixsiarPostglacial',
  depth_name='RPOdepth',
  val_unit='fraction'
)
mix_poststdev_ens, mix_poststdev = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='mixsiarPostglacialStdev',
  depth_name='RPOdepth',
  val_unit='fraction'
)

mix_mis5_ens, mix_mis5 = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='mixsiarMIS5',
  depth_name='RPOdepth',
  val_unit='fraction'
)
mix_mi5stdev_ens, mix_mis5stdev = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='mixsiarMIS5Stdev',
  depth_name='RPOdepth',
  val_unit='fraction'
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

rpo_acc_ens, rpo_acc = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='accumulation',
  depth_name='RPOdepth',
  val_unit='cm/yr'
)

rpo_toc_ens, rpo_toc = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='RPOtotalOrganicCarbon',
  depth_name='RPOdepth',
  val_unit='percent'
)

cf8_chir_lt10_ens, cf8_chir_lt10 = cf8_fun.getlipd(
  'Axford.CF8.2009.lpd',
  paleoData_variableName='midgeOptimaLt10C',
  depth_name='chrDepth',
  val_unit='percent'
)

cf8_chir_headcount_ens, cf8_chir_headcount = cf8_fun.getlipd(
  'Axford.CF8.2009.lpd',
  paleoData_variableName='midgeHeadCapsuleCount',
  depth_name='chrDepth',
  val_unit='cc wet sediment'
)

ea_cn_ens, ea_cn = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='C/N',
  depth_name='EAdepth',
  val_unit='unitless'
)

ea_totalc_ens, ea_totalc = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='totalCarbon',
  depth_name='EAdepth',
  val_unit='percent'
)

ms_ens, ms = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='MS',
  depth_name='geotekDepth',
  val_unit='SI'
)


## Calculations for CO2 amount-weighted bulk RPO, inverse CO2 cummulative yield
# CF817-03 macrofossil fraction modern values reported in Crump et al. (2021)
# DOI: https://doi.org/10.1073/pnas.2019069118
cf8_noaa_chron = pd.read_excel(
  "Lindberg_2024_CF8_NOAA_paleoclimate.xlsm",
  sheet_name="Chronology",
  header=19
)
macro_fm = np.array(cf8_noaa_chron.fraction_modern)

co2_df = pd.concat(
  [
    pd.Series(data=s1_conc.paleoData_values, name='s1'),
    pd.Series(data=s2_conc.paleoData_values, name='s2'),
    pd.Series(data=s3_conc.paleoData_values, name='s3'),
    pd.Series(data=s4_conc.paleoData_values, name='s4'),
    pd.Series(data=s5_conc.paleoData_values, name='s5')
  ], axis=1
)
fm_df = pd.concat(
  [
    pd.Series(data=s1_fm.paleoData_values, name='s1'),
    pd.Series(data=s2_fm.paleoData_values, name='s2'),
    pd.Series(data=s3_fm.paleoData_values, name='s3'),
    pd.Series(data=s4_fm.paleoData_values, name='s4'),
    pd.Series(data=s5_fm.paleoData_values, name='s5')
  ], axis=1
)

co2_yield = np.array(co2_df)
fm_arr = np.array(fm_df)

## Convert RPO CO2 split concentration to inverse cummulative yield
icy = np.zeros(np.shape(np.array(co2_yield)))
for i in range(0, np.shape(icy)[0]):
    for j in range(0, np.shape(icy)[1]):
        icy[i, j] = 1/(np.sum(co2_yield[i, 0:j+1]))

co2_frac = closure(co2_yield)
icy_yint = np.zeros(np.shape(icy)[0])

## Calculate RPO CO2 concentration-weighted average Fm
fm_bulk = np.zeros(np.shape(icy)[0])
for i in range(0, np.shape(fm_bulk)[0]):
    fm_bulk[i] = np.sum(co2_frac[i,:]*fm_arr[i,:])/np.sum(co2_frac[i,:])

oc_acc_mean = (rpo_dbd.paleoData_values*(rpo_toc.paleoData_values*0.01)*rpo_acc.paleoData_values)*(1e4)
oc_acc_psd = ((rpo_dbd.paleoData_values+rpo_dbdstdev.paleoData_values)*(rpo_toc.paleoData_values*0.01)*rpo_acc.paleoData_values)*(1e4)
oc_acc_msd = ((rpo_dbd.paleoData_values-rpo_dbdstdev.paleoData_values)*(rpo_toc.paleoData_values*0.01)*rpo_acc.paleoData_values)*(1e4)


# Import Agassiz Ice Cap d18O data from Vinther et al. (2008)
# DOI: https://doi.org/10.1029/2007JD009143
# Link to data: https://www.ncei.noaa.gov/access/paleo-search/study/11131
ag_d18o_all = pd.read_excel(
  'vinther2008renland-agassiz.xlsx',
  sheet_name='Agassiz d18O',
  skiprows=58,
  names=['age', 'a77', 'a79', 'a84', 'a87']
)
ag_d18o_avg = ag_d18o_all[['a77', 'a79', 'a84', 'a87']].mean(axis=1)


## Figure 5 a-d script
fig, axs = plt.subplots(4, 1)

## Figure 5a: Permafrost endmember OC mass accumulation rates 
ax = axs[0]
ax.plot(
  mix_post.ageMedian, (oc_acc_mean*mix_post.paleoData_values),
  color='orange', linestyle='-', linewidth=1, marker='o', markersize=4, label='Postglacial'
)
ax.plot(
  mix_post.ageMedian, (oc_acc_msd*(mix_post.paleoData_values-mix_poststdev.paleoData_values)),
  color='orange', linewidth=0
)
ax.plot(
  mix_post.ageMedian, (oc_acc_psd*(mix_post.paleoData_values+mix_poststdev.paleoData_values)),
  color='orange', linewidth=0
)
ax.fill_between(
  mix_post.ageMedian,
  (oc_acc_msd*(mix_post.paleoData_values-mix_poststdev.paleoData_values)),
  (oc_acc_psd*(mix_post.paleoData_values+mix_poststdev.paleoData_values)),
  color='orange', alpha=0.15
)
ax.plot(
  mix_mis5.ageMedian, (oc_acc_mean*mix_mis5.paleoData_values),
  color='black', linestyle='-', linewidth=1, marker='o', markersize=4, label='MIS 5'
)
ax.plot(
  mix_mis5.ageMedian, (oc_acc_msd*(mix_mis5.paleoData_values-mix_mis5stdev.paleoData_values)),
  color='black', linewidth=0
)
ax.plot(
  mix_mis5.ageMedian, (oc_acc_psd*(mix_mis5.paleoData_values+mix_mis5stdev.paleoData_values)),
  color='black', linewidth=0
)
ax.fill_between(
  mix_mis5.ageMedian,
  (oc_acc_msd*(mix_mis5.paleoData_values-mix_mis5stdev.paleoData_values)),
  (oc_acc_psd*(mix_mis5.paleoData_values+mix_mis5stdev.paleoData_values)),
  color='black', alpha=0.15
)

ax.set_xlim([12500, 0])
ax.set_ylim([-1, 10])
ax.set_xticks([])
ax.set_xticklabels("")
ax.set_yticks(ticks=[0, 2.5, 5, 7.5, 10])
ax.set_ylabel('OC Accumulation Rate (g OC/m2/yr)')
ax.legend([])
ax.grid(visible=False)

## Figure 5b: Chironomid cold taxa relative summer temperature
ax = axs[1]
cf8_chir_lt10_ens.common_time(
  time_axis=cf8_chir_lt10.ageMedian,
  bounds_error=False
).plot_envelope(
  ax=ax,
  curve_clr='#d7191c',
  shade_clr='#d7191c',
  plot_legend=False
)
ax.plot(
  cf8_chir_lt10.ageMedian, cf8_chir_lt10.paleoData_values,
  linewidth=1, linestyle='--', color='black', zorder=100
)

ax.set_xlim([12500, 0])
ax.set_ylim([50, 0])
ax.set_xticks([])
ax.set_xticklabels("")
ax.set_yticks(ticks=[0, 12.5, 25, 37.5, 50])
ax.set_xlabel("")
ax.set_ylabel('Chironomid Taxa % <10 C Optima')
ax.yaxis.set_label_position("right")
ax.yaxis.set_ticks_position("right")
ax.legend([])
ax.grid(visible=False)

## Figure 5c: Agassiz ice cap d18O temperature
ax = axs[2]
ax.plot(
  (ag_d18o_all.age-50), ag_d18o_avg,
  color='black', linewidth=1
)

ax.set_xlim([12500, 0])
ax.set_ylim([-30, -25])
ax.set_xticks([])
ax.set_xticklabels("")
ax.set_yticks(ticks=[-25, -26.25, -27.5, -28.75, -30])
ax.set_xlabel("")
ax.set_ylabel("Aggasiz Ice Core d18O (permil)")
ax.grid(visible=False)

## Figure 5d: Elemental Analyzer % Carbon
ax = axs[3]
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
  linewidth=1, linestyle='--', color='black', zorder=100
)

ax.set_xlim([12500, 0])
ax.set_ylim([0, 16])
ax.set_xticks([])
ax.set_yticks(ticks=[0, 4, 8, 12, 16])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel('% C')
ax.yaxis.set_label_position("right")
ax.yaxis.set_ticks_position("right")
ax.legend([])
ax.grid(visible=False)

figure5_1 = plt.gcf()
# figure5_1.savefig('cf8rpo_figure5_1.svg')


## Figure 5 e-g script
fig, axs = plt.subplots(4, 1)

## Figure 5e: Chironomid head capsule concentration
ax = axs[0]
cf8_chir_headcount_ens.common_time(
  time_axis=cf8_chir_headcount.ageMedian,
  bounds_error=False
).plot_envelope(ax=ax,
  curve_clr='blue',
  shade_clr='blue',
  plot_legend=False
)
ax.plot(
  cf8_chir_headcount.ageMedian, cf8_chir_headcount.paleoData_values,
  linewidth=1, linestyle='--', color='black', zorder=100
)

ax.set_xlim([12500, 0])
ax.set_ylim([0, 600])
ax.set_xticks([])
ax.set_yticks(ticks=[0, 200, 400, 600])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel('Chironomid Head Capsuled per cc wet sed.')
ax.legend([])
ax.grid(visible=False)

## Figure 5f: Elemental Analyzer Carbon:Nitrogen
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
  linewidth=1, linestyle='--', color='black', zorder=100
)

ax.set_xlim([12500, 0])
ax.set_ylim([8 ,16])
ax.set_xticks([])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_yticks(ticks=[8, 10, 12, 14, 16])
ax.yaxis.set_label_position("right")
ax.yaxis.set_ticks_position("right")
ax.legend([])
ax.grid(visible=False)

## Figure 5g: Magnetic susceptibility
ax = axs[2]
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
  linewidth=1, linestyle='--', color='black', zorder=100
)

ax.set_xlim([12500, 0])
ax.set_ylim([0, 150])
ax.set_xticks(ticks=[12000, 11000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0],
              labels=[12000, "", 10000, "", 8000, "", 6000, "", 4000, "", 2000, "", 0])
ax.set_yticks(ticks=[0, 50, 100, 150])
ax.set_xlabel('Age (cal yr BP)')
ax.legend([])
ax.grid(visible=False)

fig.delaxes(axs[3])

figure5_2 = plt.gcf()
# figure5_2.savefig('cf8rpo_figure5_2.svg')
