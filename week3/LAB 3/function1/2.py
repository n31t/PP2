"""Read in a Fahrenheit temperature. 
Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F – 32)"""


def Cels(f):
    C = (5/9) * (f - 32)
    return C


print(Cels(0))
