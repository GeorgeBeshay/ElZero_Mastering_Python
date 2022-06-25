# # ---------
# # -- Set --
# # ---------
# # [1] Set Items are Enclosed in Curly Braces
# # [2] Set Items are Not Ordered and Not Indexed
# # [3] Set Indexing and Slicing Cant be Done 
# # [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not 
# # [5] Set Items are Unique
# # --------

# # Not Ordered and Not Indexing

# mySetOne = { "Osama", "Ahmed", 100}
# print(mySetOne)
# # print(mySetOne[1]) # Error

# # Slicing Cant Be Done

# mySetTwo = {1,2,3,4,5,6}
# # print(mySetTwo[0:3]) # Error

# myTuple = (1,2,3,4,5,6)
# print(myTuple[0:3])

# # Has Only Immutable Data Types

# # mySetThree = {"Osama", 100, 100.5, True,[1,2,3]} # Error because of the list
# mySetThree = {"Osama", 100, 100.5, True,(1,2,3)} 

# print(mySetThree)

# # Items are Unique

# mySetFour = {1,2,"Osama","One","Osama",1}
# print(mySetFour)

# # The End .......


b = "# # @%^ i love python # #"
print(b.rstrip("# #"))
print(b.lstrip("# #"))
print(b.strip("# #"))