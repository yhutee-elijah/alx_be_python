monthly_income = int(input("Enter your monthly income:"))
monthly_expense = int(input("Enter your total monthly expense:"))
monthly_savings = monthly_income - monthly_expense
simple_interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("your monthly_savings are $",monthly_savings)
print ("projected_savings after one year, with interest is: $",projected_savings)
