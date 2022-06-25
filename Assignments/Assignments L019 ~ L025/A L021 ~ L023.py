# L021 ~ L023
# A1
friends = ["Osama","Ahmed","Sayed","Ali","Mahmoud"]

print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])

# A2
print(friends[0] + " , " + friends[2] + " , " + friends[4] + "\n" + friends[1] + " , " + friends[3])

# A3
print(friends[1:4])
print(friends[-2:])

# A4
friends[-2:] = ["Elzero","Elzero"]
print(friends)

# A5
myNewFriends = ["Osama","Ahmed","Sayed"]
myNewFriends.insert(0,"Nasser")

print(myNewFriends)

myNewFriends.append("Salem")
print(myNewFriends)

# A6
friends = ["Nasser","Osama","Ahmed","Sayed","Salem"]

friends[:2] = []
print(friends)

# friends.remove("Salem")
# OR
friends[-1:] = []
print(friends)

# A7
friends = ["Ahmed","Sayed"]
employees = ["Samah","Eman"]
school = ["Ramy","Shady"]

# friends = friends + employees + school
# OR
friends.extend(employees)
friends.extend(school)
print(friends)

# A8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)

friends.sort(reverse=True)
print(friends)

# A9
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))


# A10
technologies = ["Html","CSS","JS","Python",["Django","Flask","Web"]]
print(technologies[4][0])
print(technologies[4][2])









