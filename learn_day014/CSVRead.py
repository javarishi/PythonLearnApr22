import csv

file = open("/RISHI/H2K/FileIO/CSVTest.csv")
#store it I	n a variable
data = csv.reader(file)
#parse each row and print the result
for each_row in data:
    print(each_row[0])
file.close()