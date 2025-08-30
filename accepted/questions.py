from pymongo import MongoClient
app = Flask(__name__)
mongoDB = MongoClient('localhost', 27017)
database = mongoDB.openPL

