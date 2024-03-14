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

        #===== khung tìm kiếm ===========
        SearchFrame=LabelFrame(self.root,text="Tìm nhân viên",font=("time new roman",12,"bold"),bd=2,relief=RIDGE,bg="#F1E4C3")
        SearchFrame.place(x=150,y=20,width=500,height=70)
        
        #===== các chức năng =========
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchtxt, values=("Chọn theo","Tên", "Email", "Contact"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_search.place(x=10, y=10, width=130)
        cmb_search.current(0)
        txt_search = Entry(SearchFrame, font=("time new roman", 15), bg="#F3EEEA").place(x=160, y=10)
        btn_search = Button(SearchFrame, text="Tìm", font=("Arial Rounded MT Bold", 17), bg="#C85108", fg="#F4EEC7").place(x=400, y=8, width=80, height=30)

    #==============title======
        title = Label(self.root, text="thông tin chi tiết của nhân viên", font=("time new roman", 15), bg="#61764B", fg="#FFF9C9").place(x=5, y=100, width=782)

    #============content=========
    #============= hàng 1 ==========
        lbl_empid = Label(self.root, text="Mã số", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=150)
        lbl_gender = Label(self.root, text="Giới tính", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=295, y=150)
        lbl_contact = Label(self.root, text="Liên hệ", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=705, y=150)
        txt_empid = Entry(self.root, textvariable= self.var_emp_id, font=("time new roman", 15), bg="#F3EEEA", fg="#000000").place(x=70, y=150, width=209)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Chọn theo","Nam", "Nữ"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_gender.place(x=440, y=150, width=190)
        cmb_gender.current(0)

        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_contact.place(x=830, y=150, width=180)
    #======== hàng 2 ===========
        lbl_name = Label(self.root, text="Họ và tên", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=190)
        lbl_dob = Label(self.root, text="Ngày sinh", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=350, y=190)        
        lbl_doj = Label(self.root, text="Ngày tham gia", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=750, y=190)
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_name.place(x=98, y=190, width=180)

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_dob.place(x=450, y=190, width=180)

        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_doj.place(x=890, y=190, width=120)

#======== hàng 3 ===========
        lbl_email = Label(self.root, text="Email", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=5, y=230)
        lbl_pass = Label(self.root, text="Mật khẩu", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=350, y=230)        
        lbl_utype = Label(self.root, text="phân quyền", font=("time new roman", 15), bg="#F1E4C3", fg="#000000").place(x=750, y=230)
        
        txt_email = Entry(self.root, textvariable=self.var_email, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_email.place(x=63, y=230, width=216)

        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_pass.place(x=450, y=230, width=180)

        txt_utype = Entry(self.root, textvariable=self.var_utype, font=("time new roman", 15), bg="#F3EEEA", fg="#000000")
        txt_utype.place(x=870, y=230, width=141)

if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
