# A L081 - L085 
# -------------



# A1
# ---

def reverse_string(my_string):
    yield my_string[::-1]
for letter in reverse_string("Elzero"):
    print(letter)

print("$" * 50)

# A2
# ---

def decorator(func):
    def sugar_adder():
        print("Sugar Added From Decorators")
        func()
        print("####################")
    return sugar_adder

@decorator
def make_tea():
    print("Tea Created")
@decorator
def make_coffee():
    print("Coffee Created")

make_tea()
make_coffee()