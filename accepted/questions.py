from pymongo import MongoClient
mongoDB = MongoClient('localhost', 27017)
database = mongoDB.openPL

questions = [
  {
    "stem": "okno",
    "choices": ["window", "cat", "food", "mountain"],
    "indexOfAnswer": 0
  },
  {
    "stem": "kot",
    "choices": ["dog", "cat", "fish", "bird"],
    "indexOfAnswer": 1
  },
  {
    "stem": "chleb",
    "choices": ["milk", "bread", "egg", "meat"],
    "indexOfAnswer": 1
  },
  {
    "stem": "pies",
    "choices": ["dog", "horse", "sheep", "cow"],
    "indexOfAnswer": 0
  },
  {
    "stem": "góra",
    "choices": ["river", "sea", "mountain", "forest"],
    "indexOfAnswer": 2
  },
  {
    "stem": "dom",
    "choices": ["car", "house", "road", "garden"],
    "indexOfAnswer": 1
  },
  {
    "stem": "jabłko",
    "choices": ["banana", "apple", "pear", "orange"],
    "indexOfAnswer": 1
  },
  {
    "stem": "książka",
    "choices": ["pen", "book", "paper", "pencil"],
    "indexOfAnswer": 1
  },
  {
    "stem": "szkoła",
    "choices": ["hospital", "school", "station", "shop"],
    "indexOfAnswer": 1
  }
]

for question in questions:
  database.questions.update_one(
    {"stem": question["stem"]},
    {"$setOnInsert": question},
    upsert=True
  )
