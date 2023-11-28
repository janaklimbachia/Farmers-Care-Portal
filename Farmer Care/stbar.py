from tkinter import*
from PIL import ImageTk,Image
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('statistics.csv')
print(df)
x = df['Crop']
y = df['Yield (Quintal/ Hectare) ']

plt.xlabel('Crop', fontsize=10)
plt.ylabel('Yield (Quintal/ Hectare) ', fontsize=10)
plt.bar(x, y)
plt.savefig('statistics.png')

 