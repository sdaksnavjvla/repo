import sqlite3 as lit

def main():

    try:
        db=lit.connect("data2.db")
        cur=db.cursor()
        query="CREATE TABLE users (id INT, nume TEXT, adresa TEXT)"
        cur.execute(query)
        print("s-a creat")
    except:
        print("nu s-a creat tabel")
    finally:
        db.close()

main()