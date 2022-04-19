def say_hello(text_to_print):
    return str(text_to_print).upper()


def shout(another_function, text):
    return another_function(text)


def calculator(action, number):
    function_name = None

    def double():
        return number + number

    def square():
        return number*number

    def cube():
        return number*number*number

    if action == "double":
        function_name = double
    elif action == "square":
        function_name = square
    else:
        function_name = cube

    return function_name


varText = "This is getting complex"
final_op = shout(say_hello, varText)
print(final_op)

db = calculator("double", 5)
sqr = calculator("square", 5)
cb = calculator("cube", 5)
print(db())
print(sqr())
print(cb())