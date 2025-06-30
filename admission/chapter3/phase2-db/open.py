from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.jungle                        # 'jungle'라는 이름의 db를 만듭니다.

users = list(db.users.find({}))
for user in users:      # 반복문을 돌며 모든 결과값을 보기
  print(user)
  
bobby = db.users.find_one({'name':'bobby'})
print(bobby)

bobbyWithoutID = db.users.find_one({'name':'bobby'},{'_id':False})
print(bobbyWithoutID)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

user = db.users.find_one({'name':'bobby'})
print(user)

db.users.delete_one({'name':'bobby'})

user = db.users.find_one({'name':'bobby'})
print(user)


"""
# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})
"""