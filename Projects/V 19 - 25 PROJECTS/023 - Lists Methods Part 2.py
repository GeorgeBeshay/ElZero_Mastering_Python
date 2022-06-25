# -------------------
# -- Lists Methods --
# -------------------

# clear()

a = [1,2,3,4]
a.clear()
print(a)

# copy()

b = [1,2,3,4]
c = b.copy()

print(b) # Main List
print(c) # Copied List

b.append(5)

print(b) # Main List
print(c) # Copied List, Notice That it is not affected by the change in b

# count()

d = [1,2,3,4,3,9,10,1,2,1]

print(d.count(1))

# index()

e = ["Osama","Ahmed","Sayed","Ramy","Ahmed","Ramy"]
print(e.index("Ramy")) # first Index ONLY 

# insert()

f = [1,2,3,4,5,"A","B"]
f.insert(2,"Test")
f.insert(-1,"Test")

print(f)

# pop()

g = [1,2,3,4,5,"A","B"]
print(g.pop(-3))

# The End 
