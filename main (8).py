#Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
# Write your solution here
# Ask for the hourly wage, hours worked, and the day of the week
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_the_week = input("Day of the week: ")

# Calculate the daily wages
if day_of_the_week.lower() == "sunday":
    daily_wages = hourly_wage * hours_worked * 2
else:
    daily_wages = hourly_wage * hours_worked

# Print the daily wages
print("Daily wages: {:.1f} euros".format(daily_wages))












