<<<<<<< HEAD
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
=======
print("giuco se indentifica drept o masa de calcat cu pronumele they/them")
'''
De asemenea tin sa ma mentionez ca sunt pansexual si doresc un partener non-binar identificabil prin pronumele Eu/Lui cu care sa impartasesc
dorintele carnale
'''
>>>>>>> d4861154c61eab82e443dcd2c63a0c48c59492e2
