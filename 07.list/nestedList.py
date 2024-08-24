numbers = [1,2,[3,[100,200,300],4],5,6]

print(numbers[2])
print(numbers[2][1])

numbers[2][1].append(500)
numbers[2][1].insert(3,400)
print(numbers)