# ----------------
# -- User Input --
# ----------------

fName = input("What\'s is Your First Name ? ")
mName = input("What\'s is Your Middle Name ? ")
lName = input("What\'s is Your Last Name ? ")

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName} Happy To See you <3 ")
