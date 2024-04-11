from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk, messagebox, Text
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
        self.var_describe = StringVar() # Change to StringVar() from Text
        self.var_status = StringVar()
        self.var_img = StringVar()
        self.cat_list=[]
        self.fetch_cat()
        self.var_pid = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()


        productFrame = Frame(self.root,bd=3,relief=RIDGE)
        productFrame.place(x=10,y=10,width=400, height=415)

        #====================title================
        title = Label(productFrame, text="Quản lý thông tin sách", font=("time new roman", 15, "bold"), bg="#A9B388",  fg="#000000").pack(side=TOP,fill=X)

        #__Cột 1__
        lbl_category = Label(productFrame, text="Danh mục:", font=("time new roman", 15), fg="#000000").place(x=10,y=50)
        lbl_product_name = Label(productFrame, text="Tên sách:", font=("time new roman", 15), fg="#000000").place(x=10,y=90)
        lbl_author = Label(productFrame, text="Tác giả:", font=("time new roman", 15), fg="#000000").place(x=10,y=130)
        lbl_price = Label(productFrame, text="Giá bán:", font=("time new roman", 15), fg="#000000").place(x=10,y=170)
        lbl_describe = Label(productFrame, text="Mô tả:", font=("time new roman", 15), fg="#000000").place(x=10,y=210)
        lbl_status = Label(productFrame, text="Tình trạng:", font=("time new roman", 15), fg="#000000").place(x=10,y=290)

        #__Cột 2__
        cmb_cat = ttk.Combobox(productFrame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER, font=("time new roman",15))
        cmb_cat.place(x=110,y=50,width=270)
        cmb_cat.current(0)

        txt_name = Entry(productFrame, textvariable=self.var_name, font=("time new roman",15), bg='#FEFBF6').place(x=110, y=90, width=270)
        txt_author = Entry(productFrame, textvariable=self.var_author, font=("time new roman",15), bg='#FEFBF6').place(x=110, y=130, width=270)
        txt_price = Entry(productFrame, textvariable=self.var_price, font=("time new roman",15), bg='#FEFBF6').place(x=110, y=170, width=270)
        self.txt_describe = Text(productFrame, font=("time new roman", 15), bg='#FEFBF6', wrap=WORD, width=30, height=3)
        self.txt_describe.place(x=110, y=210, width=270, height=70)
        
        cmb_status = ttk.Combobox(productFrame, textvariable=self.var_status, values=("Sách mới", "Sách tồn kho", "Không còn sách"), state='readonly', justify=CENTER, font=("time new roman",15))
        cmb_status.place(x=110,y=290,width=270)
        cmb_status.current(0)

        #======= nút chức năng thêm xóa sửa ==========
        btn_add = Button(productFrame, text="Lưu", command=self.add, font=("time new roman", 17), bg="#1A5D1A", fg="#FAF0D7").place(x=20, y=360, width=50, height=30)
        btn_upadte = Button(productFrame, text="Sửa", command=self.update, font=("time new roman", 17), bg="#0C359E", fg="#FAF0D7").place(x=110, y=360, width=50, height=30)
        btn_delete = Button(productFrame, text="xóa", command=self.delete, font=("time new roman", 17), bg="#B70404", fg="#FAF0D7").place(x=200, y=360, width=50, height=30)
        btn_clear = Button(productFrame, text="làm mới", command=self.clear, font=("time new roman", 15), bg="#FFA447",fg="#FAF0D7").place(x=290, y=360, width=80, height=30)

        #=======------------Tìm kiếm----------- ==========
        SearchFrame = LabelFrame(self.root, text="Tìm sách", bg='white', font=("time new roman",15,"bold"), bd=2, relief=RIDGE)
        SearchFrame.place(x=420, y=10, width=360, height=90)

        cmb_search=ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Chọn", "Tên", "Tác giả"), state='readonly', justify=CENTER, font=("time new roman", 10))
        cmb_search.place(x=10, y=10, width=70)
        cmb_search.current(0)
