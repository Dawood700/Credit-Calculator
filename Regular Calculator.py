import math
calc = input("What do you want to calculate? \n type 'n' - for count of months, \n type 'a' - for annuity monthly payment \n type 'p' - for credit principal \n type 'd' - for differentiated payment \n")


# functions
def n():
    principal = float(input("Enter credit principal: "))
    monthly = float(input("Enter monthly payment: "))
    interest = float(input("Enter credit interest: "))
    rate = interest / (1200)
    log = math.log(monthly / (monthly - rate * principal), 1 + rate)
    true_log = math.ceil(log)
    cost = monthly * true_log
    overpay = math.ceil(cost - principal)
    if true_log == 12:
        return("You need 1 year to repay this credit \n Overpay: {overpay}")
    elif true_log < 12:
        return(f"You need {true_log} months to repay this credit \n Overpay: {overpay}")
    elif true_log > 12:
        years = int(true_log / 12)
        months = true_log % 12
        return(f"You need {years} years and {months} months to pay off this credit \n Overpay: {overpay}")


def a():
    principal = float(input("Enter credit principal: "))
    period = float(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    rate = interest / (12 * 100)
    annuity = math.ceil(principal * ((rate * (1 + rate)**period) / ((1 + rate)**period - 1)))
    overpay = math.ceil((annuity * period) - principal)
    return(f"Your annuity payment is {annuity} \n Overpay: {overpay}")


def p():
    monthly_payment = float(input("What is your monthly payment?: "))
    period = float(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    rate = interest / (12 * 100)
    credit_principal = int(monthly_payment / ((rate * (1 + rate)**period) / ((1 + rate)**period - 1)))
    overpay = math.ceil((monthly_payment * period) - credit_principal)
    return(f"Your credit principal is {credit_principal} \n Overpay: {overpay}")


def d():
    principal = float(input("Enter credit principal: "))
    periods = float(input("Enter count of periods: "))
    interest = float(input("Enter credit interest: "))
    rate = interest / (12 * 100)
    number = 0
    diff_tot=0
    while number < periods:
      number +=1
      diff = math.ceil((principal / periods) + rate * (principal - (principal * (number - 1) / periods)))
      diff_tot +=diff
      overpay = math.ceil(diff_tot - principal)
      print(f"Month {number}: paid out {diff}")
    return(f"Overpay: {overpay}")


# if statements
if calc == "n":
    print(n())

elif calc == "a":
    print(a())

elif calc == "p":
    print(p())

elif calc == "d":
    print(d())
