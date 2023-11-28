import string
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from FarmerInfo import FarmerInfo
from Statistics import Statistics
from Production import Production
class Portal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Farmer Care Portal")

        img3=Image.open(r"C:\Users\Janak Limbachia\Farmer Care\BgImage.png")
        img3=img3.resize((1530,900),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=900)

        #title_lbl=Label(bg_img,text=" FARMERS CARE PORTAL ",font=("open sans",70,"bold"),fg="BLACK")
        #title_lbl.place(x=0,y=0,width=1530,height=130)

        main_frame=Frame(bg_img,bd=2,bg='')
        main_frame.place(x=5,y=145,width=1500,height=600)

        b1_1=Button(bg_img,text="STATISTICS",command=self.Statistics,cursor="hand2",font=("times new roman",20,"bold"),bg='#e8d39e',fg="black")
        b1_1.place(x=200,y=250,width=350,height=100)

        b2_2=Button(bg_img,text="PRODUCTION",command=self.Production,cursor="hand2",font=("times new roman",20,"bold"),bg='#e8d39e',fg="black")
        b2_2.place(x=650,y=250,width=350,height=100)

        b3_3=Button(bg_img,text="FARMER INFO",command=self.FarmerInfo,cursor="hand2",font=("times new roman",20,"bold"),bg='#e8d39e',fg="black")
        b3_3.place(x=1100,y=250,width=350,height=100)

    def Statistics(self):
       self.new_window=Toplevel(self.root)
       self.app=Statistics(self.new_window)

    def Production(self):
       self.new_window=Toplevel(self.root)
       self.app=Production(self.new_window)  

    def FarmerInfo(self):
       self.new_window=Toplevel(self.root)
       self.app=FarmerInfo(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Portal(root)
    root.mainloop()