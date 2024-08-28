def is_eligible_to_vote(age):
    
    if age >= 18 and age <= 120:
        return True
    else:
        return False


age = int(input("Enter your age: "))

print("Eligible to vote" if is_eligible_to_vote(age) else "Not Eligible to vote")