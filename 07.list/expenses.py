expenses = [10000,11000,13000,14000,15000,17000,19000,20000]

expenses_count = len(expenses)

# for i in range(0,expenses_count):
#     print(expenses[i])

total_expense = 0

for i in range(0,expenses_count):
    
    if expenses[i]>15000:
        print(expenses[i])
        
    total_expense = total_expense + expenses[i]

avg_expense = total_expense/expenses_count

print(f"Total expense = {total_expense}")
print(f"Average expense = {avg_expense}")