monthly_income = int(input("enter your monthly income"))
monthly_expense = int(input("enter your monthly expense"))
monthly_savings = monthly_income - monthly_expense
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.5))

print ("your monthly_savings are $",monthly_savings)
print ("projected_savings after one year, with interest is: $",projected_savings)