# A L079 - L080
# -------------



# A1
# ---

import datetime

print(f"The Date is {datetime.datetime(2021,6,25)}")
print(f"Today Is {datetime.datetime.now()}")
print(f"Days From {datetime.datetime(2021,6,25)} To {datetime.datetime.now()} Is => {datetime.datetime.now() - datetime.datetime(2021,6,25)}")

print("#"*50) # Separator ---------------------------------------------

# A2
# ---

today = datetime.datetime.now()
print(today)
print(today.strftime("%b %d,%Y"))
print(today.strftime("%d - %b - %Y"))
print(today.strftime("%d / %b / %y"))
print(today.strftime("%d / %B / %Y"))
print(today.strftime("%a, %d %B %Y"))

print("#"*50) # Separator ---------------------------------------------