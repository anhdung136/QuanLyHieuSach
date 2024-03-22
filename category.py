from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("792x435+206+130")
        self.root.title("- 📔 - HỆ THỐNG QUẢN LÝ HIỆU SÁCH - 📚 - NHÓM 9 - 📖 - K15DCPM06 - 📝 -")
        self.root.config(bg="#FFFFEC")
        self.root.focus_force()
    #============title===============
        lbl_titel = Label(self.root, text="Quản Lý Danh Mục", font=("time new roman",30),bg="grey",fg="white").pack(side=TOP)


if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
 