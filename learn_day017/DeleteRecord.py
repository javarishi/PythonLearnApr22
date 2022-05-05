import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = mongoclient["test_apr22_python"]
sample_collection = testdb["emp_collection"]

delete_query = {'emp_number': '0141'}
result = sample_collection.delete_one(delete_query)

print(result.deleted_count)


mongoclient.close()