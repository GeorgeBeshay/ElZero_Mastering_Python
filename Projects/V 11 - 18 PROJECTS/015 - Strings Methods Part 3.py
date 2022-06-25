# -------------------
# -- Strings Method--
# -------------------

# index(substring, start, end)

# a = "I Love Python"
# print(a.index("P")) # Index number 7 
# print(a.index("P",0,10)) # Index number 7
# print(a.index("P",0,5)) # Error


# find(substring, start, end)

# b = "I Love Python"
# print(b.find("P")) # Index number 7 
# print(b.find("P",0,10)) # Index number 7
# print(b.find("P",0,5)) # -1


# rjust(width, fill char) ljust(width, fill char)

c = "George"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "George"
print(d.ljust(10))
print(d.ljust(10, "#"))


# splitlines()
e = """First line
Second Line
Third Line"""
print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"
print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(20))

one = "I Love Python And 3G"
print(one.istitle()) # Title -> el7rf el awl fe kol kelma capital + el7rf el b3d el rkm
two = "I Love Python And 3g"
print(two.istitle()) 
three = " "
print(three.isspace())
four = ""
print(four.isspace())
five = 'i love python'
six = "I Love Python"
print(five.islower())
print(six.islower()) 

seven = "Osama_Elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero"

print(seven.isidentifier()) # identifier -> can be a variable name ..
print(eight.isidentifier())
print(nine.isidentifier()) 

x = "AaaaaaBbbbbb"
y = "AaaaaaBbbbbb1111111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaaBbbbbb"
z = "AaaaaaBbbbbb1111111"
print(u.isalnum())
print(z.isalnum())
# The end :D







