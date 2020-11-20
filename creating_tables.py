import sqlite3

def main():
    try:
        db = sqlite3.connect("D:/Unihack/repo/employee.db")
        cur = db.cursor()

        tablequesry = "CREATE TABLE users (id INT, name TEXT, email TEXT)"

        cur.execute(tablequesry)
        print(";;;")

    except:
        print("nu")


main()