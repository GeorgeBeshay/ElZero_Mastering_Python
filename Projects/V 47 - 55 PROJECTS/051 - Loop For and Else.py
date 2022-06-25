# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object:
#   Do Something With Item
# ----------------------------
# item Is A Variable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [List,tuples,set,dict,string of characters,etc ...]

myNumbers = [1,2,3,4,5,6,7,8,9]
for number in myNumbers:
    if number % 2 == 0:
        print(f"The Number {number} Is Even.")
    else:
        print(f"The Number {number} Is Odd.")
else:
    print("The Loop Is Finished")

myName = "George"
for letter in myName:
    print(f"[ {letter.upper()} ]")