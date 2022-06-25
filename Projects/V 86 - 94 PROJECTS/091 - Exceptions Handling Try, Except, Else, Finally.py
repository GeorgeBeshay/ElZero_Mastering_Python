# ----------------------------------------
# --        Exceptions Handling         --
# -- Try | Except | Else | Finally      --
# ----------------------------------------
# Try => Test The Code For Errors
# Except => Handle The Errors
# ----------------------------------------
# Else => If No Errors
# Finally => Run The Code
# ----------------------------------------

# number = int(input("Write Your Age: "))
# print(number)
# print(type(number))

# try: # Try The Code and Test Errors
#     number = int(input("Write Your Age: "))
#     print("Good, This Is Integer From Try")
# except: # Handle The Error If Its Found
#     print("Bad, This Is Not Integer")
# else: # If There Is No Error
#     print("Good, This Is Integer From Else")
# finally:
#     print("Print From Finally Whatever Happens")

try:
    # print(10/0)
    # print(x)
    print(int("Hello"))
except ZeroDivisionError:
    print("Can't Divide.")
except NameError:
    print("Identifier Not Found.")
except ValueError:
    print("Value Error Happens.")
except:
    print("Error Happens.")