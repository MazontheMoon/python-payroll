# PAYROLL APPLICATION

# Define Variables

employeeName = ""
hoursWorked = 0
rateOfPay = 0.0
rateOfTax = 0.0
grossPay = 0
taxPaid = 0
nettPay = 0
bonus = 0

# Get User Input

employeeName = input("Enter employee name: ")
hoursWorked = int(input("Enter number of hours worked: "))
rateOfPay = float(input("Enter rate of pay: €"))
rateOfTax = float(input("Enter rate of tax (0.1 for 10%, 0.2 for 20%, etc.: "))

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
