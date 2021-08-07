#!/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def read_inp(filename='input.txt'):
	data = {}
	with open(filename,'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			else:
				var = line.split(":")[0]
				val = line.split('#')[0].split(":")[1].strip().split(',')
		#		print(var,':',val)
				if len(val) ==1:
					data[var]=val[0]
				elif len(val) >1:
					data[var] = [x.strip() for x in val]

	return data

if __name__ == "__main__":
	filename='input.txt'
	data = read_inp(filename)
	print(data)
