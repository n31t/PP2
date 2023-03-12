import os
path = input('Insert path \n')
path_bool = os.access(path, os.F_OK)
if path_bool == False:
    print("Path does not exist")
elif path_bool == True:
    print("Directories:", ', '.join([name for name in os.listdir(
        path) if os.path.isdir(os.path.join(path, name))]))
    print("Files:", ', '.join([name for name in os.listdir(
        path) if not os.path.isdir(os.path.join(path, name))]))
