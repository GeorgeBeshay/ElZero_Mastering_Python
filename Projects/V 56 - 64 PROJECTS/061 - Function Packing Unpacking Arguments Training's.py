# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

myTuple = ("Html","CSS","JS")


mySkills = {
    "Go":"80%",
    "Python":"50%",
    "MySQL":"80%"
}

def show_skills(name,*skills,**skillsWithProgress):
    print(f"Hello {name} \nSkills Without Progress: ")
    for skill in skills:
        print(f"- {skill}")
    print(f"Skills With Progress Are: ")
    for skill_key,skill_value in skillsWithProgress.items():
        print(f"- {skill_key} => {skill_value}")
show_skills("George",*myTuple,**mySkills)