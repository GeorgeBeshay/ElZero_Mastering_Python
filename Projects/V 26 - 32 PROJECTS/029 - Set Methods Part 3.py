# -----------------
# -- Set Methods --
# -----------------

# issuperset()

a = {1,2,3,4}
b = {1,2,3}
c = {1,2,3,4,5}

print(a.issuperset(b)) # True  # kol el fel b mwgood fel a
print(b.issuperset(a)) # False # kol el fel a msh mwgood fel b
print(a.issuperset(c)) # False # kol el fel c msh mwgood fel a

print("=" * 40) # Separator

# issubset() # 3ks el superset

d = {1,2,3,4}
e = {1,2,3}
f = {1,2,3,4,5}

print(d.issubset(e)) # False # kol el fel d msh mwgood fel e
print(d.issubset(f)) # True  # kol el fel d mwgood fel f

print("=" * 40) # Separator

# isdisjoint() # is there any common element ??

g = {1,2,3,4}
h = {1,2,3}
i = {10,11,12}

print(g.isdisjoint(h)) # False # feh common element
print(g.isdisjoint(i)) # True  # mafeesh ay common element

print("=" * 40) # Separator

# The End ..

