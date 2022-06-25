# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------

# List Contains Admins
from os import stat


admins = ["Ahmed","Osama","Sameh","Manal","Rahma","Mahmoud","Enas"]

# Login
name = input("Please Type Your Name : ").strip().capitalize()

# If Name is In Admin
if name in admins:
    print(f"Hello {name} Welcome Back")
    # Beautiful Note
    print("*" * 80)
    print(" You Can Type The first Letter Only ".center(80,"*"))
    print("*" * 80)
    option = input("Delete Or Update Your Name ?").strip().capitalize()
    # Update Option
    if option == "Update" or option == "U":
        theNewName = input("Your New Name Please : ").strip().capitalize()
        print(theNewName)
        admins[admins.index(name)] = theNewName
        print("Name Updated.")
        print(admins)
    # Delete Option
    elif option == "Delete" or option == "D":
        admins.remove(name)
        print("Name Deleted.")
        print(admins)
    # Wrong Option
    else:
        print("Wrong Option, Please Try again Later.")
else:
    status = input("You Are Not An Admin, Would You Like To Be An Admin ?? Yes Or No ?").strip().capitalize()
    if status == "Yes" or status == "Y":
        print("You Have Been Added")
        admins.append(name)
        print(admins)
    else:
        print("You Are Not Added.")