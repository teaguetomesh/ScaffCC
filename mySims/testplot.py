import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams.update({'font.size': 16})

fn = 'vqe_run_data/vqe_opt_out.txt'
data = np.genfromtxt(fn)

iteration = data[:,0]
energies  = data[:,1]
count00   = data[:,2]
count01   = data[:,3]
count10   = data[:,4]
count11   = data[:,5]

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True, figsize=[16,12])
ax1.plot(iteration, count00, label='00')
ax1.plot(iteration, count01, label='01')
ax1.plot(iteration, count10, label='10')
ax1.plot(iteration, count11, label='11')
ax1.legend(loc='upper right')
ax1.set_title('Nelder-Mead VQE')
ax1.set_ylabel('Counts')
ax2.plot(iteration, energies)
ax2.set_ylabel('Energy')
ax2.set_xlabel('Iteration')
ax2.text(0.97,0.9,'string', horizontalalignment='right', verticalalignment='top',
		transform=ax2.transAxes, bbox=dict(facecolor='white', alpha=0.8))
plt.show()
plt.close()
