# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in 
# --------------------------

# String 

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("*" * 50) # Separator

# List

friends = ["Ahmed","Sayed","Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("@" * 50) # Separator

# Using In and Not In With If Conditional 

countriesOne = ["Egypt","KSA","Kuwait","Bahrain","Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy","USA"]
countriesTwoDiscount = 50

mycountry = "Italy"

if mycountry in countriesOne:
    print(f"Hello You Have A Discount Equal To $ {countriesOneDiscount}.")
elif mycountry in countriesTwo:
    print(f"Hello You Have A Discount Equal To $ {countriesTwoDiscount}.")
else:
    print("You Have No Discount.")