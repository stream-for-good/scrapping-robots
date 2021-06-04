class Lever:
    def __init__(self):
        self.lever = [0]
    
    def incr(self):
        self.lever[0] += 1
    
    def decr(self):
        self.lever[0] -= 1
    
    def get(self):
        return self.lever[0]
    
    def setLever(self, n):
        self.lever = [n]
