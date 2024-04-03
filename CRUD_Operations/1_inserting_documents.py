import pymongo as pm
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
#Connect to database
connection_string = f'mongodb+srv://{os.getenv("user")}:{os.getenv("passwd")}@myatlasclusteredu.d1lzas5.mongodb.net/?retryWrites=true&w=majority'
client = pm.MongoClient(connection_string)
for dbname in client.list_database_names():
    print(dbname)

#insert_one

new_account = {
    "account_holder": "mongo",
    "account_id": "MGDB123",
    "balance": 5000000,
    "last_updated": datetime.datetime.now(datetime.UTC),
}
db = client["bank"]
collection = db["accounts"]
result = collection.insert_one(new_account)
document_id = result.inserted_id
print(document_id)

client.close()



