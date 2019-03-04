#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib


# Take in the name of the data file to plot
fn = sys.argv[1]

data = np.genfromtxt(fn)

nucdis = data[:,0]
energy = data[:,1]

nucdis_pm = [r*90 for r in nucdis]

matplotlib.rcParams.update({'font.size': 16})

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=False, figsize=[16,12])
ax1.scatter(nucdis_pm, energy, label='<H>')
ax1.legend(loc='upper right')
titleStr = 'Powell-VQE, H=II+IX+IZ+XI+XX+XZ+ZI+ZX+ZZ'
ax1.set_title(titleStr)
ax1.set_ylabel('Energy (MJ/mol)')
ax1.set_xlabel('Atomic separation R (pm)')
ax2.scatter(nucdis_pm[10:65], energy[10:65])
ax2.set_ylabel('Energy (MJ/mol)')
ax2.set_xlabel('Atomic separation R (pm)')

plt.savefig('vqe_run_data/vqe_PEC_out.png')
plt.show()
plt.close()
