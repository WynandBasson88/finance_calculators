# finance_calculators
## What the finance_calculators project is for
The finance_calculators project enables the user to access and use two different financial calculators:
* An investment calculator
* A home loan repayment calculator

If the **investment calculator** is selected from the menu the user will be asked to enter specific information about the investment:
* The amount being invested (A)
* The annual interest rate as a percentage
* The number of years the money will be invested (t)
* If the user wants **simple interest** or **compound interest**
  * The total investment is calculated using the formula below when **simple interest** is selected:  
  A = P(1 + r * t)
  * The total investment is calculated using the formula below when **compound interest** is selected:  
  A = P(1 + r) ^ t  
  In the formulas above the annual interest rate as a percentage / 100 = (r)

If the **home loan repayment calculator** is selected from the menu the user will be asked to enter specific information about the investment:
* The present value of the house (P)
* The annual interest rate as a percentage
* The number of months over which the bond will be repaid (n)
 * The amount to be repaid on a home loan each month is calculated using the formula below:  
 x = (i * P) / (1 - (1 + i) ^ (-n))  
 In the formula above the annual interest rate as a percentage / 12 / 100 = (i)
 
 The goal of this project was to build two financial calculators using the Python programming language. 
 This project can be used by anyone who wants to calculate the total of an investment after an amount of years or the amount to be repaid on a home loan each month. 

## Instructions for how to test the code
* Download the finance_calculators.py file
* Ensure you have Python 3.8 installed on your computer
* Open the file using your IDE (Integrated Development Environment) of choice such as Python Idle, Phycharm, Anaconda etc.
* Run the code

## Contact information
Wynand Basson  
bassonwynand@gmail.com  
https://github.com/WynandBasson88
