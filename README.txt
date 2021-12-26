The Modulation of the Neural Network by Different Types of Neocortical Interneurons
=======================================================================================
Writers: QuJingling, LiKai, LongZhen

This is a PyNEST implementation of the cortical microcircuit model.
The network model represents three layers of cortex, L2/3, L4, L5 each consisting of a population of excitatory neurons and three types of interneurons.


File structure
##############

* ``run_microcircuit.py``: an example script to try out the microcircuit
* ``network.py``: the main Network class with functions to build and simulate the network
* ``helpers.py``: helper functions for network construction, simulation and evaluation
* ``stimulus_params.py``: parameters for optional external stimulation
* ``sim_params.py``: simulation parameters
* ``exp1.py``: network and neuron parameters of T-IN
* ``exp2.py``: network and neuron parameters of D-IN
* ``exp3.py``: network and neuron parameters of DT-IN

Running the simulation
######################

Firstly,

1. to run the simulation of T-IN, change the 34 line of run_micorciruit.py to 'from exp1 import net_dict'
2. to run the simulation of D-IN, change the 34 line of run_micorciruit.py to 'from exp2 import net_dict'
3. to run the simulation of DT-IN, change the 34 line of run_micorciruit.py to 'from exp3 import net_dict'

To run the simulation, change the directory and type the following command in the terminal:
conda activate nest;source /home/likai/data/nest-simulator-3.1-build/bin/nest_vars.sh;python run_microcircuit.py

The output will be saved in the ``data`` directory.

Postscript
This batch of codes is based on the open library Nest. And the code construct refers to an example model called Potjan2014[1] in the NEST Library.

References
##########
[1]  Potjans TC. and Diesmann M. 2014. The cell-type specific cortical
     microcircuit: relating structure and activity in a full-scale spiking
     network model. Cerebral Cortex. 24(3):785–806. DOI: `10.1093/cercor/bhs358 <https://doi.org/10.1093/cercor/bhs358>`__.