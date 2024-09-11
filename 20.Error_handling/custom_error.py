def poll(age):
    
    if age < 18:
        
        raise Exception("Invalid age")
    
    else:
        
        print("Voted")
        
try:
    poll(18)
except Exception as e:
    print("Error:", e)