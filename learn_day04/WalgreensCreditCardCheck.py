'''
1. Input Customer age
2. check age >= 15 - allow use of cc
3. Ask for Parent's consent letter
4. Store is canteen - allow usage
'''
age = input("Please Provide Customer Age:")
store = 'M&S'
if age.isnumeric():
    int_age = int(age)
    if int_age >= 15:
        print("Credit Card Allowed")
    elif store == 'Canteen':
        print("Credit Card Allowed in Canteen")
    else:
        print("Ask for Parent's consent letter")
else:
    print("Invalid Age Provided")