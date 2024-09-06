class Parent1:
    
    def m1(self):
        print("m1 from parent 1")
        
class Parent2:
    
    def m2(self):
        print("m2 from parent 2")
        
class Child(Parent1, Parent2):
    
    def m3(self):
        print("m3 from child")


child = Child()

child.m1()
child.m2()
child.m3()