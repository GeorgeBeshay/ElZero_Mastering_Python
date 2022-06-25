# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable,start = 0)

mySkills = ["Html","Css","Js","PHP"]
mySkillsWithCounter = enumerate(mySkills,20)
print(type(mySkillsWithCounter))
for Counter,skill in mySkillsWithCounter:
    print(f"{Counter} - {skill}")

print("="*39) # Separator # --------------------------

# help()

print(help(print))

print("="*39) # Separator # --------------------------

# reversed(Iterable)

# Example 1
myString = "Elzero"
for letter in reversed(myString):
    print(letter)

print("="*39) # Separator # --------------------------

# Example 2
mySkills = ["Html","Css","Js","PHP"]
for s in reversed(mySkills):
    print(s)