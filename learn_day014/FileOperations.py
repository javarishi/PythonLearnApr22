import os

file_path = "/RISHI/H2K/FileIO/demofile_FWTest.abc"
if os.path.exists(file_path):
    os.remove("/RISHI/H2K/FileIO/demofile_FWTest.abc")

folder_path = "/RISHI/H2K/FileIO/Apr2022"
if not os.path.exists(folder_path):
    os.mkdir(folder_path) # make directory
    print("new folder created")
else:
    os.rmdir(folder_path)

dir_path = "C:\RISHI\H2K\FileIO"
list_of_file = os.listdir(dir_path)
csv_list = []
other_files = []
for eachFilename in list_of_file:
    if eachFilename.count(".csv") > 0:
        csv_list.append(eachFilename)
        print(eachFilename)
    else:
        other_files.append(eachFilename)

print("file removed")