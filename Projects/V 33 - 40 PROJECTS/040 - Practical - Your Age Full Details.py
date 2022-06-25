# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Input Age
age = int(input("What's Your Age ?? ").strip())

# Get Age in All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24 
minutes = hours * 60
seconds = minutes * 60

print(f"You Lived For: \n{months} Months. \n{weeks:,} Weeks. \n{days:,} Days. \n{hours:,} Hours. \n{minutes:,} Minutes. \n{seconds:,} Seconds.")
