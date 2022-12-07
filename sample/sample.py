class Harshal(object):
    def __init__(self, x: str):
        self.x = x
        
    def print_x(self):
        print("hi")
        
    @classmethod
    def b(cls, x):
        print(x)
        
    @staticmethod
    def c(x):
        print(x + "2")
    
    
        
a = Harshal("hello")
a.print_x()
Harshal.b("dhruv")
a.c("1")
# a.b()
