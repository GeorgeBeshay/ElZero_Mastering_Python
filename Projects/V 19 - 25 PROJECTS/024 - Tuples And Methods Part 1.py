# -----------
# -- Tuple --
# -----------
# [1] Tuple Items are enclosed in parentheses
# [2] You can Remove The parentheses if you want 
# [3] Tuple are ordered, Use index to access item
# [4] Tuple are Immutable => You Cant add or delete 
# [5] Tuple Items are not Unique # can place the same item more than once 
# [6] Tuple Can Have Different Data Types 
# [7] Operators Used in Strings and lists Available in Tuples
# ----------- 

# Tuple Syntax & Type

myAwesomeTupleOne = ("Osama" , "Ahmed")
myAwesomeTupleTwo = "Osama" , "Ahmed"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))

# Tuple Indexing

myAwesomeTupleThree = (1,2,3,4,5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])

# Tuple Assign Values

myAwesomeTupleFour = (1,2,3,4,5)
# myAwesomeTupleFour[2] = "Three" # ERROR 

# print(myAwesomeTupleFour)

# Tuple Items 

myAwesomeTupleFive = ("Osama","Osama",1,2,3,100.5,True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])

# The End ...
