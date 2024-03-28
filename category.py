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
        #------variables------
        self.var_catid = StringVar()
        self.var_name = StringVar()

    #============title===============
        lbl_titel = Label(self.root, text="Quản Lý Danh Mục", font=("time new roman",30),bg="grey",fg="white",relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=2)

        lbl_name = Label(self.root, text="Nhập Danh Mục", font=("time new roman",30),bg="grey").place(x=50,y=100)
        lbl_name = Entry(self.root, textvariable= self.var_name, font=("time new roman",20),bg="lightyellow").place(x=50,y=170,width=290)

        btn_add = Button(self.root, text="Thêm", font=("time new roman",18),bg="green",fg="black", cursor="hand2").place(x=50,y=230,width=100,height=30)
        btn_delete = Button(self.root, text="Xóa", font=("time new roman",18),bg="red",fg="black", cursor="hand2").place(x=240,y=230,width=100,height=30)
    #========--category details--============
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=400,y=100,width=380,height=320)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)

        self.category_table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.category_table.yview)

        self.category_table.heading("cid",text="Mã số danh mục")
        self.category_table.heading("name",text="Tên danh mục")
        self.category_table["show"]="headings"
        self.category_table.column("cid",width=25)
        self.category_table.column("name",width=100)
        self.category_table.pack(fill=BOTH,expand=1)

        #===--image---===
        self.cat_img = Image.open("images/cat.png")
        self.cat_img = self.cat_img.resize((290, 140), Image.LANCZOS)
        self.cat_img = ImageTk.PhotoImage(self.cat_img)

        lbl_image = Label(self.root, image=self.cat_img)
        lbl_image.place(x=50, y=280)

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
 