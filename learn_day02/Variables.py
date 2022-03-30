age = 15
Age = 16
AGE = 17
print(age, Age, AGE)
percentage = 99.14
name = "Neil Armstrong"
complex_number = 1 + 5j
hasStudentJoinedTheClass = True

'''
_ as word separator - customer_name - variable declaration
camelCase  - customerFirstName - method declaration this is preferred 
- Variables cannot be started with number
- special characters are not allowed - only _ is allowed
- 256 characters in variable name 
- case sensitive
'''

age15 = 15
age15customer = 15
age_20 = 20
_ = 20

print('Age', age, id(age), type(age))
print("Percentage", percentage, id(percentage), type(percentage))
print("Name", name, id(name), type(name))
print("complex_number", complex_number, id(complex_number), type(complex_number))

varOne = 100
varTwo = 100
varThree = 100

print(id(varOne), id(varTwo), id(varThree))

varOne = 101

print(id(varOne), id(varTwo), id(varThree))