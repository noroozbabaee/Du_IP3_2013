# Author : Leyla Noroozbabaee
# Bioengineering Institute
# The University of Auckland
# Date: 5/10/2021

# To reproduce the data needed for Figure 1A in associated original paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:

#  In [1]: cd path/to/folder_this_file_is_in
#  In [2]: run Fig1_sim_modified.py

import opencor as oc
import numpy as np
prefilename = 'Fig1_A%s' %'_no_Istim'
I_stim = 0
#
if I_stim:
    prefilename = 'Fig1_A%s' %'_no_Istim'
else:
    prefilename = 'Fig1_A'

simfile = 'New_IP3_Du_2013.sedml'
simulation = oc.open_simulation(simfile)
data = simulation.data()
# Reset states and parameters
simulation.reset(True)
# Set constant parameter values
start = 0
end = 90000
pointInterval = 0.1
data.set_starting_point(start)
data.set_ending_point(end)
data.set_point_interval(pointInterval)

if I_stim:
    data.constants()['vm/I_clamp'] = 0
else:
    data.constants()['vm/I_clamp'] = 10

# Run simulation
simulation.run()
# Access simulation results
results = simulation.results()
# Grab the selected results
varName = np.array([ "time", "v_m", "I_stim"])
vars = np.reshape(varName, (1, 3))
rows = end * 10 + 1
print(rows)
r = np.zeros((rows, len(varName)))

r[:,0] = results.voi().values()
r[:,1] = results.states()['vm/v_m'].values()
r[:,2] = results.algebraic()['vm/I_stim'].values()

# Save the data
filename = '%s.csv' % prefilename
np.savetxt(filename, vars, fmt='%s', delimiter=",")
with open(filename, "ab") as f:
    np.savetxt(f, r, delimiter=",")
f.close
