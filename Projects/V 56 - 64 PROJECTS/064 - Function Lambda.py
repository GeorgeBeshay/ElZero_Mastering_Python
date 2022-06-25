# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function 
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda Is One Single Expression not Block of Code 
# [6] Lambda Type Is Function 
# ----------------------------------------------------------------------

def say_hello(name,age): return f"Hello {name} Your Age Is: {age}"
hello = lambda name,age: f"Hello {name} Your Age Is: {age}"
print(say_hello("George",19))
print(hello("George",19))

print(say_hello.__name__)
print(hello.__name__)

print(type(hello))