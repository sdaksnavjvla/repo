import sqlite3 as lit

def main():


    """
    try:
        db=lit.connect("data2.db")
        print("s-a creat")
    except:
        print("nu s-a creat DATABASE")
    finally:
        db.close()
    """
    
 
    """
    try:
        db=lit.connect("data2.db")
        #cur=db.cursor()
        query="CREATE TABLE users (id INT, nume TEXT, adresa TEXT)"
        cur.execute(query)
        print("s-a creat")
    except:
        print("nu s-a creat tabel")
    """
    """
    baietasi=((1,"geany","a"),(2,"Fany","a"),(3,"kany","a"))
    db=lit.connect("data2.db")
    with db:
            cur= db.cursor()
            cur.executemany('INSERT INTO users VALUES (?,?,?)',baietasi)
            print("s-au adaugat")
    """
    
    
    db=lit.connect("data2.db")
    with db:
        cur=db.cursor()
        sectquery="SELECT id FROM users"
        cur.execute(sectquery)

        rows=cur.fetchall()

        for i in rows:
            print(i)
    

    """
    db=lit.connect("data2.db")
    with db:
        idc=1
        num="v@ncea"
        cur = db.cursor()
        cur.execute("UPDATE users SET nume =? WHERE id=?",(num,idc))
        db.commit()
        print("merge, ba!")
    """
    
    """
    db=lit.connect("data2.db")
    with db:
        idc=1
        cur=db.cursor()
        cur.execute("DELETE FROM users WHERE id=?",(idc,)) #trb virgula in tuplu neaparat
        db.commit()
        print("merge,ba") 
    """   