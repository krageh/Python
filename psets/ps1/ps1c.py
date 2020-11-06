# #ps1c.py (to problem statement)
# total_cost = float(1000000)
# portion_down_payment = float(.25 * total_cost)
# annual_salary = float(input ("Enter your starting annual salary: "))
# semi_annual_raise = float(.07)

# x = [0.0, 1.0]

# number_of_months = 0
# current_savings = 0
# total_savings = 0
# y = float(x[0])
# monthly_portion_saved = y * annual_salary / 12
# while number_of_months < 36:
#     total_savings = current_savings * (1 + (.04 / 12)) + monthly_portion_saved
#     current_savings = total_savings
#     number_of_months += 1
#     if number_of_months % 6 == 0:
#         monthly_portion_saved = monthly_portion_saved * (1 + semi_annual_raise)
# print (current_savings)
# if 0 < abs(current_savings - portion_down_payment) < 100:
#     print ("root = ", y)

# number_of_months = 0
# current_savings = 0
# total_savings = 0
# y = float(x[1])
# monthly_portion_saved = y * annual_salary / 12
# while number_of_months < 36:
#     total_savings = current_savings * (1 + (.04 / 12)) + monthly_portion_saved
#     current_savings = total_savings
#     number_of_months += 1
#     if number_of_months in range (6, 37, 6):
#         monthly_portion_saved = monthly_portion_saved * (1 + semi_annual_raise)
# print (current_savings)
# if 0 < abs(current_savings - portion_down_payment) < 100:
#     print ("root = ", y)
# elif current_savings < portion_down_payment:
#     print ("Unfortunately, that is not feasible.")
    
# else:
#     i = 2
#     while abs(current_savings - portion_down_payment) > 100:
#         number_of_months = 0
#         current_savings = 0
#         total_savings = 0
#         y = (x[0] + x[1]) / 2
#         monthly_portion_saved = y * annual_salary / 12
#         while number_of_months < 36:
#             total_savings = current_savings * (1 + (.04 / 12)) + monthly_portion_saved
#             current_savings = total_savings
#             number_of_months += 1
#             if number_of_months in range (6, 37, 6):
#                 monthly_portion_saved = monthly_portion_saved * (1 + semi_annual_raise)

#         i +=1
#         if current_savings < portion_down_payment:
#             x[0] = (x[0] + x[1])/2

#         elif current_savings > portion_down_payment:
#             x[1] = (x[0] + x[1])/2
        
#     print ("root = ", y)
#     print (i)


#ps1c.py (to answers)
total_cost = float(1000000)
portion_down_payment = float(.25 * total_cost)
annual_salary = float(input ("Enter your starting annual salary: "))
semi_annual_raise = float(.07)

epsilon = 100
number_of_guesses = 0
low = 0.0
high = 1.0

current_savings = 0
total_savings = 0
number_of_months = 0


# saving the whole entire salary
monthly_portion_saved = high * annual_salary / 12
while number_of_months != 36:
    total_savings = current_savings * (1 + (.04 / 12)) + monthly_portion_saved
    current_savings = total_savings
    number_of_months += 1
    if number_of_months % 6 == 0:
        monthly_portion_saved = monthly_portion_saved * (1 + semi_annual_raise)

if current_savings < portion_down_payment:
    print ("Unfortunately, that is not feasible.")

else:
    number_of_guesses = 0
    while (True):
        current_savings = 0.00
        total_savings = 0.00
        number_of_months = 0
        epsilon = 100
        number_of_guesses += 1
        
        guess = (low + high) / 2.0
        monthly_portion_saved = guess * annual_salary / 12.00

        # while (portion_down_payment - current_savings) > epsilon:
        while portion_down_payment > current_savings:
            total_savings = current_savings * (1 + (.04 / 12)) + monthly_portion_saved
            current_savings = total_savings
            number_of_months += 1
            if number_of_months % 6 == 0:
                monthly_portion_saved = monthly_portion_saved * (1 + semi_annual_raise)
        if number_of_months > 36:
            low = guess
        elif number_of_months < 36:
            high = guess
        else:
            if (current_savings - portion_down_payment) > epsilon:
                high = guess
            else:
                break

                    
    print ("Best savings rate would be", round (guess, 4))
    print (number_of_guesses)
    print (current_savings)

        
    





    