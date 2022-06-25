# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module Is A File Contain A Set Of Functions 
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules 
# [4] You Can Create Your Own Modules 
# [5] Modules Saves Your Time 
# --------------------------------------------------

# Import Main Module 
# import random
# print(random)
# print(f"Printing Random Float Number {random.random()}")

# Show All Functions Inside Module
# import random
# print(dir(random))

# Import One Or Two Functions From Module
from random import randint, random
print(f"Printing Random Float {random()}")
print(f"Printing Random Integer {randint(100,900)}")