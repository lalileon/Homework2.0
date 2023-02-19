try:
    salary = float(input("What is your gross salary?"))
    if salary < 0:
        print("The number cannot be negative.")
        exit()
    number_children = int(input("How many children do you have?"))
    if number_children < 0:
        print("Why did you kill a child?")
        exit()

except ValueError:
    print("The input has to be a number")
    exit()
if salary < 1000:
    net_salary = (0.9 + (number_children * 0.01)) * salary
    print("You net salary is", round(net_salary), "euros.")
elif 1000 <= salary < 2000:
    net_salary = (0.88 + (number_children * 0.01)) * salary
    print("You net salary is", round(net_salary), "euros.")
elif 2000 <= salary < 4000:
    net_salary = (0.86 + (number_children * 0.005)) * salary
    print("You net salary is", round(net_salary), "euros.")
else:
    net_salary = (0.82 + (number_children * 0.005)) * salary
    print("You net salary is", round(net_salary), "euros.")
if net_salary <= 200:
    print("Get your money up!")


