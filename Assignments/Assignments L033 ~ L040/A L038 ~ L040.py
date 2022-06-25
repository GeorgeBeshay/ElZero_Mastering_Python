# A L038 ~ L040 
# -------------



# A1
# ----

# name = input("Please Enter Your Name : ").strip().capitalize()

# print(f"Hello {name}, Happy To See You Here.")

# print("#" * 50 ) # SEPARATOR 



# A2
# ----

# age = int(input("Please Enter Your age : ").strip())

# if age < 16:
#     print("Hello Your age is Under 16, Some Articles Is Not Suitable For You.")
# else:
#     print(f"Hello Your Age is {age}, All Articles Is Suitable For You.")

# print("#" * 50 ) # SEPARATOR 



# A3
# ----

# first_name = input("Please Enter Your First Name : ").strip().capitalize()
# second_name = input("Please Enter Your Second Name : ").strip().capitalize()

# print(f"Hello {first_name} {second_name:.1}.")

# print("#" * 50 ) # SEPARATOR 



# A4 
# ----

email = input("Please Enter Your Email: ").strip().lower()

email_name = email[:email.index("@")].capitalize()
email_service = email[email.index("@")+1:email.index(".")]
email_domain = email[email.index(".")+1:]

print(f"Your Name Is {email_name}.")
print(f"Email Service Provider Is {email_service}.")
print(f"Top Level Domain Is {email_domain}.")

# print("#" * 50 ) # SEPARATOR 