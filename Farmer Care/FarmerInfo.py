from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
class FarmerInfo:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Farmer Care Portal")

        img3=Image.open(r"C:\Users\Janak Limbachia\Farmer Care\FarmerInfo.png")
        img3=img3.resize((1530,900),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=900)

if __name__=="__main__":
    root=Tk()
    obj=FarmerInfo(root)
    root.mainloop()