purchasePrice = float(input("Enter the purchase price: "))
downPayment = 0.10 * purchasePrice
interestRate = 0.12
balance = purchasePrice - downPayment
monthlyPayment = 0.05 * purchasePrice


month = 0


print("MONTH | BALANCE OWED | INTEREST OWED | PRINCIPAL | MONTHLY PAYMENT | REMAINING BAL")
print("==================================================================================")
while balance > 0:
    interestMonthly = balance * (interestRate / 12)
    principal = monthlyPayment - interestMonthly
    remainingBalance = balance - principal
    month += 1
    print(month, "     ", balance, "       ", round(interestMonthly, 2), "        ", principal, "        ", monthlyPayment, "       ", remainingBalance)
    print("")
    if month < 12:
        continue
    elif month == 12:
        break

    




