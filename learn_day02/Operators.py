# Mathematical + - / * % ** //
varOne = 9
varTwo = 2

print("Addition", (varOne+varTwo))
print("Subtraction", (varOne - varTwo))
print("Multiplication ", (varOne*varTwo))
print("Division", (varOne / varTwo))
print("Modulus (Reminder) ", (varOne % varTwo))
print("Rest to Power", (varOne ** varTwo))
print("Floor Division", (varOne // varTwo))

# Comparison Operators < <= > >= != ==
# Result of comparison operator is always boolean
print("Greater than ", (varOne > varTwo))
print("Greater than or equals ", (varOne >= varTwo))
print("Less than ", (varOne < varTwo))
print("Less than or equals ", (varOne <= varTwo))
print("Not Equals ", (varOne != varTwo))
print("Equals ", (varOne == varTwo))

# Logical Operators - and , or , not

'''
S1  S2  AND
T   T   T
T   F   F
F   T   F
F   F   F
'''

s1 = True
s2 = False

print("Result AND " , (s1 and s2))

'''
S1  S2  OR
T   T   T
T   F   T
F   T   T
F   F   F
'''

print("Result OR " , (s1 or s2))

'''
S1   NOT
T     F
F     T
'''

print(not s1)