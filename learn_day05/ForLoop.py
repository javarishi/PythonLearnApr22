# in Python this loop is also called as for-each loop



'''
for eachItem in data_structure:
    block of code to be executed for eachItem
'''
marks = [90, 91, 95, 88, 98, 93]
total = 0
for eachSubjectMarks in marks:
    total = total + eachSubjectMarks
    print(eachSubjectMarks)

print("Total", total)