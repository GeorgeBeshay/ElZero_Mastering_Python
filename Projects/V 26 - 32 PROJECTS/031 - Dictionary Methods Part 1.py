# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = { 
        "name" : "Osama"
        }

print(user)
user.clear()
print(user)

print("=" * 50) # Seperator

# update()
member = {
        "name" : "Osama"
        }
print(member)
member["age"] = 36
print(member)
member.update({"country":"Egypt"})
print(member)

print("=" * 50)

# copy()

main = {
    "name":"Osama"
}

b = main.copy()
print(b)
main.update({"skills":"Fighting"}) # b will not be affected because it is a shallow copy ...
print(main)
print(b)

print("=" * 50)

# keys() + values()
print(main.keys())
print(main.values())

print("=" * 50)



