# Lists are written with square brackets.
sampleList = [12,14, "apple", 78.99, True]
# Access Items: sampleList[1]
print(sampleList[0])
print(sampleList[1])
print(sampleList[1:4])

sampleBigList = [12,14, [15,16,17], 18, 19]

smallList = sampleBigList[2]
print(smallList)

sampleBigList.append(sampleList[1:4])
print(sampleBigList)
# Add Element: sampleList.append("newItem")
sampleList.append("newItem")
print(sampleList)
# Add Indexed Element: sampleList.insert(1, "fruits")
sampleList.insert(1, "fruits")
sampleList.append("fruits")
print(sampleList)
# Remove Element: sampleList.remove("item")

while "fruits" in sampleList:
    sampleList.remove("fruits")
    print(sampleList)

print("all fruits are removed")

#sampleList.remove("fruits")
print(sampleList)
sampleList.pop(0)
print(sampleList)
# Using Delete function: del sampleList[0]
# Check the Length: len(sampleList)
print(len(sampleList))
# Iterate: for eachItem in sampleList:
for eachItem in sampleList:
    print(eachItem)

# membership
if "fruits" in sampleList:
    sampleList.remove("fruits")
    print(sampleList)

sortList = [12,18,9,10,15,99]
sortList.sort()
print(sortList)

sampleList.clear()
print(sampleList)