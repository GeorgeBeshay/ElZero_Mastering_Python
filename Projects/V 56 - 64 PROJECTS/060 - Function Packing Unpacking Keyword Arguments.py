# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

# def show_skills(*skills):
#     print(type(skills))
#     for skill in skills:
#         print(F"{skill}")

# show_skills("Html","CSS","JS")

mySkills = {
    "Html" : "80%",
    "CSS" : "70%",
    "JS" : "50%",
    "Python" : "80%",
    "Go":"40%"
}

def show_skills(**skills):
    print(type(skills))
    for skill,Value in skills.items():
        print(F"{skill} => {Value}")

show_skills(**mySkills)