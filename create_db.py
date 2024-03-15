import sqlite3

def create_db():
    con = sqlite3.connect(r'images/ims.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(Ma_so INTEGER PRIMARY KEY AUTOINCREMENT,Ho_ten text,Email text,Gioi_tinh text,Ngay_sinh text,Mat_khau text,Phan_quyen text,Dia_chi text,Luong text)")
    con.commit()

    

create_db()
