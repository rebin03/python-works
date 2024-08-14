def is_eligible_for_voting(age):
    
    if age >= 18:
        print("Ypu are eligible for voting")
    else:
        print("You are not eligible for voting")
        
age = int(input("Enter your age: "))
is_eligible_for_voting(age)