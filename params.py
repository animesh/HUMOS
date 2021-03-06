#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This file contains all parameters used for simulation
'''

peptide_collection_size = 100 #number of modeled peptides
TIC = [1e5, 1e6, 1e7, 1e8, 1e9] #total ion current
low_mass = 350 #low mass cutoff
high_mass = 1500 #high mass cutoff
nScans = 2 #number of BoxCar scans
nBoxes = 12 #number of boxes per scan
box_overlap = 1 #overlap between boxes
LC_time = 60 #LC method length in minutes
resolutions_list = ['IT'] + [7500*(2**x) for x in range(0,6)] #list of resolutions
agc_list = [1e5, 3e5, 5e5, 1e6, 3e6, 1e7] #list of AGC targets
transients = {resolutions_list[x + 1]: 16*(2**x) + 9 for x in range(0,6)} # transients and overhead DOI: 10.1021/pr500985w
transients['IT'] = 35 #transient for ion trap
ion_models = ['equal', 'lognormal', 'lognormal-major'] #list of ion models
