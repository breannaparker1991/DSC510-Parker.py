#DSC 510-T304
#Week 4
#Programming Assignment 4.1 (added a function)
#Author Breanna Parker
#9/25/22
# A welcome message.
# A function with two parameters.
# A call to the function.
# The application should calculate the cost based upon the number of feet being ordered.
# A printed message displaying the company name and the total calculated cost.
# All costs should display in USD Currency Format Ex: $123.45.
# Your program must have a properly defined main method and a properly defined call to main

import server
print(server.main("Hello"))

def order_for_customer(num_feet_optic_cable): #added function
  company_name = input("What is your company name?\n") #request company name
  # num_feet_optic_cable = float(input("What is the number of feet of fiber optic cable to be installed?\n")) #removed because input changed to function
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
  print("Company Name:",company_name)
  print("Number of Optic Feet:", num_feet_optic_cable,"ft") 
  print("Cost per foot:", "$",two_decimals)
  print("Total Cost:","$", cost)

order_for_customer(4)