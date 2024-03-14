from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("792x390+206+130")
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
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()

        #===== khung tìm kiếm ===========
        SearchFrame=LabelFrame(self.root,text="Tìm nhân viên",font=("time new roman",12,"bold"),bd=2,relief=RIDGE,bg="#F1E4C3")
        SearchFrame.place(x=150,y=20,width=500,height=70)

        
        #===== các chức năng =========
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchtxt, values=("Chọn theo","Tên", "Email", "Liên hệ"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_search.place(x=10, y=10, width=130)
        cmb_search.current(0)
        txt_search = Entry(SearchFrame, font=("time new roman", 15), bg="#F3EEEA").place(x=160, y=10)
        btn_search = Button(SearchFrame, text="Tìm", font=("Arial Rounded MT Bold", 17), bg="#C85108", fg="#F4EEC7").place(x=400, y=8, width=80, height=30)

    #====================title================
        title = Label(self.root, text="thông tin chi tiết của nhân viên", font=("time new roman", 15), bg="#61764B", fg="#FFF9C9").place(x=5, y=100, width=782)

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
        lbl_doj = Label(self.root, text="Ngày tham gia", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=190)
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_name.place(x=91, y=190, width=180)

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_dob.place(x=383, y=190, width=140)

        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_doj.place(x=672, y=190, width=112)

    #==================== hàng 3 ===============
        lbl_email = Label(self.root, text="Email", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=230)
        lbl_pass = Label(self.root, text="Mật khẩu", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=285, y=230)        
        lbl_utype = Label(self.root, text="phân quyền", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=230)
        
        txt_email = Entry(self.root, textvariable=self.var_email, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_email.place(x=63, y=230, width=208)

        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_pass.place(x=379, y=230, width=145)

        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Chọn theo","Quản Lý", "Nhân viên"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_utype.place(x=648, y=230, width=136)
        cmb_utype.current(0)

    #============hàng 4============
        lbl_address = Label(self.root, text="Địa chỉ", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=270)
        lbl_salary = Label(self.root, text="lương", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=535, y=270)        
        
        txt_address = Text(self.root, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_address.place(x=77, y=270, width=450)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_salary.place(x=602, y=270, width=181)

if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
