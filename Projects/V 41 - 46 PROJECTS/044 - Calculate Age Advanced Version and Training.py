# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Write A Very Beautiful Note
print("*" * 80)
print(" You Can Write The First Letter Or Full Name Of The Time Unit ".center(80,"*"))
print("*" * 80)

# Collect Age Data
age = int(input("Please Write Your Age : ").strip())

# Collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Weeks, Days").strip().lower()

# Get Time Units
months = age * 12
weeks = months * 4
days = age * 365

if unit == "months" or unit == "m" :
    print("You Chose The Unit Months ...")
    print(f"You Lived For {months:,} Months.")
elif unit == "weeks" or unit == "w":
    print("You Chose The Unit Weeks ...")
    print(f"You Lived For {weeks:,} Weeks.")
elif unit == "days" or unit == "d":
    print("You Chose The Unit Days ...")
    print(f"You Lived For {days:,} Days.")