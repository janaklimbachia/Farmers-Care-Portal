from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
class Production:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("Farmer Care Portal")

        img3=Image.open(r"C:\Users\Janak Limbachia\Farmer Care\Production.png")
        img3=img3.resize((1530,900),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=900)

        main_frame=Frame(bg_img,bd=2,bg='')
        main_frame.place(x=430,y=250,width=650,height=490)
        img4=Image.open(r"C:\Users\Janak Limbachia\Farmer Care\prline.png")
        img4=img4.resize((640,480),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        fr_img=Label(main_frame,image=self.photoimg4)
        fr_img.place(x=0,y=0,width=640,height=480)

        #title_lbl=Label(bg_img,text=" FARMERS CARE PORTAL ",font=("open sans",70,"bold"),fg="BLACK")
        #title_lbl.place(x=0,y=0,width=1530,height=130)

        
if __name__=="__main__":
    root=Tk()
    obj=Production(root)
    root.mainloop()