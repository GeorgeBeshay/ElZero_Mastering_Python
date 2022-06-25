# ------------------
name = "Osama"
age = 36
rank = 10

print("My name is: {}" .format("Osama"))
print("My name is: {}" .format(name))
print("My name is: {} and My Age is: {}" .format(name,age)) 
print("My name is: {:s} and My Age is: {:d} and my Rank is: {:f}".format(name,age,rank))
# {:s} -> String 
# {:d} -> Number
# {:f} -> Float

n = "Osama"
l = "Python"
y = 10
print("My name is {:s}, Iam {:s} Developer With {:d} years Exp." .format(n,l,y))


# Control Floating point number 

myNumber = 10 
print("My Number is: {:d}" .format( myNumber))
print("My Number is: {:f}" .format( myNumber))
print("My Number is: {:.2f}" .format( myNumber))

# Truncate String 

myLongString = "Hello people of Elzero Web School I Love You All"
print("Message is {:s}" .format(myLongString))
print("Message is {:.5s}" .format(myLongString))
print("Message is {:.13s}" .format(myLongString))

# Format Money
myMoney = 500162350198

print("My Money in Bank Is: {}".format(myMoney))
print("My Money in Bank Is: {:,.2f}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))
# print("My Money in Bank Is: {:&d}".format(myMoney)) #wrong

# ReArrange Items 
a,b,c = "one" ,"Two" ,"Three"
print("Hello {} {} {} ".format(a,b,c)) # Hello One Two Three
print("Hello {1} {2} {0} ".format(a,b,c)) # Hello Two Three One
print("Hello {2} {0} {1} ".format(a,b,c)) # Hello Three One Two

x,y,z = 10,20,30
print("Hello {} {} {} ".format(x,y,z))
print("Hello {1:d} {2:d} {0:d} ".format(x,y,z))
print("Hello {2:f} {0:f} {1:f} ".format(x,y,z))
print("Hello {2:.2f} {0:.4f} {1:.5f} ".format(x,y,z))

# Format in Version 3.6+ 
myName = "Osama"
myAge = 36

print("My Name is: {myName} and My Age is {myAge}")
print(f"My Name is: {myName} and My Age is {myAge}")

# The End.. 
