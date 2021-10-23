import os
import shutil
import time

path = input("Enter path: ")
days = 30
seconds = time.time() - (days * 24 * 60 * 60)
path = path + "/"

loF = os.listdir(path)

def file_time(path):
	ctime = os.stat(path).st_ctime
	return ctime


if os.path.exists(path):
    for file in loF:
        if seconds >= file_time(path):
            os.remove(path + file)
            print("Files have been deleted.")

        else:
            print("File was created less than 30 days ago.")
else:
    print("Path does not exist.")