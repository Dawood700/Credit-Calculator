import math
import argparse

parser = argparse.ArgumentParser() # Add command line arguments
parser.add_argument("--type", type=str) # Add "type" argument
parser.add_argument("--payment", type=float) # Add "type" argument
parser.add_argument("--principal", type=float) # Add "principal" argument
parser.add_argument("--periods", type=float) # Add "periods" argument
parser.add_argument("--interest", type=float) # Add "interest" argument
args = parser.parse_args()

def p():
  try:
    rate = args.interest / (12 * 100) # Interest rate
    credit_principal = math.ceil(args.payment / ((rate * (1 + rate)**args.periods) / ((1 + rate)**args.periods - 1))) # Finds credit principal
    overpay = math.ceil((args.payment * args.periods) - credit_principal) # Finds overpayment
    return(f"Your credit principal is {credit_principal} \n Overpay: {overpay}")
  except TypeError:
    print("Incorrect parameters.")
    
def a():
  try:
    rate = args.interest / (12 * 100) # Interest rate
    annuity = math.ceil(args.principal * ((rate * (1 + rate)**args.periods) / ((1 + rate)**args.periods - 1))) # Finds annuity payment
    overpay = math.ceil((annuity * args.periods) - args.principal) # Finds ovrpayment
    return(f"Your annuity payment is {annuity} \n Overpay: {overpay}")
  except TypeError:
    print("Incorrect parameters.")
    
def d():
  try:
    rate = args.interest / (12 * 100) # Interest rate
    number = 0 # The number of months user must pay
    diff_tot=0 # Sum of each months payment
    while number < args.periods:
      number +=1 # For each new month, add '1' to the number
      diff = math.ceil((args.principal / args.periods) + rate * (args.principal - (args.principal * (number - 1) / args.periods))) #Finds differentiated payment
      diff_tot +=diff # Add all monthly payments
      overpay = math.ceil(diff_tot - args.principal) # Find overpay
      print(f"Month {number}: paid out {diff}")
    return(f"Overpay: {overpay}")
  except TypeError:
    print("Incorrect parameters.")
    
def n():
  try:
    rate = args.interest / (12 * 100) # Interest rate
    log = math.log(args.payment / (args.payment - rate * args.principal), 1 + rate) # Use the log function to find how many months a user will have to pay
    true_log = math.ceil(log) # Round the log fuction up
    cost = args.payment * true_log # How much user will pay
    overpay = math.ceil(cost - args.principal) # Finds overpay
    if true_log == 12:
        return("You need 1 year to repay this credit \n Overpay: {overpay}")
    elif true_log < 12:
        return(f"You need {true_log} months to repay this credit \n Overpay: {overpay}")
    elif true_log > 12:
        years = int(true_log / 12)
        months = true_log % 12
        return(f"You need {years} years and {months} months to pay off this credit \n Overpay: {overpay}")
  except TypeError:
    print("Incorrect parameters.")
       
if args.type == "diff":
  print(d())
  
elif args.type == "annuity":
  if args.payment and args.periods:
    print(p())
  elif args.principal and args.periods:
    print(a())
  elif args.principal and args.payment:
    print(n())


