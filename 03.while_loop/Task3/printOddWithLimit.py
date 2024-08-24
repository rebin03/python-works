start_limit = int(input("Enter the start limit: "))
end_limit = int(input("Enter the end limit: "))

while(start_limit<=end_limit):
    if start_limit%2 != 0:
        print(start_limit, end=" ")
    start_limit += 1