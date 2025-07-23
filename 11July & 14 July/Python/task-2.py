salary = float(input("Enter your salary : "))

ta = 0.10 * salary
da = 0.05 * salary

grossSalary = salary + ta + da

print("Basic salary :" , salary)
print("TA :" , ta)
print("DA :" , da)
print("Gross Salary :", grossSalary)

tax = grossSalary * 0.1
netSalary = grossSalary - tax

print("Tax :", tax)
print("Net Salary :", netSalary)
