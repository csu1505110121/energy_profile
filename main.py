#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from input_grammar import read_inp
from deltaG_plot import DeltaG_plot
import pandas as pd

# load the input parameters
# default filename is 'input.txt'
parameters = read_inp()

data = pd.read_excel(parameters['FILENAME'],header=None,usecols=[0,1],sheet_name=parameters['SHEET_NAMES'])
_x_name = data[parameters['SHEET_NAMES'][0]].loc[:,0].values
y = [data[path].loc[:,1].values for path in parameters['SHEET_NAMES']]
#print(_x_name)
print(y)
colors = parameters['COLORS']
delta = DeltaG_plot(_x_name,y,color=colors,\
						path_labels=parameters['LEGEND_NAMES'],TextLabel='False',\
						output=parameters['OUTPUT'],\
						xlabel=parameters['XLABEL'],ylabel=parameters['YLABEL'])
delta.min_max()
delta.create_canves()
delta.set_label()
delta.add_line()
delta.add_connect()
delta.saveplot()
