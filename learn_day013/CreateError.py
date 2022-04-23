'''
1. finally runs everytime
2. any number of except blocks
3. consolidation of errors in except block with alias
4. Specific First , generic later (Child first , parent later)
'''

age = input("Enter Your Age:")
list_age = [12, 13]
try:
    if age > 15:
        print("Valid age for Sports selection")
    calc = 100/age
   # list_age.remove(calc)
except (TypeError, ZeroDivisionError) as err:
    print("There may be some problem ", err, type(err))
except Exception as err:
    print("There may be some Exception ", err, type(err))
else:
    print("This will execute only if try block completes without error")
finally:
    print("This code always execute")

print("Line after condition")