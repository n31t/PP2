class Upper:
    s = ""

    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = str(input())

    def printString(self):
        print(self.s.upper())


'''a = Upper()
a.getString()
a.printString()'''
