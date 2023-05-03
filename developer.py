from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector   
import cv2   # open cv is a open source compatitor vision liberary where more than 1000 algo available  
import os
import csv
from tkinter import filedialog


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")# Here 0,0 for starting from where in screen
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text = "DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="darkgreen",)
        title_lbl.place(x=0,y=0,width=1550,height=50)

        img_top = Image.open("AI21.png")
        img_top = img_top.resize((1550,750),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(self.root,image = self.photoimg_top)
        f_lbl_top.place(x=0,y=50,width=1550,height=750)



        button_frame = LabelFrame(f_lbl_top,bd=2,relief = RIDGE)  # here relief is use for certain 
        button_frame.place(x=1000,y=0,width=550,height=700) 


        dev_info_lbl = Label(button_frame,text = "FACIAL BIOMETRIC SYSTEM Using PYTHON(Tkinter) & MACHINE LEARNING",font=("times new roman",10,"bold"),bg="white",fg="red")
        dev_info_lbl.place(x=0,y=5,width=550,height=50)

        dev_info_lbl = Label(button_frame,text = "Here Our Team Members",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        dev_info_lbl.place(x=0,y=55,width=550,height=50)

        dev_info_lbl = Label(button_frame,text = "1. MAYANK SHARMA               2101331540059",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        dev_info_lbl.place(x=0,y=105,width=550,height=50)

        dev_info_lbl = Label(button_frame,text = "2. MOHD SHOYEB SHEIKH     2101331540065",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        dev_info_lbl.place(x=0,y=155,width=550,height=50)

        dev_info_lbl = Label(button_frame,text = "3. RAVINS KATIYAR                2101331540084",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        dev_info_lbl.place(x=0,y=205,width=550,height=50)

        dev_info_lbl = Label(button_frame,text = "4. UDIT TYAGI                           2101331540119",font=("times new roman",15,"bold"),bg="white",fg="darkblue")
        dev_info_lbl.place(x=0,y=255,width=550,height=50)


        dev_info_lbl = Label(button_frame,text = "Special Thanks To Mr. Robin",font=("times new roman",20,"bold"),bg="white",fg="darkblue")
        dev_info_lbl.place(x=0,y=305,width=550,height=50)

        img_bottom = Image.open("AI22.png")
        img_bottom = img_bottom.resize((550,345),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl_bottom = Label(button_frame,image = self.photoimg_bottom)
        f_lbl_bottom.place(x=0,y=355,width=550,height=345)









if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()