# Method overriding is overriding of methods defined in the base class with derived class's definition.
# Method ovveriding occured between a base class and derived class.(ie, it'll occure in inheritance)
# It is run time polymorphism. it will decide the method only at the run time with help of MRO and decide wich function to be called
# in this method must have same method name and same number of parameter also.

class Father:
    
    def sleep(self):
        print("Sleeps from 10:00 PM to 5:00 AM")
        
    def eat(self):
        print("Eating..")

class Son(Father):
    
    # This method will override the existing method in the base class when calling with derived class object.
    def sleep(self):
        print("Sleeps from 2:00 AM to 10:00 AM")
        super().sleep() # calls the parent class sleep method

ram = Son()
ram.sleep()