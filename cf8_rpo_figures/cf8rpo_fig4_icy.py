## Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

## Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
## Gregory A. de Wet, Benjamin V. Gaglioti

## DOI: pending

## Code Author: Kurt R. Lindberg

### Figure 4 ###
## (a) Inverse cummulative yield plot
## (b) Inverse cummulative yield y-intercept vs bulk 14C


## See cf8_rpo_conda_env.yml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import scipy.stats
from composition_stats import closure
import pyleoclim as pyleo
from pylipd.lipd import LiPD
import cf8rpo_functions as cf8_fun


## Figure parameters for editing in Inkscape
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = "Liberation Sans"


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

rpo_depth_ens, rpo_depth = cf8_fun.getlipd(
  'Lindberg.CF8.2024.lpd',
  paleoData_variableName='RPOdepth',
  depth_name='RPOdepth',
  val_unit='cm'
)


## Calculations for CO2 amount-weighted bulk RPO, inverse CO2 cummulative yield
## CF817-03 macrofossil fraction modern values reported in Crump et al. (2021)
## DOI: https://doi.org/10.1073/pnas.2019069118
cf8_noaa_chron = pd.read_excel("Lindberg_2024_CF8_NOAA_paleoclimate.xlsm",
                         sheet_name="Chronology",
                         header=19)
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

## Convert RPO CO2 split concentrations to inverse cummulative yield
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


## Figure 4 a-b script

fig5_colors = [
  '#00441b',
  '#1b7837',
  '#5aae61',
  '#a6dba0',
  '#c2a5cf',
  '#9970ab',
  '#762a83',
  '#40004b'
]

fig, axs = plt.subplots(2,2)

## Figure 4a: Inverse cummulative yield plot
ax = axs[0,0]
for i in range(0, np.shape(icy)[0]):
    modela = LinearRegression().fit(icy[i,:].reshape((-1,1)), cf8_fun.fm_todel14c(fm_arr[i,:], yc=2021))
    icy_yint[i] = modela.intercept_
    ax.plot(
      icy[i,:], (icy[i,:]*modela.coef_+modela.intercept_),
      linestyle='--', color=fig5_colors[i], zorder=1
    )
    ax.scatter(
      icy[i,:], cf8_fun.fm_todel14c(fm_arr[i,:], yc=2021),
      marker='o', s=40, color=fig5_colors[i], edgecolors='black', zorder=2,
              label=str(rpo_depth.paleoData_values[i])
    )

ax.set_xlim([0.005,0.065])
ax.set_ylim([-850,-150])
ax.xaxis.set_label_position("top")
ax.xaxis.set_ticks_position("top")
ax.set_xlabel('Inverse Cumulative Yield (umol-1)')
ax.set_ylabel('RPO CO2 Age (14C yrs)')
ax.set_xticks(ticks=[0.01,0.02,0.03,0.04,0.05,0.06])
ax.set_yticks(ticks=[-800,-600,-400,-200])
# ax.legend(loc='center left', bbox_to_anchor=(1,0.5))

## Figure 4b: Inverse cummulative yield y-intercept vs. bulk 14C
ax = axs[1,0]
modelb = LinearRegression().fit(cf8_fun.fm_todel14c(fm_bulk, yc=2021).reshape((-1,1)), icy_yint)
bulk_corr = np.array(scipy.stats.pearsonr(cf8_fun.fm_todel14c(fm_bulk, yc=2021), icy_yint))
print("R = " + str(bulk_corr[0]) + "; p = " + str(bulk_corr[1]))
ax.plot(
  cf8_fun.fm_todel14c(fm_bulk, yc=2021), (cf8_fun.fm_todel14c(fm_bulk, yc=2021)*modelb.coef_+modelb.intercept_),
  linestyle='--', color='black', zorder=1
)
ax.scatter(
  cf8_fun.fm_todel14c(fm_bulk, yc=2021), icy_yint,
  marker='o', s=40, edgecolors='black', zorder=2,
  label="R = " + str(np.round(bulk_corr[0], decimals=3)) + "; p < 0.001"
)

ax.set_xlim([-850,-150])
ax.set_ylim([-850,-150])
ax.set_xlabel('Bulk RPO Age (14C yrs)')
ax.set_ylabel('Inverse Cumulative Yield Y-Intercept')
ax.set_xticks(ticks=[-800,-600,-400,-200])
ax.set_yticks(ticks=[-800,-600,-400,-200])
ax.legend(loc='upper left')

axs[0,0].grid(visible=False)
axs[0,1].grid(visible=False)
fig.delaxes(axs[0,1])
fig.delaxes(axs[1,1])

print(modelb.coef_)
print(modelb.intercept_)
print(bulk_corr)

figure4_d14c = plt.gcf()
# figure4_d14c.savefig('cf8rpo_fig4_d14c.svg')


