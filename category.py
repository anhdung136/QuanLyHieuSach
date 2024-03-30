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
        self.var_cid = StringVar()
        self.var_name = StringVar()

    #============title===============
        lbl_titel = Label(self.root, text="Quản Lý Danh Mục", font=("time new roman",30),bg="#C6A969",fg="white",relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=2)

        lbl_name = Label(self.root, text="Nhập Danh Mục", font=("time new roman",30),bg="#FFFFEC").place(x=50,y=100)
        lbl_name = Entry(self.root, textvariable= self.var_name, font=("time new roman",20),bg="lightyellow").place(x=50,y=170,width=290)

        btn_add = Button(self.root, text="Thêm", command=self.add, font=("time new roman",18),bg="#1A5D1A",fg="#FAF0D7", cursor="hand2").place(x=50,y=230,width=100,height=30)
        btn_delete = Button(self.root, text="Xóa", command=self.delete, font=("time new roman",18),bg="#B70404",fg="#FAF0D7", cursor="hand2").place(x=240,y=230,width=100,height=30)
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
        self.category_table.column("cid",width=100)
        self.category_table.column("name",width=280)
        self.category_table.pack(fill=BOTH,expand=1)
        self.category_table.bind("<ButtonRelease-1>",self.get_data)

        #===--image---===
        self.cat_img = Image.open("images/cat.png")
        self.cat_img = self.cat_img.resize((290, 140), Image.LANCZOS)
        self.cat_img = ImageTk.PhotoImage(self.cat_img)

        lbl_image = Label(self.root, image=self.cat_img)
        lbl_image.place(x=50, y=280)

        self.show()
    #======------Chức Năng------======
    #____ADD____
    def add(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Lỗi", "Hãy nhập tên danh mục!", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Lỗi", "Đã có danh mục này rồi", parent=self.root)
                else:
                    cur.execute("INSERT INTO category (name) VALUES (?)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Thêm", "Đã thêm danh mục", parent=self.root)
                    #self.show()
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")


    #____-SHOW-____
    def show(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Lỗi",f"Lỗi đến từ: {str(ex)}",parent=self.root)


    #____-GET DATA-____
    def get_data(self,ev):
        f = self.category_table.focus()
        content = self.category_table.item(f)
        row = content['values']
        for value in row:
            print(str(value).encode('unicode_escape').decode('utf-8'))
        self.var_cid.set(row[0])
        self.var_name.set(row[1])


    #____Xóa____
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cid.get() == "":
                messagebox.showerror("Lỗi", "Hãy chọn danh mục muốn xóa!", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?", (self.var_cid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Lỗi", "Đã có lỗi, hãy thử lại", parent=self.root)
                else:
                    op=messagebox.askyesno("Xác nhận","Bạn muốn xóa danh mục?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.var_cid.get(),))
                        con.commit()
                        messagebox.showinfo("Xóa","Đã xóa thành công",parent=self.root)
                        self.show()
                        self.var_cid.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
 