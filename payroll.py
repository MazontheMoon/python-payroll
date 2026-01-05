# PAYROLL APPLICATION

# Define Variables

numberOfEmployees = 5
counter = 0;
employeeName = ""
hoursWorked = 0
rateOfPay = 0.0
rateOfTax = 0.0
grossPay = 0
taxPaid = 0
nettPay = 0
bonus = 0

# Display Greeting
print("+++++++++++++++++++++++++++++++")
print("\tEmployee Payroll")
print("+++++++++++++++++++++++++++++++\n")

# Loop through all employees
while(counter < numberOfEmployees):

    # Get User Input

    employeeName = input("Enter Employee Name: ")
    hoursWorked = int(input("Enter Number of Hours Worked: "))
    rateOfPay = float(input("Enter Rate of Pay: €"))
    rateOfTax = float(input("Enter Rate of Tax(%): ")) / 100

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

    print("\n+++++++++++++++++++++++++++++++")
    print("Employee: \t" + employeeName)
    print("Hours Worked:  \t" + str(hoursWorked))
    print("Rate of Pay: \t€" + str(rateOfPay))
    print("Tax Rate: \t" + str(rateOfTax * 100) + "%")
    print("Gross Pay: \t€" + str(grossPay))
    print("Tax Paid: \t€" + str(taxPaid))
    print("Bonus: \t\t€" + str(bonus))
    print("Nett Pay: \t€" + str(nettPay))
    print("+++++++++++++++++++++++++++++++\n")

    #Increment counter
    
    counter += 1

