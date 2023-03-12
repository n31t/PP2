with open('/Users/adilovamir/Desktop/PP2/week6/LAB6/dir-and-files/dfile.txt', 'r') as file1, open('/Users/adilovamir/Desktop/PP2/week6/LAB6/dir-and-files/dfile2.txt', 'a') as file2:
    for line in file1:
        file2.write(line)
