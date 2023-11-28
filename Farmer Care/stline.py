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

with open('statistics.csv','r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for column in lines:
		x.append(column[1])
		y.append(column[4])

plt.plot(x, y, color = 'g', linestyle = 'dashed',
		marker = 'o',label = "2010-11")

plt.xticks(rotation = 25)
plt.xlabel('State')
plt.ylabel('Cost of Production (`/Quintal) C2')
plt.title('2010-11', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
plt.savefig('prod.png')

