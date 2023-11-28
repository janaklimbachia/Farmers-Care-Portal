import string
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

class Statistics:
    def plot (self,root):
        style.use('gplot')
        x,y = np.loadtxt('statistics.csv',
                         unpack = True,
                         delimiter= '')
        print (x)
        print (y)

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Farmer Care Portal")

        img3=Image.open(r"C:\Users\Janak Limbachia\Farmer Care\sts.png")
        img3=img3.resize((1530,900),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=900)

        main_frame=Frame(bg_img,bd=2,bg='')
        main_frame.place(x=750,y=250,width=650,height=490)
        img4=Image.open(r"C:\Users\Janak Limbachia\Farmer Care\Statistics.png")
        img4=img4.resize((640,480),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        fr_img=Label(main_frame,image=self.photoimg4)
        fr_img.place(x=0,y=0,width=640,height=480)

        left_frame=Frame(bg_img,bd=2,bg='')
        left_frame.place(x=150,y=250,width=650,height=490)
        img5=Image.open(r"C:\Users\Janak Limbachia\Farmer Care\stline.png")
        img5=img5.resize((640,480),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        fm_img=Label(left_frame,image=self.photoimg5)
        fm_img.place(x=0,y=0,width=640,height=480)

        
if __name__=="__main__":
    root=Tk()
    obj=Statistics(root)
    root.mainloop()