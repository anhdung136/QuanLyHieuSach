from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("792x435+206+130")
        self.root.title("- 📔 - HỆ THỐNG QUẢN LÝ HIỆU SÁCH - 📚 - NHÓM 9 - 📖 - K15DCPM06 - 📝 -")
        self.root.config(bg="#FFFFEC")
        self.root.focus_force()
        #===========================================================

        product_Frame = Frame(self.root,bd=3,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=400, height=415)




if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()