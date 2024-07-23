# global Keyword

# if you want to modify a global variable within the local scope then you need to use global keyword to access the global variable

a = 10 #global

def display1():
  # a = a + 1 # this will show error
    print(a)
    
display1()

def display2():
    global a  # by using the global keyword we can access the 'a' and modify it.
    a = a + 1
    print(a)
    
display2()

# we can also create a global varaible within the local scope

def display():
    a = 20
    def show():
        global a # This 'a' is now available globaly 
        a = 30
    show()
    print("value after calling show:",a) # if the varable is available within the local scope then that will be used
    
display()
print(a)