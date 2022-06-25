# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

# myFile = open(r"E:\Courses & Self-Learning\[0] Mastering Python\V 65 - 68 PROJECTS\george.txt","w")
# myFile.write("Hello From Python File With Love\n")
# myFile.write("Second Line")

# myFile = open(r"E:\Courses & Self-Learning\[0] Mastering Python\V 65 - 68 PROJECTS\fun.txt","w")
# myFile.write("Elzero Web School\n" * 1000)

# mylist = ["Osama\n","Ahmed\n","Sayed\n"]

# myFile = open(r"E:\Courses & Self-Learning\[0] Mastering Python\V 65 - 68 PROJECTS\george.txt","w")
# myFile.writelines(mylist)

myFile = open(r"E:\Courses & Self-Learning\[0] Mastering Python\V 65 - 68 PROJECTS\george.txt","a")
myFile.write(" Samy")
