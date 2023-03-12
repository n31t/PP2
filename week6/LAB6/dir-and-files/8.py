import os
path = r'/Users/adilovamir/Desktop/PP2/week6/LAB6/dir-and-files/deleteME.txt'
path_bool = os.access(path, os.F_OK)
if path_bool == False:
    print('Path does not exist')
elif path_bool == True:
    os.remove(path)
    print("File has been removed")
