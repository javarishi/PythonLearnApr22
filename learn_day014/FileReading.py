file_name = "/RISHI/H2K/FileIO/CSVFilesteachers.csv"
file = None
try:
    file = open(file_name, "rt")
    for eachLine in file:
        if eachLine.count("Yrs of Exp") > 0:
            continue
        if len(eachLine.strip()) > 0:
            record = eachLine.split(',')
            print(record, type(record))
            name = record[0]
            skill = record[1]
            yrsOfExp = record[2]
            print(name, skill, yrsOfExp)
except FileNotFoundError as ex:
    print("File May Not Exists ", type(ex), ex)
finally:
    print("Closing the File")
    file.close()
