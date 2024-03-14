from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
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
        SearchFrame=LabelFrame(self.root,text="Tìm nhân viên",font=("time new roman",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
        #===== các chức năng =========
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchtxt, values=("Tên", "Email", "Contact"), state='readonly', justify=CENTER, font=("time new roman", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame, font=("time new roman", 15), bg="#FEF7DC")
        txt_search.place(x=200, y=10)
        btn_search=Button(SearchFrame,text="Tìm", textvariable=self.var_searchtxt, font=("Arial Rounded MT Bold", 17), bg="#C85108",fg="#F4EEC7")
        btn_search.place(x=470, y=8,width=80,height=30)

        #========title======
        title = Label(self.root, text="thông tin chi tiết của nhân viên", font=("time new roman", 15), bg="#61764B", fg="#FFF9C9")
        title.place(x=50, y=100, width=1000)

        #======content=========
        lbl_empid = Label(self.root, text="Mã số nhân viên", font=("time new roman", 15), bg="#61764B", fg="#FFF9C9")
        lbl_empid.place(x=50, y=150)


if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()
