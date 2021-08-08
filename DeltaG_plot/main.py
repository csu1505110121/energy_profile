#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from DeltaG_plot.input_grammar import read_inp
from DeltaG_plot.deltaG_plot import DeltaG_plot
import pandas as pd


def plot(filename):
	# load the input parameters
	# default filename is 'input.txt'
	parameters = read_inp(filename)
	
	data = pd.read_excel(parameters['FILENAME'],header=None,usecols=[0,1],sheet_name=parameters['SHEET_NAMES'])
	_x_name = data[parameters['SHEET_NAMES'][0]].loc[:,0].values
	y = [data[path].loc[:,1].values for path in parameters['SHEET_NAMES']]
	#print(_x_name)
	#print(y)
	colors = parameters['COLORS']
	delta = DeltaG_plot(_x_name,y,color=colors,\
							path_labels=parameters['LEGEND_NAMES'],\
							specified_params=parameters)
	
	#print(delta.params)
	#print(delta.ymax)
	delta.min_max()
	delta.create_canves()
	delta.set_label()
	delta.add_line()
	delta.add_connect()
	delta.plot()

def saveplot(filename):
	# load the input parameters
	# default filename is 'input.txt'
	parameters = read_inp(filename)
	
	data = pd.read_excel(parameters['FILENAME'],header=None,usecols=[0,1],sheet_name=parameters['SHEET_NAMES'])
	_x_name = data[parameters['SHEET_NAMES'][0]].loc[:,0].values
	y = [data[path].loc[:,1].values for path in parameters['SHEET_NAMES']]
	#print(_x_name)
	#print(y)
	colors = parameters['COLORS']
	delta = DeltaG_plot(_x_name,y,color=colors,\
							path_labels=parameters['LEGEND_NAMES'],\
							specified_params=parameters)
	
	#print(delta.params)
	#print(delta.ymax)
	delta.min_max()
	delta.create_canves()
	delta.set_label()
	delta.add_line()
	delta.add_connect()
	delta.saveplot()
