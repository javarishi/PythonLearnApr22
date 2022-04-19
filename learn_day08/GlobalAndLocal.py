greet = "hello"

def say_hello():
    global greet
    greet = "Howdy"
    print(greet)


say_hello()
print(greet)