# ------
# Strings Indexing And Slicing 
# ------


# Indexing ( Access Single Item )
myString = 'I Love Python'
print(myString[0])
print(myString[2])
print(myString[9])
print(myString[-2])

# Slicing   (Access Sequence Multiple Items)
# [Start:End] note that end is not included
# [Start:End:Steps]
print(myString[8:11]) #yth
print(myString[3:5]) #ov
print(myString[:10]) # if start is not mentioned, then start from zero
print(myString[5:]) # if end is not mentioned, then print till the end
print(myString[:]) # full data will be printed

print(myString[0::1]) # Full Data
print(myString[::1]) # Full Data
print(myString[::2])
print(myString[::3])