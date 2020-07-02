# database creation,insertion and display the data base
# basically sqlite is the package for creating or for working on database
import sqlite3


# first function is to make the database connection
def connection():
    con = sqlite3.connect("anushka.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE if NOT EXISTS store (item TEXT,quantity INTEGER,price REAL)")
    con.commit()
    con.close()


# this function is to create the rows in the database or i can say to insert the data into database
def insert(item, quantity, price):
    con = sqlite3.connect("anushka.db")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    con.commit()
    con.close()


# this function is to display the data of your database basically
def view():
    con = sqlite3.connect("anushka.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    row = cur.fetchall()
    con.close()
    return row


# this function is to delete the rows from the table
def delete(item):
    con = sqlite3.connect("anushka.db")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    con.commit()
    con.close()


# this function is to update the database table
def update(quantity, price, item):
    con = sqlite3.connect("anushka.db")
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?", (quantity, price, item))
    con.commit()
    con.close()


connection()
insert("chocolate", 80, 2)
view()
insert("wine", 800, 1)
view()
insert("teddy", 500, 1)
view()
update(400, 2, "wine")
view()
delete("chocolate")
view()
print(view())
