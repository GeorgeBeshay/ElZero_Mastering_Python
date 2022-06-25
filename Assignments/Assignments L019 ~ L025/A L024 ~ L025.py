# L024 ~ L025
# A1
myAwesomeTuple = "George",
print(myAwesomeTuple[0])
print(type(myAwesomeTuple))

# A2
friends = ("Osama","Ahmed","Sayed")
friends = list(friends)
friends[0] = "Elzero"
friends = tuple(friends)
print(friends)
print(type(friends))
print(str(len(friends)) + " Elements")

# A3
nums = (1,2,3)
letters = ("A","B","C")
nums_and_letters_one = nums + letters 
print("nums_and_letters_one = " + str(nums_and_letters_one))
print(str(len(nums_and_letters_one)) + " Elements")

# A4
my_tuple = (1,2,3,4)
a,b,_,c = my_tuple

print(a)
print(b)
print(c)

# The End ..
