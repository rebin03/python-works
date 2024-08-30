#  magic/dunder methoda are builtin nethods which call implicitly


class Author:
    
    def __init__(self, name, book_name, pages):
        self.name = name
        self.book_name = book_name
        self.pages = pages
        
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    
    # This will called automaticaly when we calling the instance of this class
    def __call__(self, *args, **kwds):
        print("Calling object")
    
    # this will called automaticaly when object of this class is deleted
    def __del__(self):
        print("Author object has been deleted")
    
    
obj = Author("Kevin", "Python basic to Advance", 300)
print(len(obj))
print(obj)

# we can also call an object instance but need to define it's dunder method in the object class
obj()

# we can also delete an object instance using del keyword.
del obj
print(obj)