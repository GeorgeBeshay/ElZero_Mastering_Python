# ------------------------
# -- Built In Functions --
# ------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------

# abs()
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#"*39) # Separator

# pow(base,exp,mod) => Power
print(pow(2,5)) # 2*2*2*2*2
print(pow(2,5,10)) # (2*2*2*2*2)%10 = 2

print("#"*39) # Separator

# min(item,item,item,item OR Iterator)
myNumbers = (1,20,-50,-100,100)
print(min(1,10,-50,20,30))
print(min("X","Z","Osama"))
print(min(myNumbers))

print("#"*39) # Separator

# max(item,item,item,item OR Iterator)
myNumbers = (1,20,-50,-100,100)
print(max(1,10,-50,20,30))
print(max("X","Z","Osama"))
print(max(myNumbers))

print("#"*39) # Separator

# slice(start,end,step)
a = ["A","B","C","D","E","F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2,5)])

print("#"*39) # Separator