class Dept:
    def __init__(self, *args): 
        if len(args) == 1: 
            self.dept=args[0] 
 
        elif len(args) == 0: 
            self.dept="SCO" 
    
    def deptname(self):
        print(self.dept)
    
 
d1=Dept()
d1.deptname()
 
d2=Dept("CSE")
d2.deptname()