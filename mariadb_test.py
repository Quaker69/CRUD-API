import mariadb
import sys
import json



def insert_into_db(name, address):
    try:
        conn=mariadb.connect(
                user="user1",
                password="impact2001",
                port=3306,
                database="python_db"
        )
    except mariadb.Error as e:
        print(f"Error connecting to maria-db: {e}")
        sys.exit(1)


    cur= conn.cursor()

    try:
        cur.execute("create table customer(id int auto_increment primary key, name varchar(255), address varchar(255)) ")
    except mariadb.Error as e:
        print(e)

    try:

        sql= "insert into customer (name, address) values(%s , %s)"
        val= (name,address)
        cur.execute(sql,val)
        conn.commit()
    except mariadb.Error as e:
        conn.rollback()
        return False
    return True




