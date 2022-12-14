#DSC 510-T304
#Week 2
#Programming Assignment 2.1
#Author Breanna Parker
#9/11/22

# Display a welcome message for your user.
# Retrieve the company name from the user.
# Retrieve the number of feet of fiber optic cable to be installed from the user.
# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
# Include appropriate comments throughout the program.
# Your program should adhere to PEP8 guidelines especially as it pertains to variable names.

from unicodedata import name


user_name = input('What is your name?\n')
print("Hello",user_name)

company_name = input("What is your company name?\n") #user's company
num_feet_optic_cable = float(input("What is the number of feet of fiber optic cable to be installed?\n")) #input from user number of feet needed
cost_per_foot = 0.87 #designated cost per foot
two_decimals = "{:.2f}".format(cost_per_foot) #making sure decimals are included in calculations
cost = num_feet_optic_cable * cost_per_foot #calculating total cost for user
cost = round(cost,2) #rounding cost to two decimal places

#final printed recipe
print("Recipt for", user_name)
print("Company Name:",company_name)
print("Number of Optic Feet:", num_feet_optic_cable,"ft") 
print("Cost per foot:", "$",two_decimals)
print("Total Cost:","$", cost)
