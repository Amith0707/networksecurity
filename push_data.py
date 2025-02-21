import os
import sys
import json
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecuritySystem
from networksecurity.logging.logger import logging

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
## Helps to secure a connection to mongo db and is used to validate the connection 
ca=certifi.where()

class NetwrokDataExtract():
    def __init(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecuritySystem(e,sys)
    
    def cv_to_json_converter(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())

            return records
        except Exception as e:
            raise NetworkSecuritySystem(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecuritySystem(e,sys)

if __name__=="__main__":
    FILE_PATH="network_data\\phisingData.csv"
    DATABASE="NETWORKDB"
    Collection="NetworkData"
    networkobj=NetwrokDataExtract()
    records=networkobj.cv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)

##Collection is same as table data in MYSQL
    