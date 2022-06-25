# ---------------
# -- Generator --
# ---------------
# [1] Generator Is A Function With "yield" Keyword Instead Of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have One or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From The Beginning
# [5] When Called, It Doesn't Start Automatically, It Only Gives You The Control
# -----------------------------------------------------------------------------------

def myGenerator():
    yield 1
    yield 2
    yield 3 
    yield 4
# print(myGenerator())
myGen = myGenerator()
print(next(myGen))
print("Hello From Python")
print(next(myGen))

print("#" * 50)

for number in myGen:
    print(number)