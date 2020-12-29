import math

# Display the two calculation options to the user and explain each option
print("\nChoose either 'Investment' or 'Bond' from the menu below to proceed: ")
print("\nInvestment\t- To calculate the amount of interest you'll earn on an investment")
print("Bond\t\t- To calculate the amount of interest you'll have to pay on a home loan")

# Ask the user to type either 'Investment' or 'Bond'
# Entries Investment, investment, INVESTMENT, InVeStMeNt, Bond, bond, BOND, BoNd should't effect the program
calc_choice = input("\nPlease choose an option (Type either 'Investment' or 'Bond'): ")
calc_choice = calc_choice.lower()

# Display an error message to the user if he did not type either 'Investment' or 'Bond'
if (calc_choice != "investment" and calc_choice != "bond"):
    print("You did not select an appropriate option. Please run the program again and type either 'Investment' or 'Bond'!")

# Else if the user types 'Investment' ask the user to input relevant information
elif (calc_choice == "investment"):
    amount_invested = float(input("Please enter the amount of money that you are investing: "))
    
    interest_rate = input("Please enter the percentage of the interest rate on the investment per year: ")
    interest_rate = float(interest_rate.strip('%'))
    rate = interest_rate / 100

    years_invest = int(input("How many years do you want to invest for: "))

# Ask the user to type either 'Simple' or 'Compound'
# Entries Simple, simple, SIMPLE, SiMpLe, Compound, compound, Compound, CoMpOuNd should't effect the program
    interest_type = input("Please choose between 'Simple' or 'Compound' interest (Type either 'Simple' or 'Compound'): ")
    interest_type = interest_type.lower()

# Display an error message to the user if he did not type either 'Simple' or 'Compound'
    if (interest_type != "simple" and interest_type != "compound"):
        print("You did not select an appropriate option. Please run the program again and type either 'Simple' or 'Compound'!")

# Else if the user types 'Simple' calculate the interest on his investment
    elif (interest_type == "simple"):
        total_amount = amount_invested * (1 + rate * years_invest)
        print("The total amount of your investment will be: R{} if you invest an amount of R{} for {} years at {}% interest rate per year with simple interest.".format(round(total_amount, 2), amount_invested, years_invest, interest_rate))

# Else if the user types 'Compound' calculate the interest on his investment
    elif (interest_type == "compound"):
        total_amount = amount_invested * math.pow((1 + rate), years_invest)
        print("The total amount of your investment will be: R{} if you invest an amount of R{} for {} years at {}% interest rate per year with compound interest.".format(round(total_amount, 2), amount_invested, years_invest, interest_rate))

# Else if the user types 'Bond' ask the user to input relevant information
elif (calc_choice == "bond"):
    present_value = float(input("Please enter the present value of your house: "))

    annual_interest = input("Please enter the annual interest rate on your house loan: ")
    annual_interest = float(annual_interest.strip('%'))
    monthly_interest = annual_interest / 12 / 100       # Divided by 100 to get the rate
    

    months_repay = int(input("The number of months over which the bond on your house will be repaid: "))

# Calculate the amount the user will have to repay on his house bond every month
    monthly_amount = (monthly_interest * present_value) / (1 - math.pow((1 + monthly_interest), (-months_repay)))
    print("The monthly amount you have to repay on your house bond is: R{}".format(round(monthly_amount, 2)))
