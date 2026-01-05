# PAYROLL APPLICATION

# Define variables
employeeName = "Han Solo"
hoursWorked = 40
rateOfPay = 10.00
rateOfTax = 0.2
grossPay = 0
taxPaid = 0
nettPay = 0

# Calculations
grossPay = hoursWorked * rateOfPay
taxPaid = grossPay * rateOfTax
nettPay = grossPay - taxPaid

# Display Payroll
print("+++++++++++++++++++")
print("Employee Payroll")
print("+++++++++++++++++++")
print("Employee: " + employeeName)
print("Hours Worked:  " + str(hoursWorked))
print("Rate of Pay: €" + str(rateOfPay))
print("Tax Rate: " + str(rateOfTax * 100) + "%")
print("Gross Pay: €" + str(grossPay))
print("Tax Paid: €" + str(taxPaid))
print("Nett Pay: €" + str(nettPay))
print("+++++++++++++++++++")

