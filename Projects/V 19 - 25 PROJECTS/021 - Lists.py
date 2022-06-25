# -----------
# -- Lists --
# -----------
# [1] List Items are Enclosed in Square Brackets 
# [2] List are Ordered, To Use Index To Access Item
# [3] List are Mutable => Add, Delete, Edit
# [4] List Items are not Unique # for example ["one", "two", "one"]
# [5] List can have different data types 
# -----------
myAwesomeList = ["One","Two","One",1,100.5,True]

print(myAwesomeList) # Whole List
print(myAwesomeList[1]) # "One" # Type String
print(myAwesomeList[-1]) # True 
print(myAwesomeList[-3]) # 1

print(myAwesomeList[1:4]) # ['Two', 'One', 1]
print(myAwesomeList[:4]) # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:]) # ['Two', 'One', 1, 100.5, True]
print(myAwesomeList[::1]) # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2]) # ['One', 'One', 100.5]

print(myAwesomeList)
myAwesomeList[1] = 2
print(myAwesomeList)
myAwesomeList[-1] = False
print(myAwesomeList)
myAwesomeList[:3] = ["A"] # NOT ERROR THIS IS NOT REPLACE, BUT EDIT !!!!!!!!!!!!!!!!!
print(myAwesomeList)
# The End ...











