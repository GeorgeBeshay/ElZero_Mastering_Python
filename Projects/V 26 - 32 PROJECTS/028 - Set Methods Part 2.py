# -----------------
# -- Set Methods --
# -----------------

# difference() # bytl3lk el items el fe awl set we msh fe tany set 

a = {1,2,3,4}
b = {1,2,3,"Osama","Ahmed"}
print(a)
print(a.difference(b)) # or use -> a - b
print(a) # to see if there is update in it or not 

print( "=" * 40) # mn hna we ray7 da separator el programmers


# difference_update() 

c = {1,2,3,4}
d = {1,2,"Osama","Ahmed"}
print(c)
c.difference_update(d) # bya5od el difference we y3mlo howa el main set el gdeeda 
print(c)

print( "=" * 40) # separator

# intersection()

e = {1,2,3,4,"X","Osama"}
f = {"Osama","X",2}
print(e)
print(e.intersection(f)) # e & f
print(e) # to check for updates

print( "=" * 40) # separator

# intersection_update()

g = {1,2,3,4,"X","Osama"}
h = {"Osama","X",2}
print(g)
g.intersection_update(h) # g & h
print(g) # to check for updates # bya5od el intersection we y3mlha el main set el gdeeda ..

print( "=" * 40) # separator

# symmetric_difference() # print el msh mwgood fel 2

i = {1,2,3,4,5,"X"}
j = {"Osama","Zero",1,2,4,"X"}
print(i)
print(i.symmetric_difference(j)) # i ^ j
print(i)

print( "=" * 40) # separator

# symmetric_difference_update() # print el msh mwgood fel 2 + by5leh howa el main set el gdeeda 

k = {1,2,3,4,5,"X"}
l = {"Osama","Zero",1,2,4,"X"}
print(k)
k.symmetric_difference_update(l) # k ^ l
print(k)

print( "=" * 40) # separator

# The End ..




