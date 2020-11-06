#ps1b.py
total_cost = float (input ("Enter total cost of your dream house: "))
portion_down_payment = (float (input ("Enter down payment percent of total cost: "))) * total_cost
annual_salary = float (input ("Enter your starting annual salary: "))
monthly_portion_saved = (float (input ("Enter the average percent of your salary to save: "))) * annual_salary / 12
semi_annual_raise = float (input ("Enter semi-annual salary raise: "))

current_savings = 0
number_of_months = 0
total_savings = 0
while current_savings < portion_down_payment:
    total_savings = current_savings * (1+ (.04 / 12)) + monthly_portion_saved
    current_savings = total_savings
    number_of_months += 1
    if number_of_months in range(6, number_of_months + 1, 6):
    # if number_of_months % 6 == 0:
        monthly_portion_saved = monthly_portion_saved * (1 + semi_annual_raise)

print ("Number of months = ", number_of_months)