# A L033 ~ L037 
# -------------

# A1 
# ----

print(bool("George"))         #1
print(bool(100))              #2
print(bool(100.99))           #3
print(bool(True))             #4
# print(bool([1,2,3,4]))      EXTRA
# print(bool((1,2,3,4)))      EXTRA

print(bool(0))                #5
print(bool(False))            #6
print(bool([]))               #7
print(bool(()))               #8
# print(bool(""))             EXTRA

print ("=" * 50) # SEPARATOR

# A2
# ----

html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50 )

print ("#" * 50) # SEPARATOR

# A3
# ----

num_one = 10
num_two = 20
num = 20 

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

print ("*" * 50) # SEPARATOR

# A4
# ----

num_one = 10
num_two = 20

result = num_one + num_two
print(result)

result **= 3
print(result)

result %= 26000
print(result)

result /= 5  # FLOAT
print(result)

result = str(result)
print(type(result))

print ("@" * 50) # SEPARATOR