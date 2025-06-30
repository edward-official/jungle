fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def countFruit(fruitName):
  count = 0
  for fruit in fruits:
    if fruit==fruitName:
      count += 1
  print(count)

countFruit("사과")