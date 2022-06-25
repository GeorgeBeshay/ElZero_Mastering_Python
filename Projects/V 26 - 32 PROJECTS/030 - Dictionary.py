# ----------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces 
# [2] Dict Items Contain Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not allowed
# [4] Dict Value Can Have Any Data Types 
# [5] Dict Key Need to be Unique ( will save the last update )
# [6] Dict is Not Ordered You Access Its Elements With Key
# ----------------

# Dictionary 

user = {
 "name" : "Osama" ,
 "age" : 36 ,
 "country": "Egypt",
 "skills" : ["Html" , "Css" , "Js"],
 "rating" : 10.5,
 "name" : "Ahmed" # Value will be updated
}
print(user)
print(user["country"])
print(user.get("rating"))

print(user.keys())
print(user.values())

# Two Dimensional Dictionary 

languages = {
    "One" : {
        "name" : "Html",
        "Progress" : "80%"
            },
    "Two" : {
        "name" : "Css",
        "progress" : "90%"
            },
    "Three" : {
        "name" : "Js",
        "progress" : "90%"
            }
            }

print(languages)
print(languages["One"])
print(languages["Three"]["name"])

# Dictionary Length 

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
    "name" : "Vuejs",
    "progress" : "80%"
}

frameworkTwo = {
    "name" : "ReactJs",
    "progress" : "80%"
}

frameworkThree = {
    "name" : "Angular",
    "progress" : "80%"
}

allFramework = {
    "one" : frameworkOne,
    "two" : frameworkTwo,
    "three" : frameworkThree
}

print(allFramework)

# The End ...



