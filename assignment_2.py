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

user_name = input('What is your name?\n')
print("Hello",user_name)

company_name = input("What is your company name?\n")
num_feet_optic_cable = input("What is the number of feet of fiber optic cable to be installed?\n")
num_feet_optic_cable = int(num_feet_optic_cable)
cost_per_foot = int(0.87)

cost = num_feet_optic_cable * 0.87

print("Company Name:",company_name)
print("Number of Optic Feet:", num_feet_optic_cable) 
print("Cost per foot:", cost_per_foot)
print("Total Cost:", cost)