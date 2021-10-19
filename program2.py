import sqlite3

# using sqlitte 3 database
# version 3.36.0
# download source: https://github.com/sqlite/sqlite/releases/tag/version-3.36.0
# download: https://www.sqlite.org/download.html
# no port (running locally as a process)

def insert_customer(id, name, tot_goods):
    if(type(id)!=int or type(name)!= str or type(tot_goods)!=int):
        raise TypeError("Arguments should be of type (int,str,int)")

    if(tot_goods<0):
        raise ValueError("Must not have negative total goods")

    connection = sqlite3.connect("problem2.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO customer VALUES ({id}, '{name}', {tot_goods})")
    connection.commit()

def insert_order(id, goods):
    if(type(id)!=int or type(goods)!=int):
        raise TypeError("Arguments should be of type (int,int)")

    if(goods<0):
        raise ValueError("Must not have negative goods")

    connection = sqlite3.connect("problem2.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO order VALUES ({id}, {goods})")
    connection.commit()

def retrieve_customers():
    connection = sqlite3.connect("problem2.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM customer")
    connection.commit()
    return cursor.fetchall()
