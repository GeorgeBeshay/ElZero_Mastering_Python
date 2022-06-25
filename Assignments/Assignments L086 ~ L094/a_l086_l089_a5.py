'''
This Is A Module Docstring
'''
myFriends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_people) -> list:
    '''
    This Function Is Made To Say Hello To Each Person In a Given List
    '''
    for someone in some_people:
        print(f"Hello {someone}")

say_hello(myFriends)
