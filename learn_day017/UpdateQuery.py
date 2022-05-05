import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = mongoclient["test_apr22_python"]
sample_collection = testdb["emp_collection"]

update_selector = {'emp_number': '0131'}
newvalues = { "$set": { "address" :"0131 Spring Hill Pwky"} }

results = sample_collection.update_one(update_selector, newvalues)

print(results.upserted_id)



mongoclient.close()