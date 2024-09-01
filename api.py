from fastapi import FastAPI
from typing import Union
import random as rand
from pydantic import BaseModel
from mariadb_test import *


app= FastAPI()

class Item(BaseModel):
    name: str
    address: str

@app.get("/")
def root_route():
    random_root_num=rand.randint(0,1000)
    return {f"[*] Welcome to CRUD api root, enjoy a random number {random_root_num} [*] Powered my dear FASTAPI"}


@app.post("/post/")
async def get_post_data(data: Item):
    name= data.name
    address= data.address
    flag= insert_into_db(name,address)
    if flag==True:
        return {
            "msg": "yeaboi",
        }
    else:
        return{
            "msg":"badboi",
        }