#---- Lỗi tìm kiếm------------------------
        txt_search = Entry(SearchFrame, font=("time new roman", 15), bg="#FFFFEC")
        txt_search.place(x=95, y=8, width=200)
        
        btn_search = Button(SearchFrame, text="Tìm", command=self.search, font=("time new roman", 10, "bold"), bg="#BFEA7C", cursor="hand2")
        btn_search.place(x=305, y=8)



    #======= thông tin sách =================
        product_frame = Frame(self.root, bd=3, relief=RIDGE)
        product_frame.place(x=420, y=110, width=360, height=315)

        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(product_frame,columns=("pid", "category", "name", "author", "price", "describe","status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.config(command=self.product_table.yview)
        scrollx.config(command=self.product_table.xview)

        self.product_table.heading("pid", text=u"Mã")
        self.product_table.heading("category", text=u"Danh mục")
        self.product_table.heading("name", text=u"Tên")
        self.product_table.heading("author", text=u"Tác giả")
        self.product_table.heading("price", text=u"Giá sách")
        self.product_table.heading("describe", text=u"Mô tả")
        self.product_table.heading("status", text=u"Trạng thái")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=30)
        self.product_table.column("category", width=90)
        self.product_table.column("name", width=130)
        self.product_table.column("author", width=100)
        self.product_table.column("price", width=70)
        self.product_table.column("describe", width=100)
        self.product_table.column("status", width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def fetch_cat(self):
        self.cat_list.append("Không có")
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat = cur.fetchall()
            self.cat_list.append("Không có")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Chọn")
                for i in cat:
                    self.cat_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")

    
    #____add_____ 
    def add(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Chọn" or self.var_cat.get() == "Không có" or self.var_status.get()=="Còn" or self.var_name.get()=="":
                messagebox.showerror("Lỗi", "Hãy nhập đủ thông tin!", parent=self.root)
            else:
                cur.execute("Select * from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Lỗi", "Đã có sản phẩm này rồi", parent=self.root)
                else:
                    cur.execute("Insert into product( category, name, author, price, describe, status) values (?,?,?,?,?,?)",(
                                        self.var_cat.get(),
                                        self.var_name.get(),
                                        self.var_author.get(),
                                        self.var_price.get(),
                                        self.txt_describe.get('1.0', END),  # Change to access text from Text widget
                                        self.var_status.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Thêm", "Đã thêm sách", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")


    #____show____
    def show(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Lỗi",f"Lỗi đến từ: {str(ex)}",parent=self.root)

   
    #____get-data____
    def get_data(self,ev):
        f = self.product_table.focus()
        content = self.product_table.item(f)
        row = content['values']
        if row: 
            for value in row:
                print(str(value).encode('unicode_escape').decode('utf-8'))
            self.var_pid.set(row[0])
            self.var_cat.set(row[1])
            self.var_name.set(row[2])
            self.var_author.set(row[3])
            self.var_price.set(row[4])
            self.txt_describe.delete('1.0', END)  # Clear the text widget before setting new value
            self.txt_describe.insert(END, row[5])  # Insert text into the Text widget
            self.var_status.set(row[6])

 
   #____update____ 
    def update(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Lỗi", "Hãy chọn sách!", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Lỗi","thông tin sách không hợp lệ", parent=self.root)
                else:
                    cur.execute("UPDATE product SET category=?, name=?, author=?, price=?, describe=?, status=? WHERE pid=?",(
                            self.var_cat.get(),
                            self.var_name.get(),
                            self.var_author.get(),
                            self.var_price.get(),
                            self.txt_describe.get('1.0', END),
                            self.var_status.get(),
                            self.var_pid.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Sửa", "Đã cập nhật thành công", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")


    #____Xóa____
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Lỗi", "Hãy chọn sách muốn xóa!", parent=self.root)
            else:
                cur.execute("Select * from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Lỗi", "Không tồn tại", parent=self.root)
                else:
                    op=messagebox.askyesno("Xác nhận","Bạn muốn xóa thông tin?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where name=?",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Xóa","Đã xóa thành công",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")


    #_____Làm mới____
    def clear(self):
        self.var_cat.set("Chọn"),
        self.var_name.set(""),
        self.var_author.set(""),
        self.var_price.set(""),
        self.txt_describe.delete('1.0', END),
        self.var_status.set("Chọn")
        self.var_searchtxt.set("")
        self.show()

    #____Tìm Kiếm_____
    def search(self):
        con=sqlite3.connect(database="ims.db")
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Chọn":
                messagebox.showerror("Lỗi", "Hãy chọn trường tìm kiếm", parent=self.root)
            elif self.var_searchtxt.get()=="":
                 messagebox.showerror("Lỗi", "Hãy nhập thông tin cần tìm", parent=self.root)

            else:
                cur.execute("Select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(row)!=0:

                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("Lỗi", "không tồn tại", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Lỗi",f"Lỗi đến từ: {str(ex)}",parent=self.root)


  
if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()