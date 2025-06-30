print("💻 KRAFTON JUNGLE | CHAPTER 3")

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

def getAge(name):
  for person in people:
    if person["name"] == name:
      return person["age"]

targetName = "carry"
print(f"{targetName}'s age: {getAge(targetName)}")