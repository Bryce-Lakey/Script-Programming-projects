hourlyWage = float(input("Enter your hourly wage: "))
hours = int(input("Enter the amount of hours you worked this week: "))
OThours = int(input("Enter any overtime hours you worked this week: "))

OTwage = 1.5 * hourlyWage
OTpay = OThours * (1.5 * hourlyWage)
weeklyPay = hourlyWage * hours + OTpay
print("Your pay for this week is: ", weeklyPay)

