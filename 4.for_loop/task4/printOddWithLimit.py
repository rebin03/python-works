start_limit = int(input("Enter start limit: "))
end_limit = int(input("Enter start limit: "))

for i in range(start_limit, end_limit+1):
    if i % 2 != 0:
        print(i)