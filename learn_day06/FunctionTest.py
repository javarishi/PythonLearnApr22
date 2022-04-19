'''
def function_name(optional:parameters):
    reusable function block
    optional : return output
'''

def say_hello(name="Guest", greet="Hello"):
    print(greet, name)


say_hello("David", "Howdy")
say_hello()
say_hello("Venkat", "Namaste")

print(type(say_hello))

# s2 = s1
hello = say_hello
hello()
# take 2 numbers from input
# try all functions in mathematics - add, substract, divide, multiply