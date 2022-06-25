# ---------------
# --- Numbers ---
# ---------------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))
print(type(0))

# Float

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex 

myComplexNumber = 5 + 6j
print(type(myComplexNumber))
print(f"Real part is: {myComplexNumber.real}")
print("Real part is: {}".format(myComplexNumber.real)) 
print("Imaginary part is: {}".format(myComplexNumber.imag)) 

# [1] You can convert from Int to Float or complex
# [2] You can convert from float to Int or complex
# [3] You cannot convert from Complex to any type 

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+9j)
# print(int(10+9j)) # Error cant convert 
# print(float(10+9j)) # Error cant convert 
# The end ...
