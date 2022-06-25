# A L086 - L089
# ----------------

# Function That Will be used
def List_C_T_String(list):
    myString = ""
    return myString.join(list)

# A1
# ---

my_list = ["E","Z","R",1,2,3]
my_tuple = ("L","E","O")
my_data = []

for data in zip(my_list,my_tuple):
    for item in data:
        my_data.append(item)

my_data = List_C_T_String(my_data).lower().capitalize()
print(my_data)

print("=" * 50)

# A2
# ---

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if type(item2) == int:
        break
    my_data.append(item2)
    my_data.append(item3)

my_data = List_C_T_String(my_data).lower().capitalize()
print(my_data)

print("=" * 50)

# A3
# ---

from PIL import Image
# First Demand
myImage = Image.open("E:\Courses & Self-Learning\[0] Mastering Python\Assignments\Assignments L086 ~ L094\elzero-pillow.png")
# box = (400,0,800,400)
# croppedImage = myImage.crop(box)
# croppedImage = croppedImage.convert("L")
# croppedImage.show()
# croppedImage.save("E:\Courses & Self-Learning\[0] Mastering Python\Assignments\Assignments L086 ~ L094\elzero-pillow-cropped.png")

# Second Demand

# box2 = (0,400,1200,800)
# croppedImage2 = myImage.crop(box2)
# croppedImage2 = croppedImage2.rotate(180).convert("L")
# croppedImage2.show()
# croppedImage2.save("E:\Courses & Self-Learning\[0] Mastering Python\Assignments\Assignments L086 ~ L094\elzero-pillow-cropped2.png")

print("=" * 50)

# A4
# ---

def say_hello_to(someone):
    '''
    "Parameter(someone) => Person Name"
    "Function To Say Hello To Anyone"
    '''
    return(f"Hello {someone}")

print(say_hello_to("George"))
# print(dir(say_hello_to))
print(say_hello_to.__doc__)
# help(say_hello_to)

print("=" * 50)

# A5
# ---
# SOLVED IN A SEPARATE FILE
myFriends = ["Ahmed", "Osama", "Sayed"]

def sayHello(SomePeople) -> list:
    for Someone in SomePeople:
        print(f"Hello {Someone}")

sayHello(myFriends)