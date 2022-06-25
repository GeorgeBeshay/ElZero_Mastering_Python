# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

# a,b,c = "Osama","Ahmed","Sayed"
# list = [a,b,c]

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# def =>                    Function Keyword [Define]
# say_hello() =>            Function Name
# name =>                   Parameter
# print(f"Hello {name}") => Task
# say_hello("Ahmed") =>     Ahmed is The Argument

# def say_hello(name):
#     print(f"Hello {name}")
# for i in range (3):
#     say_hello(list[i])

def addition(n1,n2):
    if type(n1) != int or type(n2) != int:
        print("Only Integers Allowed")
    else:
        print(n1+ n2)

addition(100,20)
addition(100,"-50")
addition(100,"Osama")

def full_name(first,middle,last):
    print(f"Hello {first.strip().capitalize()} {middle.strip().upper():.1s} {last.strip().capitalize()}")
full_name("           george           ","         samy        ","         wahba         ")