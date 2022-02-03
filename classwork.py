dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
dimensions[0]=250
print(dimensions)
dimensions = (250, 75)
print(dimensions)
dimensions = (250, 75)
for i in dimensions:
    print(i)
dimensions = (200, 50)
t = type(dimensions)
print(t)
user = {"u1": "Человек", "u2": "Супергерой"}
print(user["u1"])
print(user["u2"])
user = {
    "u1": "Человек"
    "u2": "Супергерой"
}
new_user = user["u2"]
message = f"Ты прошел игру, теперь ты {new_user}"
print(message)
print(user)
user["u3"] = "Волк"
user["u4"] = "Лиса"
print(user)