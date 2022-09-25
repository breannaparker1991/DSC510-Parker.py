#DSC 510-T304
#Week 3
#Programming Assignment 3.1
#Author Breanna Parker
#9/17/22

# Display a welcome message for your program.
# Get the company name from the user.
# Get the number of feet of fiber optic cable to be installed from the user.
# Evaluate the total cost based upon the number of feet requested.
# Display the calculated information including the number of feet requested and company name.

user_name = input('What is your name?\n')
print("Hello",user_name)

company_name = input("What is your company name?\n") #user's company
num_feet_optic_cable = float(input("What is the number of feet of fiber optic cable to be installed?\n")) #input from user number of feet needed

if (num_feet_optic_cable > 500):
  cost_per_foot = 0.50
elif (num_feet_optic_cable > 250):
  cost_per_foot = 0.70
elif (num_feet_optic_cable > 100):
  cost_per_foot = 0.80
elif (num_feet_optic_cable <=0):
  cost_per_foot = 0.00
  print("Error, please submit a positive number")
else:
  cost_per_foot = 0.87



two_decimals = "{:.2f}".format(cost_per_foot) #making sure decimals are included in calculations
cost = num_feet_optic_cable * cost_per_foot #calculating total cost for user
cost = round(cost,2) #rounding cost to two decimal places

#final printed recipe
print("Recipt for", user_name)
print("Company Name:",company_name)
print("Number of Optic Feet:", num_feet_optic_cable,"ft") 
print("Cost per foot:", "$",two_decimals)
print("Total Cost:","$", cost)
