from fastapi import FastAPI
from typing import Union
import random as rand
from pydantic import BaseModel
from mariadb_conn import *
import json

f = open('db_creds.json')
creds= json.load(f)
user=creds['user']
password=creds['password']

app= FastAPI()

class Item(BaseModel):
    name: str
    address: str
class Item_update(BaseModel):
    id: int
    name: str
    address: str


@app.get("/")
def root_route():
    random_root_num=rand.randint(0,1000)
    return {f"[*] Welcome to CRUD api root, enjoy a random number {random_root_num} [*] Powered my dear FASTAPI"}


@app.post("/post/")
async def post_data(data: Item):
    name= data.name
    address= data.address
    flag= insert_into_db(user,password,name,address)
    if flag==True:
        return {
            "msg": "yeaboi",
        }
    else:
        return{
            "msg":"badboi",
        }
    
@app.get("/get_data/{id_num}")
async def fetch_data(id_num):   
    return get_data(user,password,id_num)


@app.post("/update/")
async def update_data(data:Item_update):
    name= data.name
    address= data.address
    id_ref= data.id
    flag= update_database(user, password,id_ref,name , address)
    if flag==True:
        return {
            "msg": "yeaboi updated",
        }
    else:
        return{
            "msg":"badboi",
        }

@app.get("/delete_data/{id_num}")
async def delete_data_from_db(id_num):   
    flag= delete_data(user,password,id_num)
    if flag==True:
        return {
            "msg": "yeaboi updated",
        }
    else:
        return{
            "msg":"badboi",
        }


