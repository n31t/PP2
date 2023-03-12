from string import ascii_uppercase
for char in ascii_uppercase:
    file = open(
        rf'/Users/adilovamir/Desktop/PP2/week6/LAB6/dir-and-files/{char}.txt', 'x')
    file.close()
