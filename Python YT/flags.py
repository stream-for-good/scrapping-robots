class Flag:
    def __init__(self):
        self.number = 0
        self.string = "Flag"
    
    def toString(self):
        return self.string + " " + str(self.number)
    
    def plantFlag(self):
        print(self.string + " " + str(self.number))
        self.number += 1
        
