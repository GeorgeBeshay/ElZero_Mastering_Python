# --------------------
# -- Function Scope --
# --------------------

# x = 1 # Global Scope 

def one(): # What Happen In Vegas, Stay In Vegas ;)
    global x
    x = 2
    print(f"Print Variable From Function Scope {x}")

def two():
    x = 10
    print(f"Print Variable From Function Scope {x}")

one()
print(f"Print Variable From Global Scope {x}")
two()
print(f"Print Variable From Global Scope After Activating Function One Is Called {x}")