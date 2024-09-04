import mariadb
import sys
import json





def insert_into_db(user_db,password_db, name, address):
    try:
        conn=mariadb.connect(
                user=user_db,
                password=password_db,
                port=3306,
                database="python_db"
        )
    except mariadb.Error as e:
        print(f"Error connecting to maria-db: {e}")
        


    cur= conn.cursor()

    try:
        cur.execute("create table customer(id int auto_increment primary key, name varchar(255), address varchar(255)) ")
    except mariadb.Error as e:
        pass

    try:

        sql= "insert into customer (name, address) values(%s , %s)"
        val= (name,address)
        cur.execute(sql,val)
        conn.commit()
    except mariadb.Error as e:
        conn.rollback()
        return False
    return True



def get_data(user_db,password_db, id_num):
    try:
        conn=mariadb.connect(
                user=user_db,
                password=password_db,
                port=3306,
                database="python_db"
        )
    except mariadb.Error as e:
        print(f"Error connecting to maria-db: {e}")
        


    cur= conn.cursor()

    try:
        cur.execute("create table customer(id int auto_increment primary key, name varchar(255), address varchar(255)) ")
    except mariadb.Error as e:
        pass

    try:

        sql= "select name, address from customer where id ="+ id_num
        cur.execute(sql)
       
        records= cur.fetchall()
       

    except mariadb.Error as e:
        print(e)
        return False
    return {"name":{records[0]}}


def update_database(user_db,password_db,id_num,name,address):
    try:
        conn=mariadb.connect(
                user=user_db,
                password=password_db,
                port=3306,
                database="python_db"
        )
    except mariadb.Error as e:
        print(f"Error connecting to maria-db: {e}")
        


    cur= conn.cursor()

    try:
        cur.execute("create table customer(id int auto_increment primary key, name varchar(255), address varchar(255)) ")
    except mariadb.Error as e:
        pass

    try:
        sql= f"update customer set name='{name}',address='{address}' where id = {id_num}"
        
        cur.execute(sql)
        conn.commit()
        

       

    except mariadb.Error as e:
        print(e)
        return False
    return True


def delete_data(user_db,password_db, id_num):
    try:
        conn=mariadb.connect(
                user=user_db,
                password=password_db,
                port=3306,
                database="python_db"
        )
    except mariadb.Error as e:
        print(f"Error connecting to maria-db: {e}")
        


    cur= conn.cursor()

    try:
        cur.execute("create table customer(id int auto_increment primary key, name varchar(255), address varchar(255)) ")
    except mariadb.Error as e:
        pass

    try:

        sql= "delete from customer where id ="+ id_num
        cur.execute(sql)
        conn.commit()
   
       

    except mariadb.Error as e:
        print(e)
        return False
    return True


