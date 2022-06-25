# A L047 - L050
# --------------




# A1
# ----

# num = int(input("Please Enter Number Greater Than 0: ").strip())
# num_history = num -1
# if num <= 0 :
#     print(f"Number {num} Is Not Larger Than 0")
# else:
#     pass

#     # Counter 
#     c = 0

#     while num > 1:
#         num -= 1
#         if num != 6:
#             print(num)
#         else:
#             c += 1
#             num -= 1
#             continue
#     print(f"{num_history-c} Numbers Printed Successfuly.")




# A2
# ----

# friends = ["Mohamed","Shady","ahmed","eman","Sherif"]

# # Ignored Names Counter
# c = 0

# # Track Counter
# a = 0

# while a < len(friends):
#     if friends[a][0].isupper():
#         print(friends[a])
#         a += 1
#     else:
#         c += 1
#         a += 1
#         pass
# print(f"Friends Printed And Ignored Names Count Is {c}")




# A3 
# ----

skills = ["HTML","CSS","JavaScript","PHP","Python"]
while skills:
    for skill in skills: print(skill)
    break



# A4
# ----

# my_friends = []
# max_friends = 4

# while max_friends > 0:
#     friend = input("Please Enter Your Friend Name To Be Added: ").strip()
#     if friend.isupper():
#         print("Invalid Name.")
#     elif friend.islower():
#         my_friends.append(friend.capitalize())
#         max_friends -= 1
#         print(f"Friend {friend} Added => 1st Letter Became Capital")
#         print(f"Names Left in list are {max_friends}")
#     elif friend[0].isupper():
#         my_friends.append(friend.lower().capitalize())
#         max_friends -= 1
#         print(f"Friend {friend.lower().capitalize()} Added")
#         print(f"Names Left in list are {max_friends}")
# print(f"Your Friend List is: {my_friends}")