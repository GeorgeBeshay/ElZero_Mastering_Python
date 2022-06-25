# A L060 - L064
# -------------




# A1
# ----

# def get_score(**subjects):
#     for subject,grade in subjects.items():
#         print(f"{subject} => {grade}")
# get_score(Math = 90,Science = 80,Language = 70)
# get_score(Logic = 70,Problems = 60)




# A2
# ----

# def get_people_scores(name="Unknown",**subjects):
#     if len(subjects) != 0:
#         if name != "Unknown":
#             print(f"Hello {name} This Is Your Score Table:")
#         for subject,grade in subjects.items():
#             print(f"{subject} => {grade}")
#     else:
#         if name != "Unknown":
#             print(f"Hello {name} You Have No Scores To Show.")
#         else:
#             print("No Input Was Given Sorry, Please Enter Your Name And Scores To Show Them")

# get_people_scores("George",Math = 90,Science = 80,Language = 70)
# print("*"*40)
# get_people_scores("Mahmoud",Logic = 70,Problems = 60)
# print("*"*40)
# get_people_scores(Logic = 70,Problems = 60)
# print("*"*40)
# get_people_scores("Ahmed")
# print("*"*40)
# get_people_scores()




# A3
# ----

scores_list = {
    "Math" : 90,
    "Science":80,
    "Language":70
}

def get_the_scores(name = "Unknown",**scores):
    if len(scores) != 0:
        if name != "Unknown":
            print(f"Hello {name} This Is Your Score Table:")
        for subject, grade in scores.items():
            print(f"{subject} => {grade}")
    else:
        if name != "Unknown":
            print(f"Hello {name}, You Have No Scores To Show.")
        else:
            print("Sorry No Input Was Given,Please Enter Your Name And Scores To Show Them.")

get_the_scores("George",**scores_list)
print("*"*40)
get_the_scores("George")
print("*"*40)
get_the_scores(**scores_list)