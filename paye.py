#input income
income = float(input("Enter your income: "))

totaltax = list()
# if income is less than or equal to 365 then tax is 0
if income <= 365:
    totaltax.append(0)
#if income is greater than 365 but less than or euqal to 365 +  110, tax us 5% of income - 365
if income > 365:
    totaltax.append((income - 365) * 0.05)
#if income is greater than 365 + 110 but less than or equal to 365 + 110 + 130 tax is 10% of income - (365 + 110)
if income > 365 + 110:
    totaltax.append((income - (365 + 110)) * 0.1)
#if income is greater than 365 + 110 + 130 but less than or equal to 365 + 110 + 130 + 3000 tax is 17.5% of income - (365 + 110 + 130)
if income > 365 + 110 + 130:
    totaltax.append((income - (365 + 110 + 130)) * 0.175)


print("Your tax is: ", totaltax)