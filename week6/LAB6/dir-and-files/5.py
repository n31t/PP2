list = ['no', 'way', 'it\'s working']
with open(r"/Users/adilovamir/Desktop/PP2/week6/LAB6/dir-and-files/dfile.txt", 'w') as file:
    for i in list:
        file.write(i+'\n')
