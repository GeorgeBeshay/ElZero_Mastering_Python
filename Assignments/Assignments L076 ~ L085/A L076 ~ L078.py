# A L076 - L078
# -------------



# A1
# ---

import random

print(f"Random Number Between 10 and 50 => {random.randint(10,50)}")
# -------------------------------------------------------------------
x = random.randint(2,10)
while x % 2 != 0:
    x = random.randint(2,10)
else:
    print(f"Random Even Number Between 2 and 10 => {x}")
# -------------------------------------------------------------------
y = random.randint(1,9)
while y % 2 == 0:
    y = random.randint(1,9)
else:
    print(f"Random Odd Number Between 1 and 9 => {y}")
# -------------------------------------------------------------------
print(dir(random))
# -------------------------------------------------------------------
print("#"*50)



# A2 & A3
# -------

# [SOLVED IN A SEPERATE FOLDER CHECK IT !!]
