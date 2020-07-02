import sqlite3


# first function is to make the database connection
def connection():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE if NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,"
                "isbn INTEGER)")
    con.commit()
    con.close()


# this function is to create the rows in the database or i can say to insert the data into database
def insert(text, author, year, isbn):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (text, author, year, isbn))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    con.close()
    return row


# this function is to delete the rows from the table
def delete(id):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()


# this function is to search the row element
def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    row = cur.fetchall()
    con.close()
    return row


# this function is to update any row from the books
def update(id, title, author, year, isbn):
    con = sqlite3.connect("anushka.db")
    cur = con.cursor()
    cur.execute("UPDATE store SET title=?,author=?,year=?,isbn=?,WHERE id=?", (id, title, author, year, isbn))
    con.commit()
    con.close()


connection()
insert("the sea", "john", 1918, 9897969659)
insert("the road", "smith", 2004, 9878696587)
insert("the lake", "radha", 2003, 79887978)
print(view())
print(search(author="john"))
delete(3)
print(view())
