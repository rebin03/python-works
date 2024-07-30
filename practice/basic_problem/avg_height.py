
heights = input("Enter the heights seperated by space: ").split(" ")

# length = len(heights)
total = 0
count = 0
for num in heights:
    
    total += float(num)
    count += 1
    
avg_count = total//count

print(round(avg_count))