# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Becuase It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

# Use Map With PreDefined Function

def formatText(text):
    return f"- {text.strip().lower().capitalize()} -"

myTexts = [" OSama ","AHMED"," sAYed "]

# myFormatedData = map(formatText,myTexts)
# print(myFormatedData    )
for name in list(map(formatText,myTexts)):
    print(name)

print("#"*39) # Separator

# Use Map With Lambda Function

# def formatText(text):
#     return f"- {text.strip().lower().capitalize()} -"

myTexts = [" OSama ","AHMED"," sAYed "]
for name in list(map((lambda text: f"- {text.strip().lower().capitalize()} -"),myTexts)):
    print(name)

print("#"*39) # Separator