# -*- coding: utf-8 -*-
#
# run_microcircuit.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""PyNEST Microcircuit: Run Simulation
-----------------------------------------

This is an example script for running the microcircuit model and generating
basic plots of the network activity.

"""

###############################################################################
# Import the necessary modules and start the time measurements.
# %%
from stimulus_params import stim_dict
from exp1 import net_dict
fname = 'exp1'
from sim_params import sim_dict
import network
import helpers
import nest
import numpy as np
import time
import os
import pandas as pd
time_start = time.time()



tw=0.1
th_start=700
# for th_start in np.arange(600,900,5):
print('th_start:'+str(th_start))
stim_dict['th_start'] = th_start
net = network.Network(sim_dict, net_dict, stim_dict)
time_network = time.time()

net.create()
time_create = time.time()

net.connect()
time_connect = time.time()

net.simulate(sim_dict['t_presim'])
time_presimulate = time.time()

net.simulate(sim_dict['t_sim'])
time_simulate = time.time()

raster_plot_interval = np.array([sim_dict['t_presim'],
                                 sim_dict['t_presim'] + sim_dict['t_sim']])
firing_rates_interval = np.array([sim_dict['t_presim'],
                                  sim_dict['t_presim'] + sim_dict['t_sim']])
net.evaluate(raster_plot_interval, firing_rates_interval,tw)

    # dict={}
    # print(net.response_time)
    # print(net.response_time.tolist())
    # dict['response_time']=net.response_time.tolist()
    # dict['RT_start']=net.RT_start.tolist()
    # dict['rest_rate']=net.rest_rate.tolist()
    # dict['response_rate']=net.response_rate.tolist()
    # print(dict)
    # df = pd.DataFrame(dict,index=net_dict['populations'])
    # print(df)
    # if os.path.exists(fname+'.csv'):
    #     df.to_csv(fname+'.csv', mode='a+', header=False)
    # else:
    #     df.to_csv(fname+'.csv', mode='a+', header=True)
    # time_evaluate = time.time()

###############################################################################
# Summarize time measurements. Rank 0 usually takes longest because of the
# data evaluation and print calls.

# print(
#     '\nTimes of Rank {}:\n'.format(
#         nest.Rank()) +
#     '  Total time:          {:.3f} s\n'.format(
#         time_evaluate -
#         time_start) +
#     '  Time to initialize:  {:.3f} s\n'.format(
#         time_network -
#         time_start) +
#     '  Time to create:      {:.3f} s\n'.format(
#         time_create -
#         time_network) +
#     '  Time to connect:     {:.3f} s\n'.format(
#         time_connect -
#         time_create) +
#     '  Time to presimulate: {:.3f} s\n'.format(
#         time_presimulate -
#         time_connect) +
#     '  Time to simulate:    {:.3f} s\n'.format(
#         time_simulate -
#         time_presimulate) +
#     '  Time to evaluate:    {:.3f} s\n'.format(
#         time_evaluate -
#         time_simulate))

#%%
# helpers.plot_raster('./data/', 'spike_recorder', 500, 1000, 0.1,net_dict['populations'])