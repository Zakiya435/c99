import os
import shutil

source = input("enter source of folder")
destination = input("enter destination of folder")

source=source+'/'
destination=destination+'/'

listOfFiles = os.listdir(source)
for i in listOfFiles:
    shutil.copy((source+i),destination)
