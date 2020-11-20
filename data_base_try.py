import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def formare_tabel():
    try:
        db = sqlite3.connect("D:/Unihack/repo/employee.db")
        cur = db.cursor()

        tablequesry = "CREATE TABLE users (id INT, name TEXT, email TEXT)"

        cur.execute(tablequesry)
        print(";;;")

    except:
        print("nu")

def printare_tabel(db_file):
    db = sqlite3.connect(db_file)
    with db:
        cur = db.cursor()
        selecquery = "SELECT * FROM users"
        cur.execute(selecquery)

        rows = cur.fetchall()

        for data in rows:
            print(data)

def add_persones(db_file, menuti):
    db = sqlite3.connect(db_file)
    with db:
        cur = db.cursor()
        cur.executemany("INSERT INTO users VALUES (?, ?, ?)", menuti)
        print("Am adaugat menuti.")
    
def update_pers(db_file):
    db = sqlite3.connect(db_file)
    with db:
        new_name = "Birjovanu"
        user_id = 29

        cur = db.cursor()
        cur.execute("UPDATE users SET email = ? WHERE id = ? ", (new_name, user_id))
        db.commit()
        print("Data updated successfully!")

def delete_persones(db_file):
    db = sqlite3.connect(db_file)
    with db:
        user_id = 19
        cur = db.cursor()
        cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
        db.commit()
        print("Data deleted successfully!")


if __name__ == '__main__':
    create_connection("D:/Unihack/repo/employee.db")
    formare_tabel()
    menuti =( 
    ("19", "Gabi", "Mircea"),
    ("29", "Matei", "Birjovanu")
    )
    #add_persones("D:/Unihack/repo/employee.db", menuti)
    printare_tabel("D:/Unihack/repo/employee.db")
    update_pers("D:/Unihack/repo/employee.db")
    print('______________________________________________________')
    printare_tabel("D:/Unihack/repo/employee.db")
    delete_persones("D:/Unihack/repo/employee.db")
    print('______________________________________________________')
    printare_tabel("D:/Unihack/repo/employee.db")