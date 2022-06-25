# ------------------------
# -- Strings Formatting --
# ------------------------

name = "Osama"
age = 36
rank = 10

print("My name is: " + name) # Correct
# print("My name is: " + name + " and My Age is: " + age) # Error cant add stings to int

print("My name is: %s" %name)
print("My name is: %s and My Age is: %d" %(name,age)) # s stands for string , d stands for digit
print("My name is: %s and My Age is: %d and my Rank is: %f" %(name,age,rank)) #f stands for floating point
# %s -> String 
# %d -> Number
# %f -> Float

n = "Osama"
l = "Python"
y = 10
print("My name is %s, Iam %s Developer With %d years Exp." %(n,l,y))

# Control Floating point number 

myNumber = 10 
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)

# Truncate String 

myLongString = "Hello people of Elzero Web School I Love You All"
print("Message is %.5s" %myLongString)
