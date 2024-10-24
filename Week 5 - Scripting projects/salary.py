firstYearPay = int(input("Enter your first year salary: "))
percentIncrease = float(input("Enter a yearly percentage increase: "))
yearLength = int(input("Enter the amount of years: "))
year = 1

while year <= yearLength:
    firstYearPay = firstYearPay * (percentIncrease * 0.01) + firstYearPay
    print("At the end of year", year, "your salary is:", round (firstYearPay, 2))

    if year < yearLength:
        year += 1
        continue
    elif year == yearLength:
        break

