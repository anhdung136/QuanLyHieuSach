from tkinter import *
from PIL import Image,ImageTk #pip install pillow

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("- - - HỆ THỐNG QUẢN LÝ HIỆU SÁCH - - - NHÓM 9 - - - K15DCPM06 - - -")
        self.create_title_label()

    def create_title_label(self):
        self.icon_title = PhotoImage(file="images/book.png")
        title = Label(self.root, text="HỆ THỐNG QUẢN LÝ HIỆU SÁCH",image=self.icon_title,compound=LEFT , font=("Arial Rounded MT Bold", 30, "bold"), bg="#B19470", fg="#F8FAE5", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

root = Tk()
obj = IMS(root)
root.mainloop()
