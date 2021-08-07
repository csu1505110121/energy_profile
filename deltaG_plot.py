#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools

class DeltaG_plot():


	def __init__(self,_x_ticks,y,color,path_labels,\
					TextLabel='True',FontSize=18,figsize=(12,6),\
					linew=3,dlinew=1,\
					xlabel='Reaction Pathway',ylabel='Free Energy (eV)',\
					output='example.png'):
		self._x_ticks = _x_ticks
		self.x = [i*2+1.5 for i in range(len(_x_ticks))]
		self.y = y
		self.color = color
		self.TextLabel = TextLabel
		self.fontsize=FontSize
		self.path_labels= path_labels
		self.figsize = figsize
		self.linew=linew
		self.dlinew=dlinew
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.output = output

	def flatten(self):
		out = list(itertools.chain.from_iterable(self.y))
		return out

	def min_max(self):
		"""
		return the min and max value of input list
		"""
		temp = self.flatten()
		temp = [i for i in temp if i != ""] # trim the empty value
		ymin, ymax = min(temp), max(temp)
		
		#return ymin, ymax
		self.ymin = ymin
		self.ymax = ymax
		return self.ymin, self.ymax

	def create_canves(self):
		f, ax = plt.subplots(figsize=self.figsize)
		self.f =f
		self.ax =ax
		#return f, ax

	def set_label(self):
		ymin,ymax = self.min_max()

		y_inter = round((ymax -ymin)/5)

		self.ax.set_ylim(round(ymin-y_inter,1),round(ymax+y_inter,1))

		plt.xticks(self.x, self._x_ticks,fontsize=self.fontsize)
		#self.ax.yaxis.set_ticks(np.arange(ymin,ymax,y_inter))		
		self.ax.yaxis.set_ticks(np.arange(round(ymin-y_inter,1),round(ymax+y_inter,1),y_inter))

		# set the labelsize for x and y axis
		self.ax.xaxis.set_tick_params(labelsize=16)
		self.ax.yaxis.set_tick_params(labelsize=16)

		# set the xlabel and y label
		self.ax.set_xlabel(self.xlabel,fontsize=self.fontsize,fontfamily='sans-serif',labelpad=10)
		self.ax.set_ylabel(self.ylabel,fontsize=self.fontsize,fontfamily='sans-serif',labelpad=10)

	def xy_new(self,yi):
		# generate the horizontal lines
		self.yi = yi
		y_new = []
		x_new = []
		for i,ene in enumerate(self.yi):
			if ene != "":
				y_new.append(ene)
				y_new.append(ene)
				x_new.append(2*i+1)
				x_new.append(2*i+2) # should be add an arg to specify the line length
		self.x_new = x_new
		self.y_new = y_new
		return x_new, y_new


	def add_line(self):
		"""
		add horizontal line for each stable state
		"""
		ymin,ymax = self.min_max()
		y_bias = (ymax -ymin)/25

		if isinstance(self.y, list):
			for paths_idx in range(len(self.y)):
				# generate the horizontal lines
				x_new,y_new = self.xy_new(self.y[paths_idx])
				
				# plot lines generated above
				i = 0
				while i < len(y_new):
					xl = [x_new[i],x_new[i+1]]
					yl = [y_new[i],y_new[i+1]]
				
					self.ax.plot(xl,yl, linestyle='-',linewidth=self.linew,color=self.color[paths_idx])
					i += 2
			
				# add label for energy
				if self.TextLabel == 'True':
					for i, ene in enumerate(self.y[paths_idx]):
						# here should replace 0.4 and 0.4 with left shift and up shift, respectively.
						self.ax.text(self.x[i] - 0.1, self.y[paths_idx][i] + y_bias, "{:.1f}".format(ene), fontsize=self.fontsize,color=self.color[paths_idx])
				#return x_new, y_new

	def add_connect(self):
		"""
		connect each states with dotted lines
		"""
		if isinstance(self.y, list):
			for paths_idx in range(len(self.y)):
				x_new,y_new = self.xy_new(self.y[paths_idx])
				
				i = 1
				while i < len(y_new)-1:
					xl = [x_new[i],x_new[i+1]]
					yl = [y_new[i],y_new[i+1]]
					
					if i == 1:
						self.ax.plot(self.x_new, self.y_new, linestyle='--',linewidth=self.dlinew, color=self.color[paths_idx], label=self.path_labels[paths_idx])
					else:
						self.ax.plot(self.x_new, self.y_new, linestyle='--',linewidth=self.dlinew, color=self.color[paths_idx])
					i += 2

	def plot(self):
		plt.legend(fontsize=16,loc='best')
		plt.tight_layout()
		plt.show()

	def saveplot(self):
		plt.legend(fontsize=16,loc='best')
		plt.tight_layout()
		plt.savefig(self.output,dpi=800)



if __name__ == '__main__':
	filename = '../reaction_pathway.xlsx'
	label_paths = ['$Cu111$','$1Cu_2O111+4Cu111$','$3Cu_2O111+2Cu111$','$Cu_2O111$']
	sheet_name = ['Path A','Path B','Path C','Path D']
	data = pd.read_excel(filename,header=None,usecols=[0,1],sheet_name=['Path A','Path B','Path C','Path D'])
	#print(data['Path A'])
	_x_name = data['Path A'].loc[:,0].values
	y = [data[path].loc[:,1].values for path in sheet_name]
	#print(_x_name)
	#print(y)
	colors = ['black','blue','red','grey']
	delta = DeltaG_plot(_x_name,y,color=colors,path_labels=label_paths,TextLabel='False')
	delta.min_max()
	delta.create_canves()
	delta.set_label()
	delta.add_line()
	delta.add_connect()
	#delta.plot()
	delta.saveplot()
	#print(delta.ymin)
