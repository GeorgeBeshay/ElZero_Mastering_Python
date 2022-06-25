# L026 ~ L032
# --------------

# A1

my_list = [1,2,3,3,4,5,1]
unique_list = set(my_list)
unique_list = list(unique_list)

print(unique_list)
print(type(unique_list))
unique_list.remove(unique_list[-1]) # Dynamic
print(unique_list)

print("=" * 50)

# ---------------

# A2

nums = {1,2,3}
letters = {"A","B","C"}

print(nums.union(letters)) # 1st   # OR => print(nums | letters)
print(set(list(nums)+list(letters))) # 2nd
nums.update(letters) # 3rd
print(nums)

print("=" * 50)

# ----------------

# A3

my_set = {1,2,3}
letters = {"A","B","C"}

print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C") # No Error 
# my_set.remove("C") # Error 

print("=" * 50)

# A4 

set_one = {1,2,3}
set_two = {1,2,3,4,5,6}
print(set_two.issuperset(set_one))
# OR 
print(set_one.issubset(set_two))

print("=" * 50)

# A5

dictionary_one = {
    "HTML":"90%",
    "CSS":"80%",
    "Python":"30%",
}

print("HTML" + " Progress Is " + dictionary_one["HTML"])
print("CSS" + " Progress Is " + dictionary_one["CSS"])
print("Python" + " Progress Is " + dictionary_one["Python"])

dictionary_one.update({"AI":"20%"})
# print(dictionary_one) 
print("AI" + " Progress Is " + dictionary_one["AI"])

print("=" * 50)