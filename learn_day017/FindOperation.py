import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = mongoclient["test_apr22_python"]
sample_collection = testdb["emp_collection"]
'''
one = sample_collection.find_one()
print(one)
'''
# Select emp_name, emp_number from emp_collection where emp_number = 0121
results = sample_collection.find({'emp_number': {"$gt" : '0121'}}, {'_id': 0, 'emp_number' : 1, 'emp_name': 1})
for each_document in results:
    print(each_document)


mongoclient.close()