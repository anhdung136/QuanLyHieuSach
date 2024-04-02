import sqlite3

def create_db():
    # Kết nối đến cơ sở dữ liệu SQLite hoặc tạo cơ sở dữ liệu mới nếu chưa tồn tại
    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor() # Tạo một đối tượng cursor để thực hiện các truy vấn SQL
    
    #________EMPLOYEE_______
    # Tạo bảng employee nếu chưa tồn tại, với các trường dữ liệu như: empid, name, email, gender, contact, dob, utype, address, salary
    cur.execute("CREATE TABLE IF NOT EXISTS employee(empid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, utype text, address text, salary text)")
    con.commit() # Lưu các thay đổi vào cơ sở dữ liệu

    #________CATEGORY_______
    # Tạo bảng category nếu chưa tồn tại, với các trường dữ liệu như: empid, name, email, gender, contact, dob, utype, address, salary
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    con.commit() # Lưu các thay đổi vào cơ sở dữ liệu

    #________CATEGORY_______
    # Tạo bảng category nếu chưa tồn tại, với các trường dữ liệu như: empid, name, email, gender, contact, dob, utype, address, salary
    cur.execute("CREATE TABLE IF NOT EXISTS product(cid INTEGER PRIMARY KEY AUTOINCREMENT, category text, name text, author text, price text, describe text, status text)")
    con.commit() # Lưu các thay đổi vào cơ sở dữ liệu

create_db()
