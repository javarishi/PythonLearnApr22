one = int(input("First Number :"))
two = int(input("Second Number :"))
three = int(input("Third Number :"))

'''
1. one > two and one > three --> one is greatest
2. two > three --> two is greatest
3. three is greatest

H.W. How to handle equality condition in below code
'''

if (one > two) and (one > three):
    print("Greatest number :", one)
elif two > three:
    print("Greatest number :", two)
else:
    print("Greatest number :", three)