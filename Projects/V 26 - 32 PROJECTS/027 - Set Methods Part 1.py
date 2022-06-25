# -----------------
# -- Set Methods --
# -----------------

# clear()

a = {1,2,3}
a.clear()
print(a)

# union ()

b = {"One","Two","Three"}
c = {"1","2","3"}
x = {"Zero","Cool"}

print(b | c | x)
print(b.union(c,x))

# add()

d = {1,2,3,4}
d.add(5) # Only One Argument
d.add(6) 
print(d)

# copy()
e = {1,2,3,4}
f = e.copy()

print(e)
print(f)

e.add(6) # shallow copy

print(e)
print(f)

# remove()

g = {1,2,3,4}
g.remove(1)
# g.remove(7) # error 
print(g)

# discard()

h = {1,2,3,4}
h.discard(1)
h.discard(7) # no error 
print(h)

# pop()

i = {"A",True,1,2,3,4,5}
print(i.pop()) # Takes no Argument ..


# update()

j = {1,2,3}
k = {1,"A","B",2}
o = [1,2,3,4,5]
j.update(o) # msh lazm m3 set momkn list 3adyy 
j.update(["Html","CSS"])
j.update(k)

print(j) # unique items , so no repetition takes place
print(k)

# The End ........


