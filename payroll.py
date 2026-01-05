# PAYROLL APPLICATION

# Define Variables

employeeName = "Han Solo"
hoursWorked = 40
rateOfPay = 10.00
rateOfTax = 0.2
grossPay = 0
taxPaid = 0
nettPay = 0
bonus = 0

# Calculate Base Pay

grossPay = hoursWorked * rateOfPay
taxPaid = grossPay * rateOfTax
nettPay = grossPay - taxPaid

# Calculate Bonus

if hoursWorked >= 50:
    bonus = 100
elif hoursWorked >= 45:
    bonus = 60
elif hoursWorked >= 40:
    bonus = 50
else:
    bonus = 0

nettPay += bonus

# Display Payroll

print("++++++++++++++++++++++++")
print("Employee Payroll")
print("++++++++++++++++++++++++")
print("Employee: \t" + employeeName)
print("Hours Worked:  \t" + str(hoursWorked))
print("Rate of Pay: \t€" + str(rateOfPay))
print("Tax Rate: \t" + str(rateOfTax * 100) + "%")
print("Gross Pay: \t€" + str(grossPay))
print("Tax Paid: \t€" + str(taxPaid))
print("Bonus: \t\t€" + str(taxPaid))
print("Nett Pay: \t€" + str(nettPay))
print("++++++++++++++++++++++++")

