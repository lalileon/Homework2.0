salary = input("What is your gross salary?")
number_children = input("How many children do you have?")

try:
    salary = int(salary)
    number_children = int(number_children)

except ValueError:
    print("Sorry, both of the answers have to be a valid number.")
    exit()

if salary < 1000:
    net_salary = (0.9+(number_children*0.01))*salary
    print("You net salary is", round(net_salary), "euros.")
elif 1000 <= salary < 2000:
    net_salary = (0.88+(number_children*0.01))*salary
    print("You net salary is", round(net_salary), "euros.")
elif 2000 <= salary < 4000:
    net_salary = (0.86+(number_children*0.005))*salary
    print("You net salary is", round(net_salary), "euros.")
else:
    net_salary = (0.82+(number_children*0.005))*salary
    print("You net salary is", round(net_salary), "euros.")
