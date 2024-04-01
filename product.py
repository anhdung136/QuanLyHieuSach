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
        self.var_cat = StringVar()
        self.var_name = StringVar()
        self.var_author = StringVar()
        self.var_price = StringVar()
        self.var_describe = StringVar()
        self.var_status = StringVar()
        self.var_img = StringVar()



        product_Frame = Frame(self.root,bd=3,relief=RIDGE)
        product_Frame.place(x=10,y=10,width=400, height=415)

        #====================title================
        title = Label(product_Frame, text="Quản lý thông tin sách", font=("time new roman", 15), bg="#A9B388",  fg="#000000").pack(side=TOP,fill=X)

        lbl_category = Label(product_Frame, text="Danh mục", font=("time new roman", 15), fg="#000000").place(x=10,y=60)
        lbl_product_name = Label(product_Frame, text="Tên sách", font=("time new roman", 15), fg="#000000").place(x=10,y=100)
        lbl_author = Label(product_Frame, text="Tác giả", font=("time new roman", 15), fg="#000000").place(x=10,y=140)
        lbl_price = Label(product_Frame, text="Giá bán", font=("time new roman", 15), fg="#000000").place(x=10,y=180)
        lbl_describe = Label(product_Frame, text="Mô tả", font=("time new roman", 15), fg="#000000").place(x=10,y=220)
        lbl_status = Label(product_Frame, text="Tình trạng", font=("time new roman", 15), fg="#000000").place(x=10,y=260)
        lbl_img = Label(product_Frame, text="Hình ảnh", font=("time new roman", 15), fg="#000000").place(x=10,y=300)

        txt_category = Label(product_Frame,text="Category",font=("time new roman",15), fg="#000000").place(x=10,y=60)

        #====----Tuỳ Chọn----====
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=("Select"), state='readonly', justify=CENTER, font=("time new roman",15))
        cmb_cat.place(x=150,y=60,width=180)
        cmb_cat.current(0)

if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()