class StringInOutClass:
    def __init__(self):
        self.innerString = ""
    def getString(self):
        self.innerString = input()
    def printString(self):
        print(self.innerString.upper())

obj = StringInOutClass()
obj.getString()
obj.printString()

obj2 = StringInOutClass()
obj2.getString()
obj2.printString()