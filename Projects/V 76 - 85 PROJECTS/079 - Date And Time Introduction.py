# -----------------------------------
# -- Date And Time => Introduction --
# -----------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print The Current Date And Time 
print(datetime.datetime.now())

print("#"*50) # Separator -----------------

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#"*50) # Separator -----------------

# Print Start And End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#"*50) # Separator -----------------

# print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("#"*50) # Separator -----------------

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minutes
print(datetime.datetime.now().time().minute)

# Print The Current Time Seconds
print(datetime.datetime.now().time().second)

print("#"*50) # Separator -----------------

# Print Start And End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("#"*50) # Separator -----------------

# Print Specific Date
print(datetime.datetime(2002,6,4))
print(datetime.datetime(2002,6,4,10,45,55))

print("#"*50) # Separator -----------------

myBirthday = datetime.datetime(2002,6,4)
dateNow = datetime.datetime.now()

print(f"My Birthday is {myBirthday}",end = "")
print(f" Date Now Is {dateNow}",end = "")

print(f"I Lived For {dateNow - myBirthday}")
print(f"I Lived For {(dateNow - myBirthday).days} Days")