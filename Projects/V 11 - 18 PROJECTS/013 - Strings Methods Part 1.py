# ---------------
# -- Strings Method --
# ---------------

# len
a = "I Love Python"
print(len(a)) # Start Counting from 1 ...
print(a[12]) # Start Counting from 0 ...

b = "      I Love Python"
print(len(b))

# strip() rstrip() lstrip()
a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())


a = "@#@#@#@#@#I Love Python@#@#@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize() 
# Makes the first Character only Capital and the rest small 

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill
c , d , e , f= "1" , "33" , "111" , "1111"
print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))


# upper()

g = "george"
print(g.upper())

# lower()
g = "GEORGE"
print(g.lower())






