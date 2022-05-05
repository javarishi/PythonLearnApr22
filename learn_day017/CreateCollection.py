import pymongo

mongoclient = pymongo.MongoClient("mongodb://localhost:27017/")
testdb = mongoclient["test_apr22_python"]
sample_collection = testdb["emp_collection"]

oneEmp = {
            "emp_number": "0121",
            "emp_name": "David Burrow",
            "address": "121 Cumberland Pwky"
        }

many_emp = [
    { "emp_number": "0111", "emp_name": "Byron Barns", "address": "0111 Cumberland Pwky" },
    { "emp_number": "0131", "emp_name": "Ryan Coble", "address": "0131 Cumberland Pwky" },
    { "emp_number": "0141", "emp_name": "Alex Sanders", "address": "0141 Cumberland Pwky" },
]

# result = sample_collection.insert_one(oneEmp)
result = sample_collection.insert_many(many_emp)
print("Done! ", result.inserted_ids)
mongoclient.close()