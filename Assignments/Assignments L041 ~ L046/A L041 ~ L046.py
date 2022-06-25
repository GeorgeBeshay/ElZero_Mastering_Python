# A L041 ~ L046 
# -----------------




# A1
# ----

# operationList = ["+","-","*","/","%"]
# num1 = int(input("Please Enter The First Number: ").strip())
# num2 = int(input("Please Enter The Second Number: ").strip())
# operation = input("Please Choose The Type Of The Operation (+,-,*,/,%)").strip()
# if operation in operationList:
#     print("*" * 50)
#     print(f"{num1:,} {operation} {num2:,} =")
#     if operation == "+":
#         print(num1 + num2)
#     elif operation == "-":
#         print(num1 - num2)
#     elif operation == "*":
#         print(num1 * num2)
#     elif operation == "/":
#         print(num1 / num2)
#     else:
#         print(num1 % num2)
#     print("*" * 50)
# else:
#     print("Wrong Operation Was Chosen, Please Try Again Later.")




# A2
# ----

# age = 15
# print("App Is Suitable For You.") if age > 16 else print("App Is Not Suitable For You.")




# A3
# ----

# age = int(input("Please Enter Your Age In Numbers: ").strip())
# if 100 > age > 10:
#     months = age * 12
#     weeks = months * 4
#     days = age * 365
#     hours = days * 24
#     minutes = hours * 60
#     seconds = minutes * 60
#     print(f"Your Age In Months Is {months}.\n\
# Your Age in Weeks Is {weeks}.\n\
# Your Age in Days Is {days}.\n\
# Your Age in Hours Is {hours}.\n\
# Your Age in Minutes Is {minutes}.\n\
# Your Age in Seconds Is {seconds}.")
# else:
#     print("Sorry The Age is Out Of Range.")




# A4 
# ----

countries = ["Egypt","Palestine","Syria","Yemen","KSA","USA","Bahrain","England"]
price = 100
discount = 30
country = input("Please Enter Your Country : ").strip().capitalize()
if country in countries:
    print(f"Your Country Is Eligible For Discount And The Price After Discount Is ${price-discount}.")
else:
    print(f"Your Country Is Not Eligible For Discount And The Price Is ${price}.")