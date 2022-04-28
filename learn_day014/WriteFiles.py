file_name = "/RISHI/H2K/FileIO/demofile_FWTest.abc"
file = None
try:
    file = open(file_name, 'a')
    file.write("This is another Line added 1 \n")
    file.write("This is another Line added 2 \n")
except Exception as ex:
    print("Some Error with File ", type(ex), ex)
finally:
    print("Closing the File")
    file.close()