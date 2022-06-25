# A L051 ~ L055
# -------------




# A1
# ----

# my_nums = [15,81,5,17,20,21,13]
# my_nums.sort(reverse=True)
# counter = 0

# for num in my_nums:
#     if num % 5 == 0:
#         print(f"{counter+1} => {num}")
#         counter += 1
#     else:
#         continue # Notice That: At this line, we can also use pass, but continue forced the loop to enter the next count, while pass means there is no code in this line to execute
# print("All Numbers Printed")




# A2
# ----

# banned = [6,8,12]
# for i in range(20):
#     if (i+1) in banned:
#         continue
#     else:
#         print(str(i+1).zfill(2))
# print("All Numbers Printed.")




# A3
# ----

# my_ranks = {
#     "Math":"A",
#     "Science":"B",
#     "Drawing":"A",
#     "Sports":"C"
# }
# grades_equivalent = {
#     "A":100,
#     "B":80,
#     "C":40
# }
# total_points = 0
# for rank in my_ranks:
#     print(f"My Rank in {rank} Is {my_ranks[rank]} And This Is Equal To {grades_equivalent[my_ranks[rank]]} Points.")
#     total_points += grades_equivalent[my_ranks[rank]]
# print(f"Total Points Is {total_points}")




# A4
# ----

# students = {
#     "Ahmed":{
#         "Math":"A",
#         "Science":"D",
#         "Draw":"B",
#         "Sports":"C",
#         "Thinking":"A"
#     },
#     "Sayed":{
#         "Math":"B",
#         "Science":"B",
#         "Draw":"B",
#         "Sports":"D",
#         "Thinking":"A"
#     },
#     "Mahmoud":{
#         "Math":"D",
#         "Science":"A",
#         "Draw":"A",
#         "Sports":"B",
#         "Thinking":"B"
#     }
# }
# grades_equivalent = {
#     "A":100,
#     "B":80,
#     "C":40,
#     "D":20
# }

# Method 1
# --

# for name in students:
#     total_points = 0
#     print("-"*30)
#     print(f"-- Student Name => {name}")
#     print("-"*30)
#     for subject in students[name]:
#         print(f"- {subject} => {grades_equivalent[students[name][subject]]} Points.")
#         total_points += grades_equivalent[students[name][subject]]
#     print(f"Total Points For {name} Is {total_points}")

# Method 2
# --

# for name in students:
#     total_points = 0
#     print("-"*30)
#     print(f"-- Student Name => {name}")
#     print("-"*30)
#     for subject,grade in students[name].items():
#         print(f"- {subject} => {grades_equivalent[grade]} Points.")
#         total_points += grades_equivalent[students[name][subject]]
#     print(f"Total Points For {name} Is {total_points}")