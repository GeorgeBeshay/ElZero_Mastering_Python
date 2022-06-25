# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python Is Object Even Functions 
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function as Parameter)
# ------------------------------------------------------------------------------

def myDecorator(func): # Decorator
    def nestedfunc(): # Any Name Its Just For Decoration
        print("Before") # Message From Decorator 
        func() # Execute Function 
        print("After") # Message From Decorator 
    return nestedfunc

@myDecorator
def sayHello():
    print("Hello From Say Hello Function")

@myDecorator
def sayHowAreYou():
    print("Hello From Say How Are You Function")

# afterDecoration = myDecorator(sayHello)
# afterDecoration()

sayHello()
print("#"*50)
sayHowAreYou()