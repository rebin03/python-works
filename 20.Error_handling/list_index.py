lst = [1, 2, 3, 4, 5, 6]

index = int(input("Enter index value: "))


try:
    print(lst[index])
    
except Exception as e:
    
    print("Error:", e)
    
print("Database commit")
print("File transfer")