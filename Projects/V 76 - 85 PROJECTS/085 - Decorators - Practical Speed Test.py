# ---------------------------------------
# -- Decorator => Practical Speed Test --
# ---------------------------------------
from time import time 

# def myDecorator(func):
#     def nestedFunc(*numbers):
#         for number in numbers:
#             if number < 0:
#                 print("Beaware One of The Numbers is Less Than Zero.")
#                 break # So It Doesnt Print the message for each negative number
#         func(*numbers)
#     return nestedFunc

# @myDecorator
# def calculate(n1,n2,n3):
#     print(n1+n2+n3)

# calculate(-10,90,-5)

def speedTest(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Function Running Time Is {end - start}")
    return wrapper

@speedTest
def bigLoop():
    for number in range(1,20000):
        print(number)

bigLoop()