import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = mongoclient["testdatabase"]

print("********** Database Names ***********")

db_names = mongoclient.list_database_names()
for each_name in db_names:
    print(each_name)

print("********** Collection Names in testdatabase ***********")

collection_names = testdb.list_collection_names()
for each_collection in collection_names:
    print(each_collection)

mongoclient.close()