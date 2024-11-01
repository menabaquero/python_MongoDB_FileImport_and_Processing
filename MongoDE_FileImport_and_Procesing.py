
import pandas as pd
import pymongo
from pymongo import MongoClient
import json

#https://www.mongodb.com/community/forums/t/import-csv-file-data-into-mongodb-using-python/15759/2i
#https://gist.github.com/jxub/f722e0856ed461bf711684b0960c8458
def mongoimport(csv_path, db_name, coll_name, db_url='localhost', db_port=27000):
    """ Imports a csv file at path csv_name to a mongo colection
        returns: count of the documants in the new collection
        """
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    return coll.count()

#https://www.w3schools.com/python/python_functions.asp
def createDataBase():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]

print("Creating Database...STARTING")
createDataBase()
print("Creating Database...DONE")
