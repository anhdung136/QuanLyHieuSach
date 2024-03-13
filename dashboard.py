from tkinter import *
from PIL import Image, ImageTk #pip install pillow

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("- - - HỆ THỐNG QUẢN LÝ HIỆU SÁCH - - - NHÓM 9 - - - K15DCPM06 - - -")
        self.create_title_label()
        self.create_clock_label()  # Gọi hàm tạo label clock
        self.create_left_menu()     # Gọi hàm tạo left menu
        self.root.config(bg="#FFFFEC")
    
    #====title====
    def create_title_label(self):
        self.icon_title = PhotoImage(file="images/book.png")
        title = Label(self.root, text="HỆ THỐNG QUẢN LÝ HIỆU SÁCH", image=self.icon_title, compound=LEFT , font=("Arial Rounded MT Bold", 30, "bold"), bg="#B19470", fg="#F8FAE5", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        #====btn_logout====
        btn_logout = Button(self.root, text="Thoát", font=("time new roman", 15, "bold"), bg="#BECA5C")
        btn_logout.place(x=1230, y=10, width=100)

    #====clock====
    def create_clock_label(self):
        self.lbl_clock = Label(self.root, text="Chào mừng đã đến với hệ thống\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("Arial Rounded MT Bold", 15), bg="#E1C78F", fg="#F8FAE5")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)  

    #====Left menu====
    def create_left_menu(self):
        self.MenuLogo = Image.open("images/menu.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        self.leftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="#F3EEEA")
        self.leftMenu.place(x=0, y=102, width=200, height=533)
        
        lbl_menuLogo = Label(self.leftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(self.leftMenu, text="Menu", font=("time new roman", 25, "bold"), bg="#76453B",fg="#F8FAE5")
        lbl_menu.pack(side=TOP, fill=X)
        
        self.icon_side=PhotoImage(file="images/side.png")
        btn_employee = Button(self.leftMenu, text="Nhân viên",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)

        btn_supplier = Button(self.leftMenu, text="Vật tư",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)

        btn_category = Button(self.leftMenu, text="danh mục",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_category.pack(side=TOP, fill=X)
        
        btn_product = Button(self.leftMenu, text="Sách",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_product.pack(side=TOP, fill=X)
        
        btn_sales = Button(self.leftMenu, text="Lợi tức",image=self.icon_side,compound=LEFT,padx=10,anchor="w", font=("time new roman", 20, "bold"), bg="#CC9B6D", bd=3, cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)

root = Tk()
obj = IMS(root)
root.mainloop()
