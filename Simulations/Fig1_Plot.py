import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt


prefilename = 'Fig1_A'
filename = '%s.csv' % prefilename
data = pd.read_csv(filename)
time = data [ 'time' ]
vm = data [ 'v_m' ]
I_stim = data [ 'I_stim' ]

prefilename1 = 'Fig1_A_no_Istim'
filename1 = '%s.csv' % prefilename1
data0 = pd.read_csv(filename1)

vm_no_Istim = data0 [ 'v_m' ]
time = time / 1000

fig, axs = plt.subplots(2)
labelfontsize = 12
axs [ 0 ].plot(time, vm, '-.k', time, vm_no_Istim, 'k')
axs [ 1 ].plot(time, I_stim, 'k')
axs [ 0 ].set_ylabel('$V_{m}$ (mV)', fontsize=labelfontsize)
axs [ 1 ].set_ylabel('$I_{s} (\mu A)$', fontsize=labelfontsize)
axs [ 1 ].set_xlabel('Time (s)', fontsize=labelfontsize)
axs [ 0 ].axis([ 0, 90, -80, -30 ])
axs [ 1 ].axis([ 0, 90, 0, 20 ])
plt.show()  #

# plt.savefig('Figure_1')
