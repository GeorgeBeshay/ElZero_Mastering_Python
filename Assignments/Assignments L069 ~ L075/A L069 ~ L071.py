# A L069 - L071
# --------------



# A1 
# ----

values = (0,1,2)
if any(values): # Any Element in iterator is true ?? Then [True] => Execute The Following Code:
    my_var = 0 
my_list = [True,1,1,["A","B"],10.5,my_var]
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]): # True or False or False == [True] => Execute The Following Code:
    print("Good")
else:
    print("Bad")
# ----------- OUTPUT & Explanation -----------
# L12 If any Element in iterator "values" is true (Not Equal 0) then executre the following code:
# L13   create variabla named "my_var" with value 0
# L15 If All Elements in Iterator "my_list" from index 0 to 4 are true, then execute the following code:
# L16   print("Good")
# THE OUTPUT IS "GOOD"

print("="*39) # Separator # ------------------------------------

# A2 
# ----

v = 40
my_range = list(range(v))
print(sum(my_range,v) + pow(v,v,v)) # 820

print("="*39) # Separator # ------------------------------------

# A3
# ----

n = 20 # Can be [20 , 21 ,22]
l = list(range(n))
if round(sum(l)/n) == max(0,3,10,2,-100,-23,9):
    print("Good")

print("="*39) # Separator # ------------------------------------

# A4
# ----

def my_all(myList):
    counter = 0
    for element in myList:
        if bool(element):
            counter += 1
        else:
            continue
    if counter == len(myList):
        return True
    else:
        return False

def my_any(myAwesomeList):
    counter = 0
    for element in myAwesomeList:
        if bool(element):
            counter += 1
        else:
            continue
    if counter > 0:
        return True
    else:
        return False

def my_min(myAmazingList):
    myAmazingList = list(myAmazingList)
    min = myAmazingList[0]
    for element in myAmazingList[1:]:
        if element < min: 
            min = element
        else:
            continue
    return min

def my_max(myWonderfulList):
    myWonderfulList = list(myWonderfulList)
    max = myWonderfulList[0]
    for element in myWonderfulList[1:]:
        if element > max: 
            max = element
        else:
            continue
    return max

print(my_all([1,2,3]))
print(my_all([1,2,3,0]))

print(my_any([0,1,[],False]))
print(my_any([(),0,False]))

print(my_min([10,100,-20,-100,50]))
print(my_min((10,100,-20,-100,50)))

print(my_max([10,100,-20,-100,50,700]))
print(my_max((10,100,-20,-100,50,700)))