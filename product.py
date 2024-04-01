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
        self.var_describe = StringVar()
        self.var_status = StringVar()
        self.var_img = StringVar()


        productFrame = Frame(self.root,bd=3,relief=RIDGE)
        productFrame.place(x=10,y=10,width=400, height=415)

        #====================title================
        title = Label(productFrame, text="Quản lý thông tin sách", font=("time new roman", 15, "bold"), bg="#A9B388",  fg="#000000").pack(side=TOP,fill=X)

        #__Cột 1__
        lbl_category = Label(productFrame, text="Danh mục:", font=("time new roman", 15), fg="#000000").place(x=10,y=60)
        lbl_product_name = Label(productFrame, text="Tên sách:", font=("time new roman", 15), fg="#000000").place(x=10,y=100)
        lbl_author = Label(productFrame, text="Tác giả:", font=("time new roman", 15), fg="#000000").place(x=10,y=140)
        lbl_price = Label(productFrame, text="Giá bán:", font=("time new roman", 15), fg="#000000").place(x=10,y=180)
        lbl_describe = Label(productFrame, text="Mô tả:", font=("time new roman", 15), fg="#000000").place(x=10,y=220)
        lbl_status = Label(productFrame, text="Tình trạng:", font=("time new roman", 15), fg="#000000").place(x=10,y=300)

        txt_category = Label(productFrame,text="Danh mục:",font=("time new roman",15), fg="#000000").place(x=10,y=60)

        #__Cột 2__
        cmb_cat = ttk.Combobox(productFrame, textvariable=self.var_cat, values=("Chọn"), state='readonly', justify=CENTER, font=("time new roman",15))
        cmb_cat.place(x=110,y=60,width=270)
        cmb_cat.current(0)

        txt_name = Entry(productFrame, textvariable=self.var_name, font=("time new roman",15), bg='#FEFBF6').place(x=110, y=100, width=270)
        txt_author = Entry(productFrame, textvariable=self.var_author, font=("time new roman",15), bg='#FEFBF6').place(x=110, y=140, width=270)
        txt_price = Entry(productFrame, textvariable=self.var_price, font=("time new roman",15), bg='#FEFBF6').place(x=110, y=180, width=270)
        self.txt_describe = Text(productFrame, font=("time new roman", 15), bg='#FEFBF6', wrap=WORD, width=30, height=3)
        self.txt_describe.place(x=110, y=220, width=270, height=70)
        
        cmb_status = ttk.Combobox(productFrame, textvariable=self.var_status, values=("Còn hàng"), state='readonly', justify=CENTER, font=("time new roman",15))
        cmb_status.place(x=110,y=300,width=270)
        cmb_status.current(0)

        #======= nút chức năng thêm xóa sửa ==========
        btn_add = Button(productFrame, text="Lưu", command=self.add, font=("time new roman", 17), bg="#1A5D1A", fg="#FAF0D7").place(x=20, y=370, width=50, height=30)
        btn_upadte = Button(productFrame, text="Sửa", command=self.update, font=("time new roman", 17), bg="#0C359E", fg="#FAF0D7").place(x=110, y=370, width=50, height=30)
        btn_delete = Button(productFrame, text="xóa", command=self.delete, font=("time new roman", 17), bg="#B70404", fg="#FAF0D7").place(x=200, y=370, width=50, height=30)
        btn_clear = Button(productFrame, text="làm mới", command=self.clear, font=("time new roman", 15), bg="#FFA447",fg="#FAF0D7").place(x=290, y=370, width=80, height=30)

        #=======------------Tìm kiếm----------- ==========
        SearchFrame = LabelFrame(self.root, text="Tìm sách", bg='white', font=("time new roman",15,"bold"), bd=2, relief=RIDGE)
        SearchFrame.place(x=420, y=10, width=360, height=90)

        cmb_search=ttk.Combobox(SearchFrame, values=("Tên", "Tác giả"), state='readonly', justify=CENTER, font=("time new roman", 10))
        cmb_search.place(x=10, y=10, width=70)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame, font=("time new roman", 15),bg="#FFFFEC").place(x=95, y=8, width=200)
        btn_search=Button(SearchFrame, text ="Tìm", font=("time new roman", 10, "bold"),bg="#BFEA7C", cursor="hand2").place(x=305, y=8)


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

        self.product_table.heading("pid", text=u"Mã số")
        self.product_table.heading("category", text=u"Danh mục")
        self.product_table.heading("name", text=u"Tên")
        self.product_table.heading("author", text=u"Tác giả")
        self.product_table.heading("price", text=u"Giá sách")
        self.product_table.heading("describe", text=u"Mô tả")
        self.product_table.heading("status", text=u"Trạng thái")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=5)
        self.product_table.column("category", width=90)
        self.product_table.column("name", width=70)
        self.product_table.column("author", width=17)
        self.product_table.column("price", width=40)
        self.product_table.column("describe", width=40)
        self.product_table.column("status", width=30)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()


    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
         #____add_____ 
    def add(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Chọn" or self.var_status.get()=="Còn hàng" or self.var_name.get()=="":
                messagebox.showerror("Lỗi", "Hãy nhập đủ thông tin!", parent=self.root)
            else:
                cur.execute("Select * from product where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Lỗi", "Đã có sản phẩm này rồi", parent=self.root)
                else:
                    cur.execute("Insert into employee(empid,name,email,gender,contact,dob,utype,address,salary) values (?,?,?,?,?,?,?,?,?)",(
                                        self.var_empid.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_dob.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END), 
                                        self.var_salary.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Thêm", "Đã thêm nhân viên", parent=self.root)
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
        for value in row:
            print(str(value).encode('unicode_escape').decode('utf-8'))
        self.var_empid.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_utype.set(row[6])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[7])
        self.var_salary.set(row[8])


    #____update____ 
    def update(self):
        con = sqlite3.connect(database="ims.db")
        cur = con.cursor()
        try:
            if self.var_empid.get() == "":
                messagebox.showerror("Lỗi", "Hãy nhập mã số nhân viên!", parent=self.root)
            else:
                cur.execute("Select * from employee where empid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Lỗi","Mã số không hợp lệ", parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,utype=?,address=?,salary=? where empid=?",(
                                        
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_utype.get(),
                            self.txt_address.get('1.0',END), 
                            self.var_salary.get(),
                            self.var_empid.get()
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
            if self.var_empid.get() == "":
                messagebox.showerror("Lỗi", "Hãy chọn nhân viên muốn xóa!", parent=self.root)
            else:
                cur.execute("Select * from employee where empid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Lỗi", "Đã có mã số này rồi", parent=self.root)
                else:
                    op=messagebox.askyesno("Xác nhận","Bạn muốn xóa thông tin?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where empid=?",(self.var_empid.get(),))
                        con.commit()
                        messagebox.showinfo("Xóa","Đã xóa thành công",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Lỗi", f"Lỗi đến từ : {str(ex)}")


    #_____Làm mới____
    def clear(self):
        self.var_empid.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_utype.set("Select")
        self.txt_address.delete('1.0',END) 
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()