# PAYROLL APPLICATION

# Define Variables
numberOfEmployees = 5
counter = 0;
payrollList = []
employeeName = ""
hoursWorked = 0
rateOfPay = 0.0
rateOfTax = 0.0
grossPay = 0
taxPaid = 0
nettPay = 0
bonus = 0
    
# Display Greeting
def displayWelcome():
    print("++++++++++++++++++++++++++++++++++++")
    print("Welcome to Employee Payroll")
    print("++++++++++++++++++++++++++++++++++++\n")

# Get User Input
def getInput():
    employeeName = input("Enter Employee Name: ")
    hoursWorked = int(input("Enter Number of Hours Worked: "))
    rateOfPay = float(input("Enter Rate of Pay: €"))
    rateOfTax = float(input("Enter Rate of Tax(%): ")) / 100
    inputList = []
    inputList.append(employeeName)
    inputList.append(hoursWorked)
    inputList.append(rateOfPay)
    inputList.append(rateOfTax)
    return inputList
    
# Calculate Gross Pay
def calcGross(hoursWorked, rateOfPay):
    return hoursWorked * rateOfPay

# Calculate Tax Paid
def calcTax(grossPay, rateOfTax):
    return grossPay * rateOfTax

# Calculate Nett Pay
def calcNett(grossPay, taxPaid):
    return grossPay - taxPaid

# Calculate Bonus
def calcBonus(hoursWorked):
    if hoursWorked >= 50:
        return 100.00
    elif hoursWorked >= 45:
        return 60.00
    elif hoursWorked >= 40:
        return 50.00
    else:
        return 0.0

# Caluclate Pay
def calcPay(payrollList):
    grossPay = calcGross(payrollList[1], payrollList[2])
    taxPaid = calcTax(grossPay, payrollList[3])
    nettPay = calcNett(grossPay, taxPaid)
    bonus =  calcBonus(payrollList[1])
    nettPay += bonus
    payrollList.append(grossPay)
    payrollList.append(taxPaid)
    payrollList.append(bonus)
    payrollList.append(nettPay)
    return payrollList

# Display Payroll
def displayPayroll(payrollList):
    print("\n+++++++++++++++++++++++++++++++")
    print("Employee: \t" + payrollList[0])
    print("Hours Worked:  \t" + str(payrollList[1]))
    print("Rate of Pay: \t€" + str(payrollList[2]))
    print("Tax Rate: \t" + str(payrollList[3] * 100) + "%")
    print("Gross Pay: \t€" + str(payrollList[4]))
    print("Tax Paid: \t€" + str(payrollList[5]))
    print("Bonus: \t\t€" + str(payrollList[6]))
    print("Nett Pay: \t€" + str(payrollList[7]))
    print("+++++++++++++++++++++++++++++++\n")

# Display Exit Message
def displayExit():
    print("++++++++++++++++++++++++++++++++++++")
    print("Thank you for using Employee Payroll")
    print("++++++++++++++++++++++++++++++++++++\n")

# Main
displayWelcome()

# Loop through all employees
while(counter < numberOfEmployees):

    #Prompt for input
    payrollList += getInput()

    #Calculate wages
    payrollList += calcPay(payrollList)

    # Display payroll
    displayPayroll(payrollList)

    #Clear payroll list
    payrollList.clear()

    # Increment counter
    counter += 1
#End Of loop    

displayExit()
