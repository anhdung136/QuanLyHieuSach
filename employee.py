from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("792x435+206+130")
        self.root.title("- - - HỆ THỐNG QUẢN LÝ HIỆU SÁCH - - - NHÓM 9 - - - K15DCPM06 - - -")
        self.root.config(bg="#FFFFEC")
        self.root.focus_force()
    #===========================================================
        #----Tất cả biến--------
        self.var_searchType = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
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
        SearchFrame=LabelFrame(self.root,text="Tìm nhân viên",font=("time new roman",12,"bold"),bd=2,relief=RIDGE,bg="#F1E4C3")
        SearchFrame.place(x=10,y=20,width=500,height=70)

        
        #===== các chức năng =========
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchtxt, values=("Chọn theo","Tên", "Email", "Liên hệ"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_search.place(x=10, y=10, width=130)
        cmb_search.current(0)
        txt_search = Entry(SearchFrame, font=("time new roman", 15), bg="#F3EEEA").place(x=160, y=10)
        btn_search = Button(SearchFrame, text="Tìm", font=("Arial Rounded MT Bold", 17), bg="#C85108", fg="#F4EEC7").place(x=400, y=8, width=80, height=30)

    #====================title================
        title = Label(self.root, text="thông tin chi tiết của nhân viên", font=("time new roman", 15), bg="#52D3D8", fg="#000000").place(x=5, y=100, width=535)
        title = Label(self.root,bg="#52D3D8", fg="#FFF9C9").place(x=520, y=4, width=25,height=125)

    #===================content====================
    #================== hàng 1 ==========
        lbl_empid = Label(self.root, text="Mã số", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=150)
        lbl_gender = Label(self.root, text="Giới tính", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=285, y=150)
        lbl_contact = Label(self.root, text="Liên hệ", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=150)
        txt_empid = Entry(self.root, textvariable= self.var_emp_id, font=("time new roman", 15), bg="#F3EEEA", fg="#000000").place(x=70, y=150, width=200)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Chọn theo","Nam", "Nữ"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_gender.place(x=373, y=150, width=149)
        cmb_gender.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_contact.place(x=612, y=150, width=171)
    #==================== hàng 2 ===========
        lbl_name = Label(self.root, text="Họ & tên", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=190)
        lbl_dob = Label(self.root, text="Ngày sinh", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=285, y=190)        
        lbl_utype = Label(self.root, text="phân quyền", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_name.place(x=91, y=190, width=180)

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_dob.place(x=383, y=190, width=140)

        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Chọn theo","Quản Lý", "Nhân viên"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_utype.place(x=648, y=190, width=135)
        cmb_utype.current(0)

    #==================== hàng 3 ===============
        lbl_email = Label(self.root, text="Email", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=230)
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
        
        txt_address = Text(self.root, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_address.place(x=77, y=270, width=705, height=50)
    #======= nút chức năng thêm xóa sửa ==========
        btn_add = Button(self.root, text="Lưu", font=("time new roman", 17), bg="#1A5D1A", fg="#FAF0D7").place(x=570, y=25, width=80, height=30)
        btn_upadte = Button(self.root, text="Sửa", font=("time new roman", 17), bg="#0C359E", fg="#FAF0D7").place(x=685, y=25, width=80, height=30)
        btn_delete = Button(self.root, text="xóa", font=("time new roman", 17), bg="#B70404", fg="#FAF0D7").place(x=570, y=70, width=80, height=30)
        btn_clear = Button(self.root, text="làm mới", font=("time new roman", 15), bg="#FFA447", fg="#FAF0D7").place(x=685, y=70, width=80, height=30)
    #======= thông tin nhân viên ===========
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=325,relwidth=1,height=109)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrolly=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("Mã số","Họ & tên","Email","Giới tính","Ngày sinh","Mật khẩu","Phân quyền","Địa chỉ","Lương"))
        self.EmployeeTable.heading("#0", text=u"Mã số")
        self.EmployeeTable.heading("#1", text=u"Họ & tên")
        self.EmployeeTable.heading("#2", text=u"Email")
        self.EmployeeTable.heading("#3", text=u"Giới tính")
        self.EmployeeTable.heading("#4", text=u"Liên hệ")
        self.EmployeeTable.heading("#5", text=u"Ngày sinh")
        self.EmployeeTable.heading("#6", text=u"Mật khẩu")
        self.EmployeeTable.heading("#7", text=u"Quyền")
        self.EmployeeTable.heading("#8", text=u"Địa chỉ")
        self.EmployeeTable.heading("#9", text=u"Lương")

        self.EmployeeTable.pack(fill=BOTH,expand=1)

        self.EmployeeTable.column("#0", width=5)
        self.EmployeeTable.column("#1", width=100)
        self.EmployeeTable.column("#2", width=50)
        self.EmployeeTable.column("#3", width=17)
        self.EmployeeTable.column("#4", width=30)
        self.EmployeeTable.column("#5", width=40)
        self.EmployeeTable.column("#6", width=40)
        self.EmployeeTable.column("#7", width=10)
        self.EmployeeTable.column("#8", width=100)
        self.EmployeeTable.column("#9", width=20)
        
if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
