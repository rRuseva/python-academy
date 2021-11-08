import json

person = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
if __name__ == '__main__':
  with open("person.json","wt", encoding="utf-8") as f:
    json.dump(person, f,indent=4)

  with open("person.json", "rt",encoding="utf-8") as f:
    result = json.load(f)
  print(result)
  print(type(result))
