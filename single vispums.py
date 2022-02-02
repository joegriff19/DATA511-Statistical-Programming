# DATA 51100 - SPRING 2021
# NAME: GROUP 3
# PROGRAMMING ASSIGNMENT #6

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Imports .csv file and extracts data used for the output.
raw_data = pd.read_csv('ss13hil.csv', usecols=['HHL', 'HINCP', 'VEH', 'TAXP', 'VALP', 'WGTP', 'MRGP'],
skip_blank_lines=True)

# General setup for figure and spacing
fig, ax = plt.subplots(2, 2, figsize=(13, 7))
plt.tight_layout(pad=1.5, w_pad=1.5, h_pad=1.5)
plt.subplots_adjust(wspace=0.160, hspace=0.318)

# Pie chart for household languages.
HHL = raw_data.HHL.value_counts()
labels = ['English Only', 'Spanish', 'Other Indo-European', 'Asian and Pacific Island languages', 'Other']
ax[0, 0].pie(HHL, startangle=243, radius=1.2)
ax[0, 0].set_title('Household Languages')
ax[0, 0].set_ylabel('HHL')
ax[0, 0].legend(labels, prop={'size': 7}, loc='upper left')

# Histogram with KDE plot of household income.
HINCP = raw_data.HINCP.dropna().tolist()
kde = stats.gaussian_kde(HINCP)
kde_range = np.linspace(0, max(HINCP), num=1000)
ax[0, 1].hist(HINCP, bins=np.logspace(np.log10(10), np.log10(10**7), 100), density=True, color='green', alpha=.5)
ax[0, 1].set_xscale("log")
ax[0, 1].set_title('Distribution of Household Income')
ax[0, 1].set_ylabel('Density')
ax[0, 1].set_xlabel('Household Income($)- Log Scaled')
ax[0, 1].set_xlim(10)
ax[0, 1].plot(kde_range, kde(kde_range), '--', color='black')
ax[0, 1].get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: '{0:.6f}'.format(x)))
ax[0, 1].grid(linestyle='--')

# Bar chart for number of cars per house that is taking PUMS data weights into consideration.
VEH = raw_data.groupby('VEH').aggregate({'WGTP': 'sum'})
ax[1, 0].bar(VEH.index, VEH.WGTP / 1000, color='r')
ax[1, 0].set_title('Vehicles Available in Households')
ax[1, 0].set_ylabel('Thousands of Households')
ax[1, 0].set_xlabel('# of Vehicles')

# Creates scatter plot of Property Taxes vs Property Value
taxp_dict = {}


def get_taxp_mapping_dict():
    taxp_dict = {}


def get_taxp_mapping_dict():
# Function to create dictionary for tax

    taxp_dict[1] = np.NaN
    taxp_dict[2] = 1
    taxp_dict[63] = 5500
    taxp_dict[64] = 6000
    taxp_dict[65] = 7000
    taxp_dict[66] = 8000
    taxp_dict[67] = 9000
    taxp_dict[68] = 10000
    counter = 50
    for key in range(3, 63):
        if key <= 22:
            taxp_dict[key] = counter
            counter += 50
        
        if key > 22:
            counter += 50
            taxp_dict[key] = counter
            counter += 50
    return taxp_dict


def convert_taxp(tax):
    # Function to convert Tax to tax amount
    get_taxp_mapping_dict()
    n = tax.count()
    for values in range(n):
        tax[values] = taxp_dict[int(tax[values])]
    return tax


# plotting the Scatter plot
sc_tax = raw_data.TAXP.fillna(1)
tax1 = convert_taxp(sc_tax)
valp = raw_data['VALP']
size = raw_data['WGTP']
color = raw_data['MRGP']
s = ax[1, 1].scatter(valp, tax1, s=size / 2, cmap='seismic', alpha=0.3, marker=".", c=color)
ax[1, 1].set_title('Property Taxes vs Property Values')
ax[1, 1].set_ylabel('Taxes($)')
ax[1, 1].set_xlabel('Property value($)')
ax[1, 1].ticklabel_format(style="plain")
ax[1, 1].set_ylim([0, 11000])
ax[1, 1].set_xlim([0, 1200000])
plt.colorbar(s, ticks=[0, 1250, 2500, 3750, 5000], label="First Mortgage Payment Monthly ($)")

# Displays output and saves copy to .png file.
plt.savefig('pums.png')
plt.show()