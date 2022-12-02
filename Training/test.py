import json

# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))

# print(type(json.dumps(42)))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
"""

"""

# x = int(42)
# y1 = json.dumps("hello")
# y2 = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(f'The type of {y2} is {type(y2)} ')

s = {'type':['allen',('192.168.115.131') ] ,
    'type2':['ele',('172.10.100.15')]
}
print(f"The before s is { type(s['type'][1]) }")
s.pop('type')
print(f'The after s is {s}')
