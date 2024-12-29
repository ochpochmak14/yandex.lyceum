deposit = float(input())
profit = float(input())
years = float(input())
if int(years) == years:
    profit = profit / 100
    while years != 0:
        deposit = deposit * (1 + profit)
        years -= 1 
    print(deposit)
else:
    profit = profit / 100
    years1 = int(years)
    while years1 != 0:
        deposit = deposit * (1 + profit)
        years1 -= 1 
    perc = years - int(years)
    perc /= 100
    deposit = deposit * (1 + perc)
    print(deposit)