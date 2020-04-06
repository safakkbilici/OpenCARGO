#%%
import sqlite3

con = sqlite3.connect("deneme.db")

cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (İsim TEXT, Sayfa INT, yazar TEXT)")
    con.commit()
    
    
createTable()

def addData():
    cursor.execute("INSERT INTO kitaplik Values('Ali',500,'assjha')")
    con.commit()

addData()

# isim = input("İsim: ")
# sayfa = int(input("Sayfa: "))

def addData2(isim, sayfa):
    cursor.execute("INSERT INTO kitaplik Values(?,?)",(isim,sayfa))
    con.commit()

# addData2(isim,sayfa)

def verileriAl():
    cursor.execute("SELECT * FROM kitaplik")
    liste = cursor.fetchall()
    return liste

def verileriAl2():
    cursor.execute("SELECT İsim FROM kitaplik")
    liste = cursor.fetchall()
    return liste

def verileriAl3():
    cursor.execute("SELECT * FROM kitaplik where İsim = 'Ali'")
    liste = cursor.fetchall()
    return liste

def verileriGuncelle():
    cursor.execute("UPDATE kitaplik set İsim = 'Enes' where İsim = 'Ali'")
    con.commit()
    

def verileriSil():
    cursor.execute("DELETE from kitaplik where İsim = 'Enes'")
    con.commit()

print(verileriAl())
print(verileriAl2())
print(verileriAl3())
verileriGuncelle()
# verileriSil()

con.close()
