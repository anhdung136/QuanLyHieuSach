import sqlite3

def create_db():
    # Kết nối đến cơ sở dữ liệu SQLite hoặc tạo cơ sở dữ liệu mới nếu chưa tồn tại
    con = sqlite3.connect(database=r'ims.db')

    # Tạo một đối tượng cursor để thực hiện các truy vấn SQL
    cur = con.cursor()

    # Tạo bảng employee nếu chưa tồn tại, với các trường dữ liệu như: empid, name, email, gender, contact, dob, utype, address, salary
    cur.execute("CREATE TABLE IF NOT EXISTS employee(empid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, utype text, address text, salary text)")

    # Lưu các thay đổi vào cơ sở dữ liệu
    con.commit()

create_db()
