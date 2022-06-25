# A L056 - L059
# --------------




# A1
# ----

# print("Note: While Using The Calculation Function You Can Enter The First Letter Only From The Operation.")
# def calculate(N1,N2,operation="add"):
#     operation = operation.strip().lower().capitalize()
#     if type(N1) != int or type(N2) != int:
#         print("Error, Please Enter Integers Only")
#     else:
#         ops = ["Add","Subtract","Multiply","A","S","M"]
#         if operation in ops:
#             if operation == "Multiply" or operation == "M":
#                 return N1*N2
#             elif operation == "Subtract" or operation == "S":
#                 return N1-N2
#             else:
#                 return N1+N2
#         else:
#             return "Wrong Operation Has Been Entered, Please Try Again Later."
# print(calculate(10,20)) #30
# print(calculate(10,20,"AdD")) #30
# print(calculate(10,20,"a")) #30
# print(calculate(10,20,"A")) #30

# print(calculate(10,20,"S")) #-10
# print(calculate(10,20,"subTRACT")) #-10

# print(calculate(10,20,"Multiply")) #200
# print(calculate(10,20,"m")) #200




# A2
# ----

# def addition(*numbers):
#     numbers = list(numbers)
#     sum = 0 
#     for number in numbers:
#         if number == 10:
#             continue
#         if number == 5:
#             sum -= number
#         else:
#             sum += number
#     return sum 

# print(addition(10,20,30,10,15))
# print(addition(10,20,30,10,15,5,100))



# A3
# ----

# def show_skills(name,*skills):
#     if len(skills) > 0:
#         print(f"Hello {name} Your Skills Are:")
#         for skill in skills:
#             print(f"- {skill}")
#     else:
#         print(f"Hello {name} You Have No Skills To Show.")

# show_skills("George","HTML","CSS","JS","Python")




# A4
# ----

# def say_hello(name = "Unknown",age = "Unknown",country = "Unknown"):
#     return f"Hello {name} Your Age Is {age} And You Live In {country}."

# print(say_hello("George",19,"Egypt"))
# print(say_hello())