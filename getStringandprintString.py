# Define a class which has at least two methods: getString: to get a string from console input 
# printString: to print the string in upper case.

class InputOutString:
    def __init__(self):
        self.s=""
        
    def getString(self):
        self.s=input("Enter a string: ")
        
    def printString(self):
        print (self.s.upper())
        
obj=InputOutString
obj.getString()
obj.printString()