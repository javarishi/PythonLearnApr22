# Sets are written with curly brackets
sampleSet = {12,13,14,15}
# Add Element: sampleSet.add("mango")
print(sampleSet)
sampleSet.add(16)
sampleSet.add(16)
sampleSet.add(16)
print(sampleSet)
# Remove Element: sampleSet.remove("banana")
sampleSet.remove(16)
print(sampleSet)
sampleSet.discard(17)
print(sampleSet)
# Iterate: for eachItem in sampleSet:

# Element Exists? : if "apple" in sampleSet:

# Add another set: sampleSet.update(anotherSet)

anotherSet = {1,2,3,4,5,6}
sampleSet.update(anotherSet)
print(sampleSet)

