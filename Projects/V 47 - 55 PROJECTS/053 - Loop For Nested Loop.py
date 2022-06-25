# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

# people = ["Osama","Ahmed","Sayed","Ali"]
# skills = ["Html","Css","Js"]

# for name in people: # Outer Loop
#     print(f"{name} Skills Is: ")
#     for skill in skills: # Inner Loop
#         print(f"- {skill}")

people = {
    "Osama":
    {
        "Html":"70%",
        "Css":"80%",
        "Js":"70%"
    },
    "Ahmed":
    {
        "Html":"90%",
        "Css":"80%",
        "Js":"90%"
    },
    "Sayed":
    {
        "Html":"70%",
        "Css":"60%",
        "Js":"90%"
    }
}
# print(people["Osama"])
# print(people["Sayed"]["Css"])

for name in people:
    print(f"~ Skills and Progress For {name} Is: ")
    for skill in people[name]:
        print(f"{skill.upper()} => {people[name][skill]}")
    print("*"*50)