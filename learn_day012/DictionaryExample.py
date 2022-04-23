# Dictionaries are written in Curly Braces { "Key" : "value"}

sampleDictionary = {
    "model" : "Hybrid",
    "year" : 2022,
    "company" : "Toyota",
}

print(sampleDictionary)
sampleDictionary["color"] = "Grey"
sampleDictionary["company"] = "Lexus"
print(sampleDictionary)
print(sampleDictionary["year"])
print(sampleDictionary.get("year"))
sampleDictionary.pop("model")
print(sampleDictionary)
# Keys
for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary.get(eachKey))

# Key, value
for eachKey, eachValue in sampleDictionary.items():
    print(eachKey, eachValue)

# values
for eachValue in sampleDictionary.values():
    print(eachValue)

if "Toyota" in sampleDictionary.values():
    print("Present ")

# Remove Last Added Item: sampleDictionary.popitem()
sampleDictionary.popitem()
print(sampleDictionary)
# Remove Item with Key: sampleDictionary.pop("101")
sampleDictionary.pop("year")
print(sampleDictionary)