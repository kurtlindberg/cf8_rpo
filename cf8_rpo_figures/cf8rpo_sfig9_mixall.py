## Lake CF8 RPO Supplemental Figure 8
# Boxplots of MixSIAR results - all RPO CO2 splits and bulk averages

# Postglacial carbon cycling history of a northeastern Baffin Island lake catchment inferred from ramped pyrolysis oxidation and radiocarbon dating

# Manuscript authors: Kurt R. Lindberg, Elizabeth K. Thomas, Brad E. Rosenheim, Gifford H. Miller, Julio Sepulveda, Devon R. Firesinger,
# Gregory A. de Wet, Benjamin V. Gaglioti

# DOI: pending

# Author: Kurt R. Lindberg
# Last edited: 09/25/2024

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from composition_stats import closure
import pyleoclim as pyleo
from pylipd.lipd import LiPD
import cf8rpo_functions as cf8_fun

plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = "sans-serif"

# Import spreadsheet of all MixSIAR quantile results
mixsiar_all = pd.read_excel('cf8rpo_mixsiar_allout.xlsx')

# Figure script
fig, axs = plt.subplots(4, 2)

ax = axs[0, 0]
sns.boxplot(ax=ax, x=mixsiar_all.q1_split, y=(mixsiar_all.fc1)*100, hue=mixsiar_all.q1_end,
            palette=['blue', 'orange', 'black'], saturation=1, linewidth=0.75)
sns.boxplot(ax=ax, x=mixsiar_all.m1_split, y=(mixsiar_all.m1)*100, hue=mixsiar_all.m1_end,
            showmeans=True, meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black","markersize":"2.5"})
ax.set_ylim([-5, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel('MixSIAR % Contribution')
ax.legend([])
ax.grid(visible=False)

ax = axs[0, 1]
sns.boxplot(ax=ax, x=mixsiar_all.q2_split, y=(mixsiar_all.fc2)*100, hue=mixsiar_all.q2_end,
            palette=['blue', 'orange', 'black'], saturation=1, linewidth=0.75)
sns.boxplot(ax=ax, x=mixsiar_all.m2_split, y=(mixsiar_all.m2)*100, hue=mixsiar_all.m2_end,
            showmeans=True, meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black","markersize":"2.5"})
ax.set_ylim([-5, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel("")
ax.legend([])
ax.grid(visible=False)

ax = axs[1, 0]
sns.boxplot(ax=ax, x=mixsiar_all.q3_split, y=(mixsiar_all.fc3)*100, hue=mixsiar_all.q3_end,
            palette=['blue', 'orange', 'black'], saturation=1, linewidth=0.75)
sns.boxplot(ax=ax, x=mixsiar_all.m3_split, y=(mixsiar_all.m3)*100, hue=mixsiar_all.m3_end,
            showmeans=True, meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black","markersize":"2.5"})
ax.set_ylim([-5, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel("")
ax.legend([])
ax.grid(visible=False)

ax = axs[1, 1]
sns.boxplot(ax=ax, x=mixsiar_all.q4_split, y=(mixsiar_all.fc4)*100, hue=mixsiar_all.q4_end,
            palette=['blue', 'orange', 'black'], saturation=1, linewidth=0.75)
sns.boxplot(ax=ax, x=mixsiar_all.m4_split, y=(mixsiar_all.m4)*100, hue=mixsiar_all.m4_end,
            showmeans=True, meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black","markersize":"2.5"})
ax.set_ylim([-5, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel("")
ax.legend([])
ax.grid(visible=False)

ax = axs[2, 0]
sns.boxplot(ax=ax, x=mixsiar_all.q5_split, y=(mixsiar_all.fc5)*100, hue=mixsiar_all.q5_end,
            palette=['blue', 'orange', 'black'], saturation=1, linewidth=0.75)
sns.boxplot(ax=ax, x=mixsiar_all.m5_split, y=(mixsiar_all.m5)*100, hue=mixsiar_all.m5_end,
            showmeans=True, meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black","markersize":"2.5"})
ax.set_ylim([-5, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel("")
ax.legend([])
ax.grid(visible=False)

ax = axs[2, 1]
sns.boxplot(ax=ax, x=mixsiar_all.q6_split, y=(mixsiar_all.fc6)*100, hue=mixsiar_all.q6_end,
            palette=['blue', 'orange', 'black'], saturation=1, linewidth=0.75, fliersize=2.5)
sns.boxplot(ax=ax, x=mixsiar_all.m6_split, y=(mixsiar_all.m6)*100, hue=mixsiar_all.m6_end,
            showmeans=True, meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black","markersize":"2.5"})
ax.set_ylim([-5, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
ax.set_xticklabels("")
ax.set_xlabel("")
ax.set_ylabel("")
ax.legend([])
ax.grid(visible=False)

ax = axs[3, 0]
sns.boxplot(ax=ax, x=mixsiar_all.q7_split, y=(mixsiar_all.fc7)*100, hue=mixsiar_all.q7_end,
            palette=['blue', 'orange', 'black'], saturation=1, linewidth=0.75)
sns.boxplot(ax=ax, x=mixsiar_all.m7_split, y=(mixsiar_all.m7)*100, hue=mixsiar_all.m7_end,
            showmeans=True, meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black","markersize":"2.5"})
ax.set_ylim([-5, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
# ax.set_xticklabels("")
ax.set_xlabel('RPO CO2 Split')
ax.set_ylabel("")
ax.legend([])
ax.grid(visible=False)

ax = axs[3, 1]
sns.boxplot(ax=ax, x=mixsiar_all.q8_split, y=(mixsiar_all.fc8)*100, hue=mixsiar_all.q8_end,
            palette=['blue', 'orange', 'black'], saturation=1, linewidth=0.75)
sns.boxplot(ax=ax, x=mixsiar_all.m8_split, y=(mixsiar_all.m8)*100, hue=mixsiar_all.m8_end,
            showmeans=True, meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black","markersize":"2.5"})
ax.set_ylim([-5, 100])
ax.set_yticks(ticks=[0, 25, 50, 75, 100])
# ax.set_xticklabels("")
ax.set_xlabel('RPO CO2 Split')
ax.set_ylabel("")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.grid(visible=False)

figures8 = plt.gcf()
# figures8.savefig('cf8rpo_figures8.svg')