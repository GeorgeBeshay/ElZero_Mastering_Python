# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

# print(1,2,3,4)

# myList = [1,2,3,4]

# print(myList)
# print(*myList)

# def say_hello(*people):
#     for name in people:
#         print(f"Hello {name}")

# say_hello("Osama","Ahmed","Sayed","Mahmoud","Alaa")

def show_details(name,*skills):
    print(f"Hello {name}, Your Skills Is: ")
    for skill in skills:
        print(f"{skill}")
show_details("Osama","Html","CSS","JS","Python","Data Science")
show_details("Ahmed","Html","CSS","JS","Python","Data Science","PHP","MySQL")