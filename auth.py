from email import message
from tabnanny import check
import pymongo
from pymongo import MongoClient

DATABASE_HOST = "mongodb://127.0.0.1:27017"
DATABASE_NAME = "testBase"
DATABASE_COLLECTION = "users"

AUTH_FAIL = "Wrong user or password"
AUTH_SUCSSEED = "User exist and password correct!"

FIELD_ID = "id"
FIELD_PWD = "pwd"

def auth(message):
    client = pymongo.MongoClient(DATABASE_HOST)
    db = client[DATABASE_NAME]
    users = db[DATABASE_COLLECTION]

    data = message.text.split()
    if len(data)!=2:
        return AUTH_FAIL
    else:
        checkUser = users.find_one({FIELD_ID:data[0], FIELD_PWD:data[1]})
        if checkUser is None:
            print(AUTH_FAIL)
            return AUTH_FAIL
        else:
            print(AUTH_SUCSSEED)
            return AUTH_SUCSSEED

