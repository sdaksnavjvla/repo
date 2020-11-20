import sqlite3 as lit
from erori import error_adaugare,error_creeaza

class Clasa_baza:
    def __init__(self,nume):
        pass
    
    def createDb(self,nume):
        try:
            db=lit.connect(nume)
        except:
            raise error_creeaza
        finally:
            db.close()
    
    def createTable(self,nume):
        try:
            db=lit.connect(nume)
            cur=db.cursor()
            query="CREATE TABLE entries (id INT,x  INT,y  INT,data TEXT)"
            cur.execute(query)
        except:
            raise error_adaugare
    
    def add(self):
        pass