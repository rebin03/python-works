class GrandParent:
    
    def m1(self):
        print("m1 method from grand parent")
        

class Parent(GrandParent):
    
    def m2(self):
        print("m2 method from parent")
        

class Child(Parent):
    
    def m3(self):
        print("m3 method from child")
        

child = Child()

child.m3()
child.m2()
child.m1()