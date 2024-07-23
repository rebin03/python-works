numbers = [1,2,[3,(100,200,300),4],5,6]   #output >>> [1,2,[3,4,(100,150,200,300)],5,6]

n = numbers[2].pop()
numbers[2].insert(1,n)
num = list(numbers[2][2])
num.insert(1,150)

numbers[2][2] = tuple(num)

print(numbers)