import os
import shutil

path = input("Enter name of directory to be sorted")
listOfFiles = os.listdir(path)
for i in listOfFiles:
    name,ext = os.path.splitext(i)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext) :
        shutil.move(path+'/'+ i , path + '/' + ext + '/' + i)

    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+ i , path + '/' + ext + '/' + i)