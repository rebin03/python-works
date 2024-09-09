class Person:
    
    def get_person(self, **kwargs):
        
        print(kwargs.get("name"))
        print(kwargs.get("work_place"))
        
        
p = Person()

p.get_person(name="Hari", work_place="TVM", native_place="Kakkanad")