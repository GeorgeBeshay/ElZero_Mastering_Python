# A L072 - L075
# -------------



# A1
# ----

friends_map = ["AEmanS","AAhmedS","DSamehF","LOsamaL"]
def remove_chars(string):
    string = string[1:-1]
    return string
cleand_list = map(remove_chars,friends_map)
for cleaned_name in cleand_list:
    print(cleaned_name)

print("="*39) # Separator # -----------------------------



# A2
# ----

friends_filter = ["Osama","Wessam","Amal","Essam","Gamal","Othman"]
def get_names(awesomeString):
    return awesomeString.endswith("m")
names = filter(get_names,friends_filter)
for name in names:
    print(name)

print("="*39) # Separator # -----------------------------



# A3 
# ----

# Method 1
from functools import reduce
from typing import Counter
nums = [2,4,6,2]
def multiplying(num1 , num2):
    return num1 * num2
print(reduce(multiplying,nums))

# Method 2
print(reduce((lambda num1,num2: num1*num2),nums))

print("="*39) # Separator # -----------------------------



# A4 
# ----

skills = ("HTML","CSS",10,"PHP","Python",20,"JavaScript")
skills = reversed(skills)
skills = enumerate(skills,50)
for counter,skill in skills:
    if type(skill) != int:
        print(f"{counter} - {skill}")

print("="*39) # Separator # -----------------------------