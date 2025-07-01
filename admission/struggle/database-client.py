from pymongo import MongoClient
client = MongoClient('localhost', 27017)
jungleDB = client.jungle


"""
jungleDB.users.insert_one({'name':'bobby','age':21})
jungleDB.users.insert_one({'name':'kay','age':27})
jungleDB.users.insert_one({'name':'john','age':30})

jungleDB.users.insert_one({'name': 'alice', 'age': 24})
jungleDB.users.insert_one({'name': 'david', 'age': 29})
jungleDB.users.insert_one({'name': 'susan', 'age': 22})
jungleDB.users.insert_one({'name': 'mike', 'age': 26})
jungleDB.users.insert_one({'name': 'linda', 'age': 31})

jungleDB.users.insert_one({'name': 'tom', 'age': 28})
jungleDB.users.insert_one({'name': 'emma', 'age': 23})
jungleDB.users.insert_one({'name': 'jake', 'age': 32})
jungleDB.users.insert_one({'name': 'nina', 'age': 25})
jungleDB.users.insert_one({'name': 'oliver', 'age': 27})
"""

"""
jungleDB.users.update_one({'name':'bobby'},{'$set':{'age':19}})
jungleDB.users.delete_one({"name": "bobby"})
"""

users = list(jungleDB.users.find({}, {"_id": False}))
for user in users:
  # print(user["name"])
  if user["age"] <= 25:
    print(user)

