
def add_three(n1, n2, n3):
    return n1+n2+n3


num1, num2, num3 = map(int, input("Enter 3 numbers(seperated by space): ").split())

res = add_three(num1, num2, num3)
print(res)