# take 2 numbers from input
# try all functions in mathematics - add, substract, divide, multiply

'''
1. Function can return to caller with return statement
2. You can return any number of outputs

'''

def add(varOne, varTwo):
    total = varOne + varTwo
    print("Total ", total)
    varOne += 1
    varTwo += 1
    return total, varTwo, varOne


def student_report(name, percentile=50.0):
    print("Student Name : {} with percentile : {} " .format(name, percentile))


student_report(98.66)

first = int(input("Enter First Number:"))
second = int(input("Enter First Number:"))

summation = add(first, second)
print("first : {} and second: {} ".format(first, second))
print("Value returned by Function ", summation)

