year = int(input('Enter a year: '))
salary = float(input('Enter the salary: '))
if year > 5:
    bonus = salary*0.05
    a = bonus+salary
    print("salary",a)
else:
    print("salary",salary)