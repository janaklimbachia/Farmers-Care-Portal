from tkinter import*
from PIL import ImageTk,Image
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

x = ['Crop']
y = ['Production 2010-11']

with open('production.csv.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for column in lines:
		x.append(column[0])
		y.append(column[5])

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "Production")

plt.xticks(rotation = 25)
plt.xlabel('')
plt.ylabel('')
plt.title('Production', fontsize = 20)
plt.grid()
plt.legend()
plt.show()