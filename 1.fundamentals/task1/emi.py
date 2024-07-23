# Program to calculate monthly emi

# inputs: loan_amount, tenure, interest_rate

# EMI = loan_amount * interest_rate * (1 + interest_rate)^tenure / ((1 + interest_rate)^tenure - 1)

loan_amount = int(input("Enter loan amount: "))
interest_rate = int(input("Enter interest rate: "))
tenure = int(input("Enter tenure: "))

monthly_interest_rate = interest_rate/100/12
tenure_in_months = tenure*12

EMI = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**tenure_in_months / ((1 + monthly_interest_rate)**tenure_in_months - 1)

total_payable_amount = EMI * tenure_in_months
total_interest_payable = total_payable_amount - loan_amount

print(f"Loan amount: {loan_amount}\nInterest rate: {interest_rate}\nTenure: {tenure}\nMonthly EMI = {EMI}\nTotal payable amount = {total_payable_amount}\nTotal interest payable = {total_interest_payable}")