from pymongo import MongoClient
client = MongoClient('localhost', 27017)
database = client.jungle

allUsers = list(database.users.find())
for user in allUsers:
  print(user)