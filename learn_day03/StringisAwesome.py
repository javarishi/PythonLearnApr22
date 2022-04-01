hello = 'Hello, World,!'
say_hello = "     Add space    "
print(hello[0])
print(hello[3:10]) # 3 to 9 Start:End - print start to (end-1)
print(hello[:5]) # Start till 5
print(hello[5:]) # 5 to End

# H. W (Research) - Write a Single line code to reverse a String

print("Without Strip ", say_hello)
print("Strip ", say_hello.strip())
print(len(hello))
print("lower ", hello.lower())
print("upper ", hello.upper())
print("title ", hello.title())
print("capitalize ", hello.capitalize())

print("replace", hello.replace('o', '0'))
first = hello.find(',')
second = hello.find(',',first+1)
print(first, second)
print("find", hello.find(',')) # index of given character
print("count", hello.count(',')) # How many number of characters

age = "55.45"
name = "Nei1"
print(age.isnumeric())
print(age.isdigit())
print(age.isdecimal())
