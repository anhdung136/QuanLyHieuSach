from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("792x435+206+130")
        self.root.title("- 📔 - HỆ THỐNG QUẢN LÝ HIỆU SÁCH - 📚 - NHÓM 9 - 📖 - K15DCPM06 - 📝 -")
        self.root.config(bg="#FFFFEC")
        self.root.focus_force()
        #===========================================================
        #----Tất cả biến--------
        self.var_searchType = StringVar()
        self.var_searchtxt = StringVar()

        self.var_empid = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()

        #===== khung tìm kiếm ===========
        SearchFrame = LabelFrame(self.root, text="Tìm nhân viên", font=("time new roman", 12, "bold"), bd=2, relief=RIDGE, bg="#F1E4C3")
        SearchFrame.place(x=10, y=20, width=500, height=70)

        #===== các chức năng =========
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchtxt,values=("Chọn theo", "Tên", "Email", "Liên hệ"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_search.place(x=10, y=10, width=130)
        cmb_search.current(0)
        txt_search = Entry(SearchFrame, font=("time new roman", 15), bg="#F3EEEA").place(x=160, y=10)
        btn_search = Button(SearchFrame, text="Tìm 🔍", font=("Arial Rounded MT Bold", 17), bg="#C85108",fg="#F4EEC7").place(x=400, y=8, width=80, height=30)

        #====================title================
        title = Label(self.root, text="thông tin chi tiết của nhân viên", font=("time new roman", 15), bg="#52D3D8", fg="#000000").place(x=5, y=100, width=535)
        title = Label(self.root, bg="#52D3D8", fg="#FFF9C9").place(x=520, y=4, width=25, height=125)

        #===================content====================
        #================== hàng 1 ==========
        lbl_empid = Label(self.root, text="Mã số", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=150)
        lbl_gender = Label(self.root, text="Giới tính", font=("time new roman", 15), bg="#F1E4C3",fg="#000000").place(x=285, y=150)
        lbl_contact = Label(self.root, text="Liên hệ", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=150)
        txt_empid = Entry(self.root, textvariable=self.var_empid, font=("time new roman", 15), bg="#F3EEEA", fg="#000000").place(x=70, y=150, width=200)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Chọn theo", "Nam", "Nữ"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_gender.place(x=373, y=150, width=149)
        cmb_gender.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("time new roman", 15), bg="#F3EEEA",fg="#000000")
        txt_contact.place(x=612, y=150, width=171)
        #==================== hàng 2 ===========
        lbl_name = Label(self.root, text="Họ & tên", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place( x=5, y=190)
        lbl_dob = Label(self.root, text="Ngày sinh", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=285, y=190)
        lbl_utype = Label(self.root, text="phân quyền", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_name.place(x=91, y=190, width=180)

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("time new roman", 15), bg="#F3EEEA",fg="#000000")
        txt_dob.place(x=383, y=190, width=140)

        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Chọn theo", "Quản Lý", "Nhân viên"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_utype.place(x=648, y=190, width=135)
        cmb_utype.current(0)

        #==================== hàng 3 ===============
        lbl_email = Label(self.root, text="Email", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place( x=5, y=230)
        lbl_pass = Label(self.root, text="Mật khẩu", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=285, y=230)
        lbl_salary = Label(self.root, text="lương", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_email.place(x=63, y=230, width=208)

        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_pass.place(x=379, y=230, width=145)

        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_salary.place(x=602, y=230, width=181)

        #============hàng 4=======================
        lbl_address = Label(self.root, text="Địa chỉ", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=270)

        self.txt_address = Text(self.root, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        self.txt_address.place(x=77, y=270, width=705, height=50)
        #======= nút chức năng thêm xóa sửa ==========
        btn_add = Button(self.root, text="Lưu", command=self.add, font=("time new roman", 17), bg="#1A5D1A", fg="#FAF0D7").place(x=570, y=25, width=80, height=30)
        btn_upadte = Button(self.root, text="Sửa", font=("time new roman", 17), bg="#0C359E", fg="#FAF0D7").place(x=685, y=25, width=80, height=30)
        btn_delete = Button(self.root, text="xóa", font=("time new roman", 17), bg="#B70404", fg="#FAF0D7").place(x=570, y=70, width=80, height=30)
        btn_clear = Button(self.root, text="làm mới", font=("time new roman", 15), bg="#FFA447",fg="#FAF0D7").place(x=685, y=70, width=80, height=30)
        #======= thông tin nhân viên ===========
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=325, relwidth=1, height=109)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame,columns=("empid", "name", "email", "gender", "contact", "dob", "pass","utype", "address", "salary"), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("empid", text=u"Mã số")
        self.EmployeeTable.heading("name", text=u"Họ tên")
        self.EmployeeTable.heading("email", text=u"Email")
        self.EmployeeTable.heading("gender", text=u"Giới tính")
        self.EmployeeTable.heading("contact", text=u"Liên hệ")
        self.EmployeeTable.heading("dob", text=u"Ngày sinh")
        self.EmployeeTable.heading("pass", text=u"Mật khẩu")
        self.EmployeeTable.heading("utype", text=u"Quyền")
        self.EmployeeTable.heading("address", text=u"Địa chỉ")
        self.EmployeeTable.heading("salary", text=u"Lương")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("empid", width=5)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=50)
        self.EmployeeTable.column("gender", width=17)
        self.EmployeeTable.column("contact", width=30)
        self.EmployeeTable.column("dob", width=40)
        self.EmployeeTable.column("pass", width=40)
        self.EmployeeTable.column("utype", width=10)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=20)

        self.EmployeeTable.pack(fill=BOTH, expand=1)

#=================================================================================================================
    
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_empid.get() == "":
                messagebox.showerror("Error", "Hãy nhập mã số nhân viên!", parent=self.root)
            else:
                cur.execute("Select * from employee where empid=?", (self.var_empid.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Đã có mã số này rồi", parent=self.root)
                else:
                    cur.execute("Insert into employee(empid,name,email,gender,contact,dob,pass,utype,address,salary) values (?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_empid.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_gender.get(),
                                        self.var_contact.get(),
                                        self.var_dob.get(),
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),  # Sửa từ txt_address thành self.txt_address
                                        self.var_salary.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Thành công", "Đã thêm nhân viên", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
