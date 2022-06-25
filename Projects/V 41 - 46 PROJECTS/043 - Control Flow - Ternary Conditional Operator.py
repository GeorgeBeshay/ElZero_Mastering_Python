# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "Egypt"

if country == "Egypt": print(f"The Weather in {country} is 15.")
elif country == "KSA": print(f"The Weather in {country} is 30.")
else: print(f"The Country is not in the list.")

# Short If

movieRate = 18
age = 18    

if age < movieRate:
    print("Movie Is Not Good For You.") # Condition if True
else:
    print("Movie Is Good For You And Happy Watching.") # Condition if False

print("Movie Is Not Good For You" if age < movieRate else "Movie Is Good For You And Happy Watching.")

# Condition If True | If Condition | Else | Condition If False.